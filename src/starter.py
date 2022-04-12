from tkinter import Tk
from gui.gui import Gui

window = Tk()
window.title("Simple Manager")
window.minsize(500,150)

gui = Gui(window)   #root for ui class
gui.start()


window.mainloop()
