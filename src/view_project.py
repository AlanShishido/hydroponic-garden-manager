import tkinter as tk
from tkinter import ttk
from functools import partial
from choices import ViewConstant as colors

root = tk.Tk()
root.title("Qualidade dos Nutrientes da Hidroponia de alface")
pad = 15
# widthMaxPx = 600
# heightMaxPx = 400
widthMaxPx = root.winfo_screenwidth()
heightMaxPx = root.winfo_screenheight()
root.geometry("{0}x{1}+0+-3".format(widthMaxPx-pad, heightMaxPx-pad))
# root["bg"] = colors.AERO_BLUE

# cabeçalho
ctHeader = tk.Frame(root, bg=colors.AERO_BLUE)
lbH1 = tk.Label(ctHeader, text="Hidroponia de Alfaces",
                bg=colors.AERO_BLUE, font=("Roboto", 32, "bold"))

ctHeader.pack(side=tk.TOP, fill='x')
lbH1.pack(side=tk.LEFT, expand=1)

root.mainloop()
