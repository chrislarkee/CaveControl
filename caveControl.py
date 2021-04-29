#a tool to remotely control a group of Christie WU7K-M projectors using their network interfaces. This is the GUI version.

import tkinter as tk
from tkinter import ttk
from christie import transmit

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        root.title('Marquette Visualization Lab Control')
        root.geometry("450x470")

        s = ttk.Style()
        s.theme_use('vista')
        s.configure('Heading.TLabel', font=('Helvetica Bold', 14))
        #s.configure('TLabel', font=('Helvetica', 11))
    
    def create_widgets(self):
        #header
        header = tk.Frame(root)
        ttk.Label(header, text='Marquette Visualization Lab Control', style='Heading.TLabel').pack()
        ttk.Label(header, text='Select a command').pack()
        ttk.Separator(header).pack(expand=True, fill='x', pady=10)
        header.pack(expand=False, fill='x', pady=10)

        #main area layout
        f = tk.Frame(root)
        ttk.Label(f, text='Power:').grid(row=0, column=0)
        ttk.Radiobutton(f, text='On', variable=p_power, value="on").grid(row=0, column=1, sticky="W")
        ttk.Radiobutton(f, text='Off', variable=p_power, value="off").grid(row=0, column=2, sticky="W")

        ttk.Label(f, text='Shutters:').grid(row=1, column=0)
        ttk.Radiobutton(f, text='Open', variable=p_shutters, value="open").grid(row=1, column=1, sticky="W")
        ttk.Radiobutton(f, text='Closed', variable=p_shutters, value="close").grid(row=1, column=2, sticky="W")
        
        ttk.Label(f, text='Stereo:').grid(row=2, column=0)
        ttk.Radiobutton(f, text='Frame Doubled', variable=p_3d, value="3d").grid(row=2, column=1, sticky="W")
        ttk.Radiobutton(f, text='Disabled', variable=p_3d, value="2d").grid(row=2, column=2, sticky="W")

        ttk.Label(f, text='Floor:').grid(row=3, column=0)
        ttk.Radiobutton(f, text='Normal', variable=p_floor, value="floorOn").grid(row=3, column=1, sticky="W")
        ttk.Radiobutton(f, text='Disabled', variable=p_floor, value="floorOff").grid(row=3, column=2, sticky="W")

        f.columnconfigure(0, pad=0, weight=2)
        f.columnconfigure(1, pad=0, weight=1)
        f.columnconfigure(2, pad=0, weight=1)
        f.rowconfigure(0, pad=20)
        f.rowconfigure(1, pad=20)
        f.rowconfigure(2, pad=20)
        f.rowconfigure(3, pad=20)
        f.pack(expand=False, fill='x', padx=10, pady=0)        

        #footer
        footer = tk.Frame(root)
        ttk.Separator(footer).pack(expand=True, fill='x', pady=5)
        ttk.Label(footer, textvariable=p_info).pack(pady=5)
        footer.pack(expand=False, fill='x', pady=0)

def onclick(s):
    p_info.set("Please wait...");
    app.update()
    p_info.set(transmit(s));
    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    
    #state variables & callbacks
    p_power = tk.StringVar()
    p_shutters = tk.StringVar()
    p_3d = tk.StringVar()
    p_floor = tk.StringVar()
    p_command = tk.StringVar()
    p_info = tk.StringVar(value="")
    p_power.trace_add('write', lambda *args: p_command.set(p_power.get()))
    p_shutters.trace_add('write', lambda *args: p_command.set(p_shutters.get()))
    p_3d.trace_add('write', lambda *args: p_command.set(p_3d.get()))
    p_floor.trace_add('write', lambda *args: p_command.set(p_floor.get()))
    p_command.trace_add('write', lambda *args: onclick(p_command.get()))
    
    #keyboard shortcuts
    root.bind('<Escape>', lambda x: root.destroy())
    
    app.create_widgets()
    app.mainloop()
