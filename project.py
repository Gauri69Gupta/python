from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog 
import tkinter.messagebox
import tkinter.simpledialog

root=Tk()
root.title("My NotePad")
text=Text(root)
file=''
text=''
root.initialfile=("myfile.txt")
root.configure(width=90,height=80)
textPad=ScrolledText(root,width=200,height=200)

def newpopup():
    result = tkinter.messagebox.askyesno("SAVE","Do you want to save the current file")
    if result:
        saveas()
    else:
        new()
def new():
    root.title("Untitled")
    global file
    file ="untitled"
    textPad.delete(1.0,END)
    
def open():
   a =tkinter.filedialog.askopenfile(mode='r+')
   t=a.read()
   textPad.delete(1.0,END)
   textPad.insert(1.0,t)
   
def save():
    loc=tkinter.filedialog.asksaveasfile(mode='w')
    t = textPad.get("1.0",END)
    try:
        loc.write(t.rstrip())
    except:
        tkinter.messagebox.showerror(title="not saved",message='sorry')
        
def saveas():
    loc=tkinter.filedialog.asksaveasfile(mode='w')
    t = textPad.get("1.0",END)
    try:
        loc.write(t.rstrip())
    except:
        tkinter.messagebox.showerror(title="not saved",message='sorry')
def cut():
    sel =textPad.selection_get()
    clipboard = sel
    textPad.delete(SEL_FIRST, SEL_LAST)
    
    
def hello():
    label=tkinter.messagebox.showinfo("About","Have a nice day.. we love you ")
    
def show():
    label=tkinter.messagebox.showinfo("Info","You are using Gauri's Textpad")
    

def find():
    textPad.tag_remove('found', '1.0', END)
    t= tkinter.simpledialog.askstring('Find', 'Search Enter text:')
    if t:
        idx = '1.0'
    while 1:
        idx = textPad.search(t, idx, nocase=1, stopindex=END)
        if not idx: break
        lastidx = '%s+%dc' % (idx, len(t))
        textPad.tag_add('found', idx, lastidx)
        idx = lastidx
    textPad.tag_config('found', foreground='white', background='red')
   
menuM=Menu(root)
root.configure(menu=menuM)
fileM=Menu(menuM)
menuM.add_cascade(label='File',menu=fileM)
fileM.add_command(label="New",command=newpopup)
fileM.add_command(label="Open...",command=open)
fileM.add_command(label="Save..",command=save)
fileM.add_separator()
fileM.add_command(label="Exit",command=root.destroy)

editM=Menu(menuM)
menuM.add_cascade(label="Edit",menu=editM)
editM.add_command(label="Undo")
editM.add_command(label="delete")
editM.add_separator()
editM.add_command(label="Cut",command=cut,accelerator="Ctrl+C")
editM.add_command(label="Copy",accelerator="Ctrl+D")
editM.add_command(label="Paste",accelerator="Ctrl+P")

menuM.add_cascade(label="Info",command=show)

menuM.add_cascade(label="About",command=hello)

menuM.add_cascade(label="Find",command=find)

textPad.pack()
root.mainloop()
