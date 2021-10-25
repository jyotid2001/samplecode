from tkinter import *
root=Tk()
def add():
    t3.delete(0,END)
    n1=int(t1.get())
    n2=int(t2.get())
    t3.insert(0,n1+n2)

l1=Label(root,text="calculator").grid(row=1,column=5)
l2=Label(root,text="firstno").grid(row=2,column=2)
l3=Label(root,text="secondno").grid(row=3,column=3)

l4=Label(root,text="result").grid(row=4,column=3)

t1=Entry()
t2=Entry()
t3=Entry()

t1.grid(row=2,column=5)
t2.grid(row=3,column=5)
t3.grid(row=4,column=5)

b1 = Button(root,text='add',command=add).grid(row=6,column=3)
b2 = Button(root,text='quit',command=root.destory).grid(row=6,column=4)
root.mainloop()


