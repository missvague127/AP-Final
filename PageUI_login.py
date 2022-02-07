from cgitb import text
from functools import partial
from tkinter import *
import client
import PageUI_signup
import PageUI_dashboard

def makeLoginUI():
    mainWindow= Tk()
    mainWindow.title("client")
    mainWindow.geometry('300x300')

    #---------------------------------------------------------------nathional code  
    lbl_ncode = Label(mainWindow, text="national code: ")
    lbl_ncode.place(x=20 , y=20 )

    ncode=StringVar(mainWindow)
    te_ncode=Entry(mainWindow , textvariable=ncode)
    te_ncode.place(x=130 , y=20)
    
    #---------------------------------------------------------------password
    lbl_pass=Label(mainWindow , text="password :")
    lbl_pass.place(x=20 , y=50 )

    pass1=StringVar(mainWindow)
    te_pass=Entry(mainWindow , textvariable=pass1)
    te_pass.place(x=130 , y=50)

    #--------------------------------------------------------------- sign in button
    def click_btn_login():
        lbl_result.config(text="")
        #check if fields are not empty
        if(ncode.get()=="" or pass1.get()==""):
            lbl_result.config(text="fields cant be empty!!")
            return   
        res = client.request_login(ncode.get() , pass1.get())
        if(res.result=="success"):
            #open dashboard UI
            PageUI_dashboard.makeDashboardUI(mainWindow)
            pass
        else:
            lbl_result.config(text="login was not successfull!!")
        return

    btn_signin = Button(mainWindow, text="Login", command=click_btn_login)
    btn_signin.place(relx=0.5 , y=100 , anchor = CENTER)


    #---------------------------------------------------------------result
    lbl_result=Label(mainWindow , text="")
    lbl_result.place(relx=0.5 , y=140 , anchor = CENTER)


    #--------------------------------------------------------------- sign up
    lbl_signUp = Label(mainWindow, text="or you can sign up")
    lbl_signUp.place(relx=0.5 , y=170 , anchor = CENTER)

    def click_btn_signup():
        ## make a insert query and call database function
        PageUI_signup.makeSignUpUI(mainWindow)
        return
    #signNewUser = partial(signNewUser , mainWindow)
    btn_signup = Button(mainWindow, text="Sign up", command=click_btn_signup)
    btn_signup.place(relx=0.5 , y=200 , anchor = CENTER)

    mainWindow.mainloop()

    return

makeLoginUI()