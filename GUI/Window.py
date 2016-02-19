from Tkinter import Tk
from Input import Input


class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.input = Input(self)

    def destroy(self, *args):
        Tk.destroy(self)
