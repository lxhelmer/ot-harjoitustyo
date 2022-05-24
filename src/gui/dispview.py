from tkinter import ttk, constants
from repostories.entryrepo import EntryRepo


class DispView:
    def __init__(self,root,handle_tableview,table_name):
        self.root = root
        self.frame = None
        self.table_view = handle_tableview
        self.indexzero = 0

        self.table_name = table_name
        self.tablevalueset = []

        self.initialize()

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()

    def make_index(self,zero):
        for line in range(0,31):
            self.cell = ttk.Entry(self.indexframe)
            self.cell.grid(row=line,column=0)
            self.cell.insert("0",line+zero)

    def make_table(self):
        
        for y_line in range(0,31):
            for x_column in range(self.entryrepo.get_csize()):
                self.cell = ttk.Entry(self.tableframe)
                self.cell.grid(row=y_line,column=x_column)
                if y_line == 0:
                    self.entryrepo.get_colnames()
                    self.cell.insert("0",self.entryrepo.get_colnames()[x_column][0])
                else:
                    self.cell.insert("0","---")
    def fill_table(self):
        for y_line in range(0,len(self.tablevalueset)):
            print(self.tablevalueset[y_line])
            for x_column in range(0,self.entryrepo.get_csize()):
                self.cell = ttk.Entry(self.tableframe)
                self.cell.grid(row=y_line+1, column=x_column)
                print (self.tablevalueset[y_line][x_column])
                self.cell.delete("0","end")
                self.cell.insert("0",self.tablevalueset[y_line][x_column])
                
    def next_page(self):
        self.tablevalueset=self.entryrepo.get_next()
        self.indexzero += 30
        self.make_index(self.indexzero)
        self.make_table()
        self.fill_table()

    def last_page(self):
        if self.indexzero >=30:
            self.tablevalueset=self.entryrepo.get_last()
            self.indexzero -= 30
            self.make_index(self.indexzero)
            self.make_table()
            self.fill_table()

    def handle_add(self):
        self.entryrepo.insert_entry(self.entrybox.get())
        self.tablevalueset=self.entryrepo.get_first()
        self.fill_table()

    def handle_delete(self):
        self.entryrepo.delete_entry(self.delentry.get())
        self.tablevalueset=self.entryrepo.get_first()
        self.make_table()
        self.fill_table()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        name = ttk.Label(self.frame,text=self.table_name)
        back = ttk.Button(self.frame,text="Go back \n to \n tables",command=self.table_view)
        add = ttk.Button(self.frame,text="Add entry",command=self.handle_add)
        self.tableframe = ttk.Frame(master=self.frame)
        self.indexframe = ttk.Frame(master=self.frame)
        self.entrybox = ttk.Entry(self.frame,textvariable="")
        addinfo = ttk.Label(self.frame,text="Separate values with <, >")
        self.entryrepo = EntryRepo(self.table_name)

        delinfo = ttk.Label(self.frame,text="Input first real value \n of line to be deleted")
        self.delentry = ttk.Entry(self.frame,textvariable="")
        delbutton = ttk.Button(self.frame,text="Delete",command=self.handle_delete)

        self.tablevalueset = self.entryrepo.get_first()

        
        next = ttk.Button(self.frame,text="Next page \n --->",command=self.next_page)
        last = ttk.Button(self.frame,text="Last Page \n <---",command=self.last_page)
        
        self.make_index(0)
        self.make_table()
        self.fill_table()

        name.grid(row=0, column=2)
        self.tableframe.grid(row=1, column=2,rowspan=8,columnspan=2,sticky=(constants.S,constants.N))
        self.indexframe.grid(row=1, column=1,rowspan=8,sticky=(constants.S,constants.N))
        back.grid(row=0, column=0,rowspan=2,sticky=(constants.W,constants.N))
        add.grid(row=10,column=3)
        addinfo.grid(row=9,column=1)
        self.entrybox.grid(row=10,column=1,columnspan=2,sticky=(constants.E,constants.W)) 
        delinfo.grid(row=11,column=1)
        self.delentry.grid(row=12,column=1,columnspan=2,sticky=(constants.E,constants.W))
        delbutton.grid(row=12,column=3)

        next.grid(row=2,column=0,rowspan=2,sticky=(constants.N,constants.S))
        last.grid(row=4,column=0,rowspan=2,sticky=(constants.N,constants.S))

