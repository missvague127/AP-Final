from tkinter import *

mainWindow= Tk()
mainWindow.title("client")
mainWindow.geometry('600x400')

#username label and username entry box
usernameLabel = Label(mainWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(mainWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(mainWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(mainWindow, textvariable=password, show='*').grid(row=1, column=1)  

def validateLogin():
    ## make a select query and call database function
    mainWindow.withdraw()
    dashboard=Tk()
    def on_closing():
        print("subwindow endded")
        mainWindow.deiconify()
        dashboard.destroy()
        
    dashboard.protocol("WM_DELETE_WINDOW", on_closing)
    dashboard.mainloop()
    
    pass

#login button
loginButton = Button(mainWindow, text="Login", command=validateLogin).grid(row=1, column=2)  

signUpLabel = Label(mainWindow, text="or you can sign up").grid(row=2, column=0)


def signNewUser():
    ## make a insert query and call database function
    pass
signUpButton = Button(mainWindow, text="Sign up", command=signNewUser).grid(row=3, column=0)

mainWindow.mainloop()