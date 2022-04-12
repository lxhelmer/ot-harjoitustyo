from tkinter import Tk, ttk
from gui.startmenu import StartMenu
from gui.tableview import TableView

class GUI:
    def __init__(self,root):
        self.root = root
        self.current_view = None

    def start(self):
        self.show_start_menu()
    
    def stop_current_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_start_menu(self):
        self.stop_current_view()
        self.current_view = StartMenu(self.root,
                self.show_tableview,
                self.show_createview,
                self.exit
                )
        self.current_view.pack()
    
    def show_tableview(self):
        self.stop_current_view()
        self.current_view = TableView(self.root,self.show_start_menu)
        self.current_view.pack()
    def show_createview(self):
        self.stop_current_view()
    def exit(self):
        self.root.destroy()


