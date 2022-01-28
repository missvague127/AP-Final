from tkinter import *
import client


def makeSignUpUI(mainWin):
    mainWin.withdraw()
    dashboard=Tk()
    dashboard.geometry("400x400")
    def on_closing():
         print("subwindow endded")
         mainWin.deiconify()
         dashboard.destroy()
        
    dashboard.protocol("WM_DELETE_WINDOW", on_closing)
    dashboard.mainloop()
    return
