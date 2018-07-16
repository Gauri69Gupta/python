from tkinter import *
root=Tk()
root.title("Gauri")
def fun():
    k=nameE.get()
    v=mobE.get()
    dict[k]=v
    #lbl.configure(scrollbar=k)
    #lbl2.configure(text=v)
nameL=Label(root,text='User name:')
nameL.grid(row=0,column=0)
mobL=Label(root,text="Mobile_No:")
mobL.grid(row=1,column=0)
nameE=Entry(root)
nameE.grid(row=0,column=1)
mobE=Entry(root)
mobE.grid(row=1,column=1)
addB=Button(root,text="Add It",bg='red',command=fun)
addB.grid(row=2,column=1)
lbl=Scrollbar(root)
lbl.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=fun)
for line in range(10):
 mylist.insert(END,k)
mylist.pack(side=LEFT,fill=BOTH)
lbl.config(command=mylist.yview)

root.mainloop()
