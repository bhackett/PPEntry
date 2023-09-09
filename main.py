
import ttkbootstrap as ttk
from ttkbootstrap import Style
# from ttkbootstrap.constants import *

root = ttk.Window()

style = Style(theme='darkly')

y = 0

l0 = ttk.Label(root, text="FS URL", width=10).grid(row=y, column=5)
e0 = ttk.Entry(root, style='info.TEntry', width=30).grid(row=y, column=25)

y += 20

l1 = ttk.Label(root, text="FindAGrave", width=10).grid(row=y, column=5)
e1 = ttk.Entry(root, style='info.TEntry', width=30).grid(row=y, column=25)

y += 20

l2 = ttk.Label(root, text="PplLegacy", width=10).grid(row=y, column=5)
e2 = ttk.Entry(root, style='info.TEntry', width=30).grid(row=y, column=25)

y += 20

l3 = ttk.Label(root, text="Oldest Grav", width=10).grid(row=y, column=5)
e3 = ttk.Entry(root, style='info.TEntry', width=30).grid(row=y, column=25)

root.mainloop()

