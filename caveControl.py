#!/usr/bin/env python

#GUI
import wx
from data.layout import maingui
from datetime import datetime

#transmissions
from threading import Thread, active_count
import socket       #for christie
import telnetlib    #for marantz

class Transmit():
    def __init__(self):
        self.callback = None
        #projectors
        self.ips = ["172.22.1." + str(i) for i in range(101,111)]
        
        #audio
        self.audioIP = "172.22.1.50"        
        
    #dispatch to all projectors
    def allProjectors(self, command):
        for i in range(len(self.ips)):
            thr = Thread(target=self._transmitThread, args=(i, command))
            thr.start()
    
    #dispatch to 1 projector
    def projector(self, id, command):        
        thr = Thread(target=self._transmitThread, args=(id, command))
        thr.start()
        
    def _transmitThread(self, id, command):    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5.0)  
        ip = self.ips[int(id) - 1]
        try:
            s.connect((ip, 3002))
            s.send(("(#" + command + ")").encode())
            response = str(s.recv(1024).decode())
            self.callback.gridUpdate(id, response)
        except socket.timeout:
            self.callback.gridUpdate(id, "Timeout")
        s.close()        
    
    def audio(self, command):
        thr = Thread(target=self._transmitAudio, args=(command,))
        thr.start()
        
    def _transmitAudio(self, command):
        #is the connection still open?
        try: 
            self.tn.sock_avail()
        except:
            self.tn = telnetlib.Telnet()
            try:
                self.tn.open(self.audioIP, 23, 3)
            except:
                return

        try:
            self.tn.write((command + "\r").encode())
            #print(self.tn.read_eager().decode())
            #print(response)
            self.callback.gridUpdate(10, command)
        except:
            self.callback.gridUpdate(10, "Message error.")

    
class gui(maingui): 
    def __init__(self, parent):
        maingui.__init__(self, parent)      #initialize widgets
        transmit.callback = self            #connection to the GUI
        
        #initialize grid statuses        
        transmit.allProjectors("PWR?")
        transmit.audio("PW?")
        
        #set up the autoshutdown timer
        self.t = wx.Timer()
        self.t.Bind(wx.EVT_TIMER, self.autoShutdown)
        self.t.Start(60000)

    def refreshStatus( self, event ):  
        transmit.allProjectors("PWR?")
        transmit.audio("PW?")   

    def togglePower(self, event):
        if event.IsChecked():
            event.GetEventObject().SetLabel("ON")
            transmit.allProjectors("PWR1")
        else:
            #confirm power off, because the cooldown takes uninterruptible minutes
            dlg = wx.MessageDialog(None, "Are you sure you want to shut down the projectors?",'Confirm', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_YES:
                event.GetEventObject().SetLabel("OFF")
                transmit.allProjectors("PWR0")
            else:
                event.GetEventObject().SetValue(True)

    def toggleShutters(self, event):
        if event.IsChecked():
            event.GetEventObject().SetLabel("OPEN") 
            transmit.allProjectors("SHU0")
        else:
            event.GetEventObject().SetLabel("CLOSED")
            transmit.allProjectors("SHU1")
            
    def toggleFloor(self, event):
        if event.IsChecked():
            event.GetEventObject().SetLabel("OPEN")
            transmit.projector(1, "SHU0")
            transmit.projector(2, "SHU0")
            transmit.projector(7, "SHU0")
            transmit.projector(8, "SHU0")
            transmit.projector(9, "SHU0")
            transmit.projector(10, "SHU0")
        else:
            event.GetEventObject().SetLabel("CLOSED")
            transmit.projector(1, "SHU1")
            transmit.projector(2, "SHU1")
            transmit.projector(7, "SHU1")
            transmit.projector(8, "SHU1")
            transmit.projector(9, "SHU1")
            transmit.projector(10, "SHU1")

    def toggleStereo(self, event):
        if event.IsChecked():
            event.GetEventObject().SetLabel("ON")            
            transmit.allProjectors("TDM+MAIN5")
        else:
            event.GetEventObject().SetLabel("OFF")
            transmit.allProjectors("TDM+MAIN0")

    def toggleAudio(self, event):
        if event.IsChecked():
            event.GetEventObject().SetLabel("ON")
            transmit.audio("PWON")
        else:
            event.GetEventObject().SetLabel("OFF")
            transmit.audio("PWSTANDBY")

    def updateVolume(self, event):
        volume = "MV" + str(event.GetEventObject().GetValue()).zfill(2)
        transmit.audio(volume)
    
    #this def is only triggered by the timer made in init(), and no GUI event
    def autoShutdown(self, event):
        #is it 6pm?
        dt = datetime.now().strftime("%H%M")
        if dt != "1800":
            return
        
        #start another timer     
        self.shutdownTimer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.autoShutdownTimeout, self.shutdownTimer)
        self.shutdownTimer.StartOnce(15000)  # 15 seconds        
        
        #give a warning to the user
        self.shutdownDlg = wx.GenericMessageDialog(self, "The projectors will be automatically shutdown in 15 seconds...",'Auto-Shutdown', wx.OK | wx.ICON_WARNING)
        self.shutdownDlg.SetOKLabel("Cancel Shutdown")

        result = self.shutdownDlg.ShowModal()  
        self.shutdownTimer.Stop()     
            
    def autoShutdownTimeout(self, event):
        if self.shutdownDlg:
            self.shutdownDlg.EndModal(wx.ID_OK)
        self.c_ppower.SetLabel("OFF")
        transmit.allProjectors("PWR0")
        self.c_audio.SetLabel("OFF")
        transmit.audio("PWSTANDBY")

    #the threads call this when they're done
    def gridUpdate(self, id, message):
        self.grid.SetCellValue(row=id, col=0, s=message)
        
    def quit(self, event):
        self.t.Stop()           #the timer
        transmit.tn.close()     #the audio connection
        wx.Exit()
        

if __name__ == '__main__':
    app = wx.App(False)
    transmit = Transmit()        
    frame = gui(None)
    frame.Show()
    app.MainLoop()
   