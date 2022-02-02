from cProfile import label
from functools import partial
from textwrap import fill
from tkinter import *

import client


def makeSignUpUI(parrentWin):
    parrentWin.withdraw()
    win=Tk()
    win.geometry("300x300")
    win.title("Sign Up")
    
    #---------------------------------------------------------------name
    lbl_name=Label(win , text="name :")
    lbl_name.place(x=20 , y=20 )

    name=StringVar(win)
    te_name=Entry(win , textvariable=name)
    te_name.place(x=130 , y=20)

    #---------------------------------------------------------------nathional code
    lbl_ncode=Label(win , text="national code :")
    lbl_ncode.place(x=20 , y=50 )

    ncode=StringVar(win)
    te_ncode=Entry(win , textvariable=ncode)
    te_ncode.place(x=130 , y=50)

    #---------------------------------------------------------------password
    lbl_pass1=Label(win , text="password :")
    lbl_pass1.place(x=20 , y=80 )

    pass1=StringVar(win)
    te_pass1=Entry(win , textvariable=pass1)
    te_pass1.place(x=130 , y=80)

    #---------------------------------------------------------------confirm password
    lbl_pass2=Label(win , text="confirm password :")
    lbl_pass2.place(x=20 , y=110 )

    pass2=StringVar(win)
    te_pass2=Entry(win , textvariable=pass2)
    te_pass2.place(x=130 , y=110)

    #---------------------------------------------------------------phone number
    lbl_phone=Label(win , text="phone number :")
    lbl_phone.place(x=20 , y=140 )

    phone=StringVar(win)
    te_phone=Entry(win , textvariable=phone)
    te_phone.place(x=130 , y=140)

    #---------------------------------------------------------------email
    lbl_email=Label(win , text="email address :")
    lbl_email.place(x=20 , y=170 )

    email=StringVar(win)
    te_email=Entry(win , textvariable=email)
    te_email.place(x=130 , y=170)

    #--------------------------------------------------------------- sign up button
    def click_btn_signup():
         #check if password are the same
          if (pass1.get() != pass2.get()):
              lbl_result.config(text="passwords should match")
              return
          res=client.request_signup(name.get(),ncode.get(),pass1.get(),phone.get(),email.get())
          if(res.result=="unsuccess"):
              lbl_result.config(text=res.message)
          return
     
    #click_btn_signup = partial(click_btn_signup,name,ncode,pass1,pass2,phone,email)
    btn_signup = Button(win , text = "Sign Up" , command=click_btn_signup)
    btn_signup.place(relx=0.5 , y=220 , anchor = CENTER)

     #---------------------------------------------------------------result
    lbl_result=Label(win , text="")
    lbl_result.place(x=20 , y=250 )





    def on_closing():
         print("subwindow endded")
         parrentWin.deiconify()
         win.destroy()
        
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()
    return


