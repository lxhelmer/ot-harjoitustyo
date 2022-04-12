import unittest
from tkinter import Tk
from gui.gui import Gui
from gui.startmenu import StartMenu

class TestGui(unittest.TestCase):
    def setUp(self):
        self.test_window = Tk()
        self.test_gui = Gui(self.test_window)
    def test_first_state_none(self):
        self.assertEqual(self.test_gui.current_view, None) 
    def test_state_after_start(self):
        self.test_gui.start()
        self.assertEqual(type(self.test_gui.current_view), type(StartMenu(self.test_gui.root,self.test_gui.show_tableview,self.test_gui.show_createview,self.test_gui.exit)))
