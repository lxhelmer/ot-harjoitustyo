from tkinter import ttk, constants

class CreateView:
    def __init__(self,root,handle_start):
        self.root = root
        self.frame = None
        self.handle_start = handle_start
        self.handle_open = None
        self.entrytext = ""

        self.initialize()

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        label = ttk.Label(self.frame,text="Create new table \n input name here")
        startbutton = ttk.Button(self.frame,text="Back \n to \n menu",command=self.handle_start)
        createnew = ttk.Button(self.frame, text="Create \n new \n table")
        nameentry = ttk.Entry(self.frame, textvariable = self.entrytext)

        label.grid(row=0,column=1)
        nameentry.grid(row=1, column=1)
        createnew.grid(row=0,column=2,rowspan=2,sticky=(constants.S,constants.N))
        startbutton.grid(row=0,column=0,rowspan=2,sticky=(constants.S,constants.N))
