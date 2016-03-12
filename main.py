# encoding=utf8

from Transformer.Transformer import Transformer
from Transformer.TransformLoader.TransformerLoader import  TransformerLoader
from GUI.Window import Window
import Tkinter as Tk

window = Window()
transformer = Transformer(TransformerLoader())
content = ""
try:
    content = window.clipboard_get()
except:
    pass
content = transformer.transform(content)

window.geometry("600x50")
window.bind("<Escape>", window.destroy)
window.input.insert(Tk.INSERT, content)
window.clipboard_clear()
window.clipboard_append(content)
window.after(20000, lambda: window.destroy())
window.mainloop()
