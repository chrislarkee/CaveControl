#a tool to remotely control a group of Christie WU7K-M projectors using their network interfaces. This is the GUI version.

import tkinter as tk
from tkinter import ttk
from christie import transmit as projectorTransmit
from marantz import transmit as audioTransmit

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        root.title('Marquette Visualization Lab Control')
        root.geometry("450x580")

        s = ttk.Style()
        s.theme_use('vista')
        s.configure('Heading.TLabel', font=("TkDefaultFont", 16, "bold"))
    
    def create_widgets(self):
        #header
        header = tk.Frame(root)
        ttk.Label(header, text='Marquette Visualization Lab Control', style='Heading.TLabel').pack()
        ttk.Label(header, text='Select a command').pack()
        #ttk.Separator(header).pack(expand=True, fill='x', pady=5)
        header.pack(expand=False, fill='x', pady=10)

        #frame 1, projector
        frame1 = ttk.Labelframe(root, text='Projector Controls')
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
        frame2 = ttk.Labelframe(root, text='Audio Controls')
        
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

        #footer
        footer = ttk.Labelframe(text='Info')
        ttk.Label(footer, textvariable=infoarea).pack(pady=5)
        footer.pack(expand=True, fill='both', padx=10, pady=10)

def onclick(s):
    infoarea.set("Please wait...");
    app.update()
    if s[0] == 'p':
        infoarea.set(projectorTransmit(s[2:]))
        #infoarea.set(s[2:])
    elif s == "a_reset":
        infoarea.set(audioTransmit(s[2:]))
        infoarea.set(s[2:])
        b_avolume.set(60)
    elif s[0] == 'a':
        infoarea.set(audioTransmit(s[2:]))
        #infoarea.set(s[2:])
        
def volumeChange(s):
    infoarea.set("Please wait...");
    app.update()
    command = "MV" + str(b_avolume.get() * 10).zfill(3)
    infoarea.set(audioTransmit(command))
    #infoarea.set(command)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    
    #state variables & callbacks
    b_ppower = tk.StringVar()
    b_shutters = tk.StringVar()
    b_3d = tk.StringVar()
    b_floor = tk.StringVar()
    b_apower = tk.StringVar()
    b_avolume = tk.IntVar(value=60)
    b_ppower.trace_add('write', lambda *args: command.set(b_ppower.get()))
    b_apower.trace_add('write', lambda *args: command.set(b_apower.get()))
    b_shutters.trace_add('write', lambda *args: command.set(b_shutters.get()))
    b_3d.trace_add('write', lambda *args: command.set(b_3d.get()))
    b_floor.trace_add('write', lambda *args: command.set(b_floor.get()))    
    
    infoarea = tk.StringVar(value="Ready.")
    command = tk.StringVar()
    command.trace_add('write', lambda *args: onclick(command.get()))
    
    #keyboard shortcuts
    root.bind('<Escape>', lambda x: root.destroy())
    
    app.create_widgets()      
    app.mainloop()
