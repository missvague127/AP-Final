from tkinter import *
from tkinter import messagebox
import client
import PageUI_dashboard

def makeNewAccUI(parrentWin):
    parrentWin.withdraw()
    win=Tk()
    win.geometry("400x200")
    win.title("new account")

    lbl_desc=Label(win , text="select an alias for your new account\nbecause it is your first account, you will get some initial balance")
    lbl_desc.place(x=20 , y=20 )

    lbl_alias=Label(win , text="alias: ")
    lbl_alias.place(x=20 , y=70 )

    alias=StringVar(win)
    te_ncode=Entry(win , textvariable=alias)
    te_ncode.place(x=60 , y=70)

    lbl_initBalance=Label(win , text="init balance: ")
    lbl_initBalance.place(x=20 , y=100 )

    initBalance=StringVar(win)
    te_initBalance=Entry(win , textvariable=initBalance)
    te_initBalance.place(x=60 , y=100)

    def click_btn_openacc():
        try:
            PageUI_dashboard.lbx_accounts.curselection()[0]
        except:
            messagebox.showwarning("no account selected" , "you need to select an account first")
            parrentWin.deiconify()
            win.destroy()
            return
        ret = client.request_addMoreAccount(client.user.ncode , alias.get() , PageUI_dashboard.lbx_accounts.get(PageUI_dashboard.lbx_accounts.curselection()[0]) , initBalance.get())
        if(ret.result == "unsuccess"):
            messagebox.showwarning(ret.result , ret.message)
        else:
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