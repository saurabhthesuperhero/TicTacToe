#TIC TAC NEW +GUI
from tkinter import *
from tkinter import messagebox
#USER
user='X'
a1,a2,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,0,0,0,0
def check():
    if(a1!=0 or  a2!=0 or a3!=0 or a4!=0 or a5!=0 or a6!=0 or a7!=0 or a9!=0):
        if (a1==a2==a3 and a1!=0 or a1==a4==a7 and a1!=0 or a4==a5==a6 and a4!=0 or  a7==a8==a9 and a7!=0 or a2==a5==a8 and a2!=0 or a3==a5==a6 and a3!=0 or a1==a5==a9 and a1!=0 or a3==a5==a7 and a3!=0):
            return user
        else:
            pass
def clear():
    global user
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    global a9
    
    a1,a2,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,0,0,0,0
    b1text.set('')
    b2text.set('')
    b3text.set('')
    b4text.set('')
    b5text.set('')
    b6text.set('')
    b7text.set('')
    b8text.set('')
    b9text.set('')
    

def click(id):
    global user
    global a1
    global a2
    global a3
    global a4
    global a5
    global a6
    global a7
    global a8
    global a9
    
    if  user=='X':
        user='O'
    elif user=='O':
        user='X'
    if id==1:
        a1=user
        b1text.set(user)
        
    elif id==2:
        a2=user
        b2text.set(user)
    elif(id==3):
        a3=user
        b3text.set(user)
        
    elif id==4:
        a4=user
        b4text.set(user)
        
    elif id==5:
        a5=user
        b5text.set(user)
       
    elif id==6:
        a6=user
        b6text.set(user)
       
    elif id==7:
        a7=user
        b7text.set(user)
       
    elif id==8:
        a8=user
        b8text.set(user)
        
    elif id==9:
        a9=user
        b9text.set(user)
        
    try: 
        winner=check()
        if winner!=None:
            winner=str(winner)+' Is The winner\n'
            #result.insert(END,winner)
            messagebox.showinfo("Winner",winner)
    except TclError:
        pass
window=Tk()
window.geometry('450x500')
l1=Label(text='Tic Tac Toe',anchor=W,fg='white',bg='brown',font=('Times New Roman',20))
l1.grid(row=1,column=1)
window.configure(background='brown')
window.resizable(0, 0)
window.pack_propagate(0)
#textButton
b1text=StringVar()
b2text=StringVar()
b3text=StringVar()
b4text=StringVar()
b5text=StringVar()
b6text=StringVar()
b7text=StringVar()
b8text=StringVar()
b9text=StringVar()
b1=Button(textvariable=b1text,font=('Times',19),bg='purple',fg='white',command=lambda:click(1))
b1.grid(row=3,column=0,sticky=S+N+E+W,ipady=40,ipadx=55)
b2=Button(textvariable=b2text,font=('Times',19),bg='purple',fg='white',command=lambda:click(2))
b2.grid(row=4,column=0,sticky=S+N+E+W,ipady=40,ipadx=55)
b3=Button(textvariable=b3text,font=('Times',19),bg='purple',fg='white',command=lambda:click(3))
b3.grid(row=5,column=0,sticky=S+N+E+W,ipady=40,ipadx=55)
b4=Button(textvariable=b4text,font=('Times',19),bg='purple',fg='white',command=lambda:click(4))
b4.grid(row=3,column=1,sticky=S+N+E+W,ipady=40,ipadx=55)
b5=Button(textvariable=b5text,font=('Times',19),bg='purple',fg='white',command=lambda:click(5))
b5.grid(row=4,column=1,sticky=S+N+E+W,ipady=40,ipadx=55)
b6=Button(textvariable=b6text,font=('Times',19),bg='purple',fg='white',command=lambda:click(6))
b6.grid(row=5,column=1,sticky=S+N+E+W,ipady=40,ipadx=55)
b7=Button(textvariable=b7text,font=('Times',19),bg='purple',fg='white',command=lambda:click(7))
b7.grid(row=3,column=2,sticky=S+N+E+W,ipady=40,ipadx=55)
b8=Button(textvariable=b8text,font=('Times',19),bg='purple',fg='white',command=lambda:click(8))
b8.grid(row=4,column=2,sticky=S+N+E+W,ipady=40,ipadx=55)
b9=Button(textvariable=b9text,font=('Times',19),bg='purple',fg='white',command=lambda:click(9))
b9.grid(row=5,column=2,sticky=S+N+E+W,ipady=40,ipadx=55)
bend=Button(text='Clear',anchor=N,font=('Times',19),bg='purple',fg='white',command=clear)
bend.grid()
l2=Label(text='BySaurabhJadhav',anchor=W,fg='white',bg='brown',font=('Times New Roman',15))
l2.grid(row=6,column=2)

window.mainloop()
