from tkinter import *
from tkinter import messagebox
import client
import PageUI_dashboard

def makeNewFirtAccUI(parrentWin):
    parrentWin.withdraw()
    win=Tk()
    win.geometry("400x100")
    win.title("new first account")

    lbl_desc=Label(win , text="select an alias for your new account\nbecause it is your first account, you will get some initial balance")
    lbl_desc.place(x=20 , y=20 )

    lbl_alias=Label(win , text="alias: ")
    lbl_alias.place(x=20 , y=70 )

    alias=StringVar(win)
    te_ncode=Entry(win , textvariable=alias)
    te_ncode.place(x=60 , y=70)

    def click_btn_openacc():
        client.request_openFirstAccount(client.user.ncode , alias.get())
        parrentWin.deiconify()
        win.destroy()
        PageUI_dashboard.refreshAccLiat(PageUI_dashboard.lbx_accounts)
        return

    btn_openacc = Button(win , text = "   open new Acount   " , command=click_btn_openacc )
    btn_openacc.place(x=200 ,y=70)


    def on_closing():
         #print("subwindow endded")
         parrentWin.deiconify()
         win.destroy()
        
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()

    return