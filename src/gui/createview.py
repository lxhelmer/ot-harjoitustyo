import tkinter as tk
from tkinter import ttk, constants
from services.tables import create_table,make_columns

class CreateView:
    def __init__(self,root,handle_start,handle_disp):
        self.root = root
        self.frame = None
        self.handle_start = handle_start
        self.handle_open = handle_disp
        self.entrytext = ""
        self.columns = [] 
        
        self.initialize()

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()
    def warning(self,warn):
        self.warninglabel.config(text=warn)
    def create_new(self):
        if (self.nameentry.get()=="" or self.colentry.get() == ""):
            self.warning("input not sufficient")
            return
        if (", " not in self.colentry.get()):
            self.warning("column names must be separated with <, >")
            return
        if (self.colentry.get().rstrip()[-1] == ","):
            self.warning("don't end in empty named column")
            return

        parts = self.colentry.get().split(", ")
        testset = set(parts)
        if len(parts) != len(testset):
            self.warning("column names must be unique")
        else:
            self.columns = make_columns(self.colentry.get())
            create_table(self.nameentry.get(),self.columns)
            self.handle_open(self.nameentry.get())
    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        label = ttk.Label(self.frame,text="Create new table \n input name here")
        startbutton = ttk.Button(self.frame,text="Back \n to \n menu",command=self.handle_start)
        createnew = ttk.Button(self.frame, text="Create \n new \n table",command=self.create_new)
        self.nameentry = ttk.Entry(self.frame, textvariable = self.entrytext)
        
        self.warninglabel = ttk.Label(self.frame,text="",foreground='#f00')

        text = ttk.Label(
                self.frame,
                text="Input columns in form <name> <type>.\nSeparate by ', ' and give primary value first"
                )
        self.colentry = ttk.Entry(self.frame, textvariable="")

        label.grid(row=0,column=1)
        self.nameentry.grid(row=1, column=1)
        createnew.grid(row=0,column=2,rowspan=2,sticky=(constants.S,constants.N))
        startbutton.grid(row=0,column=0,rowspan=2,sticky=(constants.S,constants.N))
        text.grid(row=2,column=1,pady=4)
        self.colentry.grid(row=3,column=1)
        self.warninglabel.grid(row=4,column=1)
