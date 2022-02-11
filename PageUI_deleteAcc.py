from tkinter import *
from tkinter import messagebox
import client
import PageUI_dashboard

def makeDeleteAccUI(parrentWin):
    parrentWin.withdraw()
    win=Tk()
    win.geometry("400x200")
    win.title("delete account")

    lbl_target=Label(win , text="select a target account")
    lbl_target.place(x=20 , y=20 )

    target=StringVar(win)
    te_ncode=Entry(win , textvariable=target)
    te_ncode.place(x=60 , y=70)

    def click_btn_deleteacc():
        try:
            PageUI_dashboard.lbx_accounts.curselection()[0]
        except:
            messagebox.showwarning("no account selected" , "you need to select an account first")
            parrentWin.deiconify()
            win.destroy()
            return
        print(PageUI_dashboard.lbx_accounts.get(PageUI_dashboard.lbx_accounts.curselection()[0]))
        deleteAcc=PageUI_dashboard.lbx_accounts.get(PageUI_dashboard.lbx_accounts.curselection()[0]).split()[1]
        targetAcc=target.get()
        if(targetAcc == deleteAcc):
            messagebox.showwarning("same acc" , "you need to select deifferent account as target")
            return

        ret = client.request_deleteAccount(deleteAcc , targetAcc)
        if(ret.result == "unsuccess"):
            messagebox.showwarning(ret.result , ret.message)
        else:
            parrentWin.deiconify()
            win.destroy()
            PageUI_dashboard.refreshAccLiat(PageUI_dashboard.lbx_accounts)


       
        return

    btn_deleteacc = Button(win , text = "   delete Acount   " , command=click_btn_deleteacc )
    btn_deleteacc.place(x=200 ,y=120)


    def on_closing():
         #print("subwindow endded")
         parrentWin.deiconify()
         win.destroy()
        
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()

    return