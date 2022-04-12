from tkinter import ttk, constants

class TableView:
    def __init__(self,root,handle_start):
        self.root = root
        self.Frame = None
        self.handle_start = handle_start
        
        self.initialize()

    def destroy(self):
        self.frame.destroy()
        
    def pack(self):
        self.frame.pack()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        label = ttk.Label(self.frame,text="Choose table to view")
        tables = ttk.Combobox(self.frame,values=["a","b","c","d"])
        startbutton = ttk.Button(self.frame,text="Back \n to \n menu",command=self.handle_start)
        openbutton = ttk.Button(self.frame,text="Open \n selected \n table")
        label.grid(row=0,column=1)
        tables.grid(row=1, column=1)
        startbutton.grid(row=0,column=0,rowspan=2,sticky=(constants.S,constants.N))
        openbutton.grid(row=0,column=2,rowspan=2,sticky=(constants.S,constants.N))
