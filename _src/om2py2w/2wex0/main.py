# coding = utf-8
#!/user/bin/env python

import Tkinter as tk
import os
import sys
from ScrolledText import ScrolledText

reload(sys)
sys.setdefaultencoding('utf-8')

root = tk.Tk()
root.title("CHER'S DIARY")

def saveClick(self):
    f = open(os.getcwd()+'mydiary','w+')
    f.write(self.text.get()) 
	
	
def write():
    append_text(var.get())
    text_output.insert(0.0, text.get())
    var.set('')
	
master = tk.Frame(root)
master.pack()

text=tk.Text(master)

text=tk.StringVar(value="Hi, wanna talk? Here we go.")
text_insert = tk.Entry(master, textvariable = text)
text_insert.pack()

master.bind('<Return>',write)

scrl=ScrolledText(master)
scrl.pack()

save=tk.Button(master, text="save",fg='magenta',command=saveClick)
save.bind('<Command-Key-S>',saveClick) # doesn't work yet
save.pack()

quit=tk.Button(master, text="close",fg='magenta', command=master.quit)
quit.pack(side='bottom')

root.mainloop()