from tkinter import ttk, constants
from services.tables import get_tables
from services.tables import delete_table

class TableView:
    def __init__(self,root,handle_start,handle_open):
        self.root = root
        self.frame = None
        self.handle_start = handle_start
        self.handle_open = handle_open
        self.initialize()

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()
    
    def open(self):
        self.handle_open(self.tables.get())
    def del_table(self):
        delete_table(self.tables.get())

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        label = ttk.Label(self.frame,text="Choose table to view")
        self.tables = ttk.Combobox(self.frame,values=get_tables())
        startbutton = ttk.Button(
                self.frame,
                text="Back \n to \n menu",
                command=self.handle_start)
        openbutton = ttk.Button(
                self.frame,
                text="Open \n selected \n table",
                command = self.open)
        delbutton = ttk.Button(
                self.frame,
                text="Delete \n table",
                command = self.del_table
                )
        label.grid(row=0,column=1)
        self.tables.grid(row=1, column=1)
        startbutton.grid(row=0,column=0,rowspan=2,sticky=(constants.S,constants.N))
        openbutton.grid(row=0,column=2,rowspan=2,sticky=(constants.S,constants.N))
        delbutton.grid(row=0,column=3,rowspan=2,sticky=(constants.S,constants.N))
