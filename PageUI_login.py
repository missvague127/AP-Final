from functools import partial
from tkinter import *
import client
import PageUI_signup

def makeLoginUI():
    mainWindow= Tk()
    mainWindow.title("client")
    mainWindow.geometry('600x400')

    #username label and username entry box
    usernameLabel = Label(mainWindow, text="User Name").grid(row=0, column=0)
    musername = StringVar()
    usernameEntry = Entry(mainWindow, textvariable=musername).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(mainWindow,text="Password").grid(row=1, column=0)  
    mpassword = StringVar()
    passwordEntry = Entry(mainWindow, textvariable=mpassword, show='*').grid(row=1, column=1)  

    def validateLogin(u ,p):
        
        client.request_login(u.get() , p.get())
        return

    #login button
    validateLogin = partial(validateLogin , musername , mpassword)
    loginButton = Button(mainWindow, text="Login", command=validateLogin).grid(row=1, column=2)  

    signUpLabel = Label(mainWindow, text="or you can sign up").grid(row=2, column=0)


    def signNewUser(m):
        ## make a insert query and call database function
        PageUI_signup.makeSignUpUI(m)
        return
    signNewUser = partial(signNewUser , mainWindow)
    signUpButton = Button(mainWindow, text="Sign up", command=signNewUser).grid(row=3, column=0)

    mainWindow.mainloop()

    return

makeLoginUI()