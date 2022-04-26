from gui.startmenu import StartMenu
from gui.tableview import TableView
from gui.createview import CreateView
from gui.dispview import DispView

class Gui:
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
        self.current_view = TableView(self.root,self.show_start_menu,self.show_dispview)
        self.current_view.pack()
    def show_createview(self):
        self.stop_current_view()
        self.current_view = CreateView(self.root,self.show_start_menu)
        self.current_view.pack()

    def show_dispview(self):
        self.stop_current_view()
        self.current_view = DispView(self.root,self.show_tableview)
        self.current_view.pack()
    def exit(self):
        self.root.destroy()
