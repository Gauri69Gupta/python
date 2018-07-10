print("Question--1")
from tkinter import *
root=Tk()
root.title("Gauri")
root.configure(background='blue')
frame_1=Frame(root,bg='green')
labelL=Label(frame_1,text="HELLO WORLD",bg='red')
frame_1.pack(fill=X)
labelL.pack()
frame_2=Frame(root,bg='blue')
exitB=Button(frame_2,text='exit',width=50,height=2,bg='yellow',command=root.destroy)
frame_2.pack(side="bottom")
exitB.pack()
root.mainloop()
print('\n')
print("Question--2")
from tkinter import *
root=Tk()
root.title("Gauri")
root.configure(background='blue')
frame_1=Frame(root,bg='green')
labelL=Label(frame_1,text="HELLO WORLD",bg='red')
frame_1.pack(fill=X)
labelL.pack()
def messageP():
   print("Have a nice day")
frame_3=Frame(root,bg="green")
actionB=Button(frame_3,text="Click Me",bg='red',command=messageP)
frame_3.pack(side=RIGHT)
actionB.pack()
frame_2=Frame(root,bg='brown')
exitB=Button(frame_2,text='exit',bg='yellow',command=root.destroy)
frame_2.pack(fill=X,side=BOTTOM)
exitB.pack()
root.mainloop()
print('\n')
print("Question--3")
from tkinter import *
import sys
root=Tk()
root.title("Gauri")
root.configure(background='brown')
frame_1=Frame(root,width=50,bg='green')
labelL=Label(frame_1,text="HELLO WORLD",bg='red')
frame_1.pack(fill=X,side=TOP)
labelL.pack(side=TOP)
def display():
    global labelL
    labelL.config(text="Text Changed..")
    
frame_2=Frame(root,bg='blue')
buttonB=Button(frame_2,text='text changed',width=50,height=2,bg='yellow',command=display)
frame_2.pack(side="left")
buttonB.pack()
frame_3=Frame(root,bg='white')
buttonB2=Button(frame_3,text='SEcond',width=50,height=2,bg='red',command=root.destroy)
frame_3.pack(side="right")
buttonB2.pack()
root.mainloop()

print('\n')
print("Question--4")
from tkinter import *

def show_entry():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

root= Tk()
Label(root, text="First Name").grid(row=0)
Label(root, text="Last Name").grid(row=1)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(root, text='Quit', command=root.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(root, text='Show', command=show_entry).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )


