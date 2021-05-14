#a tool to remotely control a group of Christie WU7K-M projectors using their network interfaces. This is the GUI version.

import tkinter as tk
from tkinter import ttk
import christie as projectorControl
import marantz as audioControl

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        root.title('Marquette Visualization Lab Control')
        root.geometry("450x580")

        s = ttk.Style()
        s.theme_use('vista')
        s.configure('header.TLabel', font=("TkDefaultFont", 16, "bold"))
        s.configure('TLabelframe.Label', font=("TkDefaultFont", 10, "bold"))
    
    def create_widgets(self):
        #header
        header = tk.Frame(root)
        ttk.Label(header, text='Marquette Visualization Lab Control', style='header.TLabel').pack()
        #ttk.Label(header, text='Select a command').pack()        
        header.pack(expand=False, fill='x', pady=10)

        #frame 1, projector
        frame1 = ttk.Labelframe(root, text='Projector Controls', labelanchor='n')
        ttk.Label(frame1, text='Power:').grid(row=0, column=0)
        ttk.Radiobutton(frame1, text='On', variable=b_ppower, value="p_on").grid(row=0, column=1, sticky="W")
        ttk.Radiobutton(frame1, text='Off', variable=b_ppower, value="p_off").grid(row=0, column=2, sticky="W")
        
        ttk.Label(frame1, text='Shutters:').grid(row=1, column=0)
        ttk.Radiobutton(frame1, text='Open', variable=b_shutters, value="p_open").grid(row=1, column=1, sticky="W")
        ttk.Radiobutton(frame1, text='Closed', variable=b_shutters, value="p_close").grid(row=1, column=2, sticky="W")
        
        ttk.Label(frame1, text='Floor Projectors:').grid(row=2, column=0)
        ttk.Radiobutton(frame1, text='Normal', variable=b_floor, value="p_floorOn").grid(row=2, column=1, sticky="W")
        ttk.Radiobutton(frame1, text='Disabled', variable=b_floor, value="p_floorOff").grid(row=2, column=2, sticky="W")
        
        ttk.Label(frame1, text='Stereo mode:').grid(row=3, column=0)
        ttk.Radiobutton(frame1, text='Frame Doubled', variable=b_3d, value="p_3d").grid(row=3, column=1, sticky="W")
        ttk.Radiobutton(frame1, text='Disabled', variable=b_3d, value="p_2d").grid(row=3, column=2, sticky="W")
        
        frame1.columnconfigure(0, pad=0, weight=2)
        frame1.columnconfigure(1, pad=0, weight=1)
        frame1.columnconfigure(2, pad=0, weight=1)
        frame1.rowconfigure(0, pad=15)
        frame1.rowconfigure(1, pad=15)
        frame1.rowconfigure(2, pad=15)
        frame1.rowconfigure(3, pad=15)
        frame1.pack(expand=False, fill='x', padx=10, pady=10)
        
        #frame 2, audio
        frame2 = ttk.Labelframe(root, text='Audio Controls', labelanchor='n')
        
        ttk.Label(frame2, text='Power:').grid(row=0, column=0)
        ttk.Radiobutton(frame2, text='On', variable=b_apower, value="a_PWON").grid(row=0, column=1, sticky="W")
        ttk.Radiobutton(frame2, text='Off', variable=b_apower, value="a_PWSTANDBY").grid(row=0, column=2, sticky="W")
        
        ttk.Label(frame2, text='Volume:').grid(row=1, column=0)
        volumeSlider = ttk.Scale(frame2, from_=0, to=99, variable=b_avolume)
        volumeSlider.grid(row=1, column=1, columnspan=2, sticky='EW', padx=10)
        volumeSlider.bind('<ButtonRelease-1>', lambda event: volumeChange(event))
        volumeSlider.bind('<Double-Button>', lambda event: onclick("a_reset"))

        frame2.columnconfigure(0, pad=0, weight=2)
        frame2.columnconfigure(1, pad=0, weight=1)
        frame2.columnconfigure(2, pad=0, weight=1)
        frame2.rowconfigure(0, pad=15)
        frame2.rowconfigure(1, pad=15)
        frame2.pack(expand=False, fill='x', padx=10, pady=10)

        #footer, info
        footer = ttk.Labelframe(text='Info', labelanchor='n')
        ttk.Label(footer, textvariable=infoarea).pack(pady=5)
        footer.pack(expand=True, fill='both', padx=10, pady=10)

def onclick(s):
    infoarea.set("Please wait...");
    app.update()
    if s[0] == 'p':
        infoarea.set(projectorControl.transmit(s[2:]))
        #infoarea.set(s[2:])
    elif s == "a_reset":
        infoarea.set(audioControl.transmit(s[2:]))
        infoarea.set(s[2:])
        b_avolume.set(60)
    elif s[0] == 'a':
        infoarea.set(audioControl.transmit(s[2:]))
        #infoarea.set(s[2:])
        
def volumeChange(s):
    infoarea.set("Please wait...");
    app.update()
    command = "MV" + str(b_avolume.get() * 10).zfill(3)
    infoarea.set(audioControl.transmit(command))
    #infoarea.set(command)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)

    #TK state variables
    #projector
    projectorStatus = projectorControl.startup()
    b_ppower = tk.StringVar()
    b_shutters = tk.StringVar()
    if projectorStatus["power"]:
        b_ppower.set("p_on")
    else:
        b_ppower.set("p_off")
    if projectorStatus["shutter"]:
        b_shutters.set("p_open")
    else:
        b_shutters.set("p_close")
    
    b_3d = tk.StringVar()
    b_floor = tk.StringVar()

    #audio
    audioStatus = audioControl.startup()
    b_apower = tk.StringVar()
    b_avolume = tk.IntVar(value=40)
    if audioStatus["power"]:
        b_apower.set("a_PWON")
    else:
        b_apower.set("a_PWSTANDBY")
        
    infoarea = tk.StringVar(value="Ready.")

    #callbacks
    b_ppower.trace_add('write', lambda *args: onclick(b_ppower.get()))
    b_apower.trace_add('write', lambda *args: onclick(b_apower.get()))
    b_shutters.trace_add('write', lambda *args: onclick(b_shutters.get()))
    b_3d.trace_add('write', lambda *args: onclick(b_3d.get()))
    b_floor.trace_add('write', lambda *args: onclick(b_floor.get()))    
    
    #keyboard shortcuts
    root.bind('<Escape>', lambda x: root.destroy())
    
    app.create_widgets()      
    app.mainloop()
