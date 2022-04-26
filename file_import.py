from tkinter.filedialog import askopenfilename
## OR  from tkinter.filedialog import *

from tkinter import *

root = Tk()
foo = askopenfilename()
root.destroy()
print(foo)

