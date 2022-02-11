from tkinter import *
from tkinter import messagebox
import client
import PageUI_dashboard

def makeTransferUI(parrentWin):
    parrentWin.withdraw()
    win=Tk()
    win.geometry("400x200")
    win.title("delete account")

    lbl_target=Label(win , text="select a target account")
    lbl_target.place(x=20 , y=20 )

    lbl_amount=Label(win , text="amount: ")
    lbl_amount.place(x=20 , y=50 )

    amount=StringVar(win)
    te_amount=Entry(win , textvariable=amount)
    te_amount.place(x=80 , y=50)


    lbl_target=Label(win , text="target: ")
    lbl_target.place(x=20 , y=80 )

    target=StringVar(win)
    te_target=Entry(win , textvariable=target)
    te_target.place(x=80 , y=80)

    def click_btn_transfer():
        try:
            PageUI_dashboard.lbx_accounts.curselection()[0]
        except:
            messagebox.showwarning("no account selected" , "you need to select an account first")
            parrentWin.deiconify()
            win.destroy()
            return
        print(PageUI_dashboard.lbx_accounts.get(PageUI_dashboard.lbx_accounts.curselection()[0]))
        fromAcc=PageUI_dashboard.lbx_accounts.get(PageUI_dashboard.lbx_accounts.curselection()[0]).split()[1]
        targetAcc=target.get()
        if(targetAcc == fromAcc):
            messagebox.showwarning("same acc" , "you need to select deifferent account as target")
            return

        ret = client.request_Transfer(fromAcc , targetAcc , amount.get())
        if(ret.result == "unsuccess"):
            messagebox.showwarning(ret.result , ret.message)
        else:
            PageUI_dashboard.refreshAccLiat(PageUI_dashboard.lbx_accounts)
            parrentWin.deiconify()
            win.destroy()
            
       
        return

    btn_transfer = Button(win , text = "   transfer by account number   " , command=click_btn_transfer )
    btn_transfer.place(x=220 ,y=80)



    lbl_targetalias=Label(win , text="alias: ")
    lbl_targetalias.place(x=20 , y=110 )

    targetalias=StringVar(win)
    te_targetalias=Entry(win , textvariable=targetalias)
    te_targetalias.place(x=80 , y=110)

    def click_btn_transferalias():
        try:
            PageUI_dashboard.lbx_accounts.curselection()[0]
        except:
            messagebox.showwarning("no account selected" , "you need to select an account first")
            parrentWin.deiconify()
            win.destroy()
            return
        print(PageUI_dashboard.lbx_accounts.get(PageUI_dashboard.lbx_accounts.curselection()[0]))
        fromAcc=PageUI_dashboard.lbx_accounts.get(PageUI_dashboard.lbx_accounts.curselection()[0]).split()[1]
        alias=targetalias.get()

        ret = client.request_TransferByAlias(fromAcc , alias , amount.get())
        if(ret.result == "unsuccess"):
            messagebox.showwarning(ret.result , ret.message)
        else:
            PageUI_dashboard.refreshAccLiat(PageUI_dashboard.lbx_accounts)
            parrentWin.deiconify()
            win.destroy()
            
       
        return

    btn_transferalias = Button(win , text = "   transfer by alias   " , command=click_btn_transferalias )
    btn_transferalias.place(x=220 ,y=110)



    def on_closing():
         #print("subwindow endded")
         parrentWin.deiconify()
         win.destroy()
        
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()

    return