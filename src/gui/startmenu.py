from tkinter import ttk

class StartMenu:
    def __init__(self, root,handle_tableview,handle_createview,handle_exit):
        self.root = root
        self.frame = None
        self.handle_table = handle_tableview
        self.handle_create = handle_createview
        self.handle_exit = handle_exit

        self.initialize()

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        label = ttk.Label(master=self.frame,
                text="What you wanna do")

        view_button = ttk.Button(
                master=self.frame,
                text="View tables",
                command=self.handle_table
        )

        create_button = ttk.Button(
                master=self.frame,
                text="Create Table",
                command=self.handle_create
        )

        exit_button = ttk.Button(
                master=self.frame,
                text="Exit",
                command=self.handle_exit
        )

        label.grid(row=0, column=1, padx=10, pady=5)
        view_button.grid(row=1,column=0,padx=5, pady=10)
        create_button.grid(row=1,column=1,padx=5, pady=10)
        exit_button.grid(row=1,column=2,padx=5, pady=10)
