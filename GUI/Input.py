from Tkinter import Text


class Input(Text):
    def __init__(self, root):
        Text.__init__(self, bd=0, width=600, highlightthickness=0)
        self.master = root
        self.focus_force()
        self.pack()
