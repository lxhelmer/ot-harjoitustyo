from tkinter import Tk,ttk
from gui.gui import GUI

window = Tk()
window.title("Simple Manager")
window.minsize(500,150)

gui = GUI(window)   #root for ui class
gui.start()


window.mainloop()
