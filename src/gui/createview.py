from tkinter import ttk, constants
from services.tables import create_table

class CreateView:
    def __init__(self,root,handle_start,handle_disp):
        self.root = root
        self.frame = None
        self.handle_start = handle_start
        self.handle_open = handle_disp
        self.entrytext = ""
        
        
        self.columns = ["user text primary key","password text"]
        
        self.initialize()


        



    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()
    
    def create_new(self):
        create_table(self.nameentry.get(),self.columns)
        self.handle_open(self.nameentry.get())


    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        label = ttk.Label(self.frame,text="Create new table \n input name here")
        startbutton = ttk.Button(self.frame,text="Back \n to \n menu",command=self.handle_start)
        createnew = ttk.Button(self.frame, text="Create \n new \n table",command=self.create_new)
        self.nameentry = ttk.Entry(self.frame, textvariable = self.entrytext)

        label.grid(row=0,column=1)
        self.nameentry.grid(row=1, column=1)
        createnew.grid(row=0,column=2,rowspan=2,sticky=(constants.S,constants.N))
        startbutton.grid(row=0,column=0,rowspan=2,sticky=(constants.S,constants.N))
