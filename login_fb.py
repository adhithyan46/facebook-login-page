from tkinter import *
# import tkinter as tk
def login():
    uname=uname_t.get('0.1',END).strip()
    pword=pword_t.get('0.1',END).strip()
    if uname=='admin'and pword=='admin':
        root2=Tk()
        root2.title('feed')
        root2.geometry('1000x700')
    else:
        msg=Label(frame1,bg='white',fg='red',text='Check your Username or Password')
        msg.place(x=110,y=225)
root =Tk()
root.title('Facebook log in')
root.geometry('1000x600')
frame1=Frame(root,width=400,height=350,border=1,bg='white',relief='flat')
frame1.place(x=750,y=150)
uname_t=Text(frame1,width=52,height=2,relief='flat',bg='gray90',font=('Helvetica',10,'normal'))
uname_t.place(x=12,y=30)
username=Label(frame1,text='username',fg="gray40",bg='white')
username.place(x=12,y=7)
pword_t=Text(frame1,width=52,height=2,relief='flat',bg='gray90',font=('Helvetica',10,'normal'))
pword_t.place(x=12,y=99)
password=Label(frame1,text='password',bg='white',fg='gray40')
password.place(x=12,y=75)
log_btn=Button(frame1,text='Login',bg='royalblue',fg='white',font=('Helvetica',13,'bold'),width=36,height=2,relief='flat',command=login)
log_btn.place(x=13,y=155)
fg_btn=Label(frame1,text='Forgot Password?',bg='white',fg='royalblue',font=('courierNew',12,'normal'),relief='flat',)
fg_btn.place(x=140,y=250)
frame2=Frame(root,width=400,height=100,bg='white',relief='flat')
frame2.place(x=750,y=505)
creat_btn=Button(frame2,width=20,height=2,text='Create new account',font=('Helvetica',13,'bold'),bg='limegreen',fg='white',relief='flat')
creat_btn.place(x=100,y=25)
fb=Label(root,text='facebook',font=('arial',50,'bold'),fg='royalblue')
fb.place(x=150,y=200)
stmt=Label(root,text=f'Connect with friends and the world \naround you on Facebook',font=('arial',20,),justify='left')
stmt.place(x=150,y=270)
root.mainloop()