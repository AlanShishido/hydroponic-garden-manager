import sys, os.path
import tkinter as tk
from tkinter import ttk
from functools import partial
from PIL import ImageTk, Image

import colors
# from . import colors

root = tk.Tk()
root.title("Qualidade dos Nutrientes da Hidroponia de alface")
pad = 15
# widthMaxPx = root.winfo_screenwidth()
widthMaxPx = 600
# heightMaxPx = root.winfo_screenheight()
heightMaxPx = 400
root.geometry("{0}x{1}+0+-3".format(widthMaxPx-pad, heightMaxPx-pad))
# root["bg"] = colors.AERO_BLUE

# cabeçalho
ctHeader = tk.Frame(root, bg=colors.AERO_BLUE)
lbH1 = tk.Label(ctHeader, text="Hidroponia de Alfaces", bg=colors.AERO_BLUE, font=("Roboto",32, "bold"))

ctHeader.pack(side=tk.TOP,fill='x')
lbH1.pack(side=tk.LEFT, expand=1)


root.mainloop()