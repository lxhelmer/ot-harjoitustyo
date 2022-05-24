from tkinter import ttk, constants     


class DispView:
    def __init__(self,root,handle_tableview,table_name):
        self.root = root
        self.frame = None
        self.table_view = handle_tableview


        self.table_name = table_name #update to real value
        self.tablevalueset = [(1,"first", "forsta"),
                            (2,"second", "andra"),
                            (3,"third", "tredje")]
        self.table_y = 3
        self.table_x = 3

        self.initialize()

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        name = ttk.Label(self.frame,text=self.table_name)
        back = ttk.Button(self.frame,text="Go back \n to \n tables",command=self.table_view)
        tableframe = ttk.Frame(master=self.frame)

        for y_line in range(self.table_y):
            for x_column in range(self.table_x):
                self.cell = ttk.Entry(tableframe)
                self.cell.grid(row=y_line, column=x_column)
                self.cell.insert("0",self.tablevalueset[y_line][x_column])

        name.grid(row=0, column=1)
        tableframe.grid(row=1, column=1)
        back.grid(row=0, column=0,rowspan=2,sticky=(constants.S,constants.N))
