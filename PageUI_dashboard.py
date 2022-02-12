from tkinter import *
from tkinter import messagebox
import client
import PageUI_newFirstAcc
import PageUI_newAcc
import PageUI_deleteAcc
import PageUI_transfer
import PageUI_transactions
import PageUI_loan

lbx_accounts=""

def makeDashboardUI(parrentWin):
    parrentWin.withdraw()
    win=Tk()
    win.geometry("600x300")
    win.title("dashboard")

    lbl_name=Label(win , text=client.user.name+"\nhere is you accounts")
    lbl_name.place(x=20 , y=20 )

    global lbx_accounts
    lbx_accounts=Listbox(win , width=40)
    lbx_accounts.place(x=20 , y=40)

    client.request_getAccounts(client.user.ncode)
    if(len(client.userAccounts)==0):
        lbl_name.config(text=client.user.name+"\nyou have no account yet")
    else:
        lbx_accounts.delete(0,END)
        for i in range(len(client.userAccounts)):
            lbx_accounts.insert(i,str(i+1)+". "+(client.userAccounts[i].prettyStr()))
        
    
    def click_btn_openacc():
        if(len(client.userAccounts)==0):
            PageUI_newFirstAcc.makeNewFirtAccUI(win)
            return
        else:
            global lbx_accounts
            if (not lbx_accounts.curselection()):
                messagebox.showwarning("no account selected" , "you need to select an account first")
                return
            PageUI_newAcc.makeNewAccUI(win)
            return
        return

    btn_openacc = Button(win , text = "   open new Acount   " , command=click_btn_openacc )
    btn_openacc.place(relx=1 , x=-5 ,y=20 , anchor = NE)

    def click_btn_deleteacc():
        global lbx_accounts
        if (not lbx_accounts.curselection()):
            messagebox.showwarning("no account selected" , "you need to select an account first")
            return
        PageUI_deleteAcc.makeDeleteAccUI(win)
        #res = client.request_deleteAccount(lbx_accounts.get(lbx_accounts.curselection()[0]).split()[1])
        #refreshAccLiat(lbx_accounts)
        return

    btn_deleteacc = Button(win , text = "   delete Acount   " , command=click_btn_deleteacc )
    btn_deleteacc.place(relx=1 , x=-5 ,y=50 , anchor = NE)



    def click_btn_transfer():
        global lbx_accounts
        if (not lbx_accounts.curselection()):
            messagebox.showwarning("no account selected" , "you need to select an account first")
            return
        PageUI_transfer.makeTransferUI(win)
        #res = client.request_deleteAccount(lbx_accounts.get(lbx_accounts.curselection()[0]).split()[1])
        #refreshAccLiat(lbx_accounts)
        return

    btn_transfer = Button(win , text = "   transfer   " , command=click_btn_transfer )
    btn_transfer.place(relx=1 , x=-5 ,y=80 , anchor = NE)


    def click_btn_transactions():
        
        PageUI_transactions.makeTransactionUI(win)
        return

    btn_transaction = Button(win , text = "   transactions   " , command=click_btn_transactions )
    btn_transaction.place(relx=1 , x=-5 ,y=110 , anchor = NE)


    def click_btn_loan():
        
        PageUI_loan.makeLoanUI(win)
        return
    btn_loan = Button(win , text = "   loans   " , command=click_btn_loan)
    btn_loan.place(relx=1 , x=-5 ,y=140 , anchor = NE)



    def click_btn_requestloan():
        if (not lbx_accounts.curselection()):
            messagebox.showwarning("no account selected" , "you need to select an account first")
            return
        ret = client.request_newLoan(client.user.ncode , lbx_accounts.get(lbx_accounts.curselection()[0]).split()[1])
        if(ret.result == "unsuccess"):
            return ret
        refreshAccLiat(lbx_accounts)
        #PageUI_loan.makeLoanUI(win)
        return
    btn_requestloan = Button(win , text = "   request loan   " , command=click_btn_requestloan)
    btn_requestloan.place(relx=1 , x=-5 ,y=170 , anchor = NE)


    def click_btn_refresh():
        global lbx_accounts

        client.request_getAccounts(client.user.ncode)
        if(len(client.userAccounts)==0):
            lbl_name.config(text=client.user.name+"\nyou have no account yet")
        else:
            lbx_accounts.delete(0,END)
            for i in range(len(client.userAccounts)):
                lbx_accounts.insert(i,str(i+1)+". "+(client.userAccounts[i].prettyStr()))
        
        return

    btn_refresh = Button(win , text = "   refresh   " , command=click_btn_refresh )
    btn_refresh.place(x=20 , y=200)

    
    

    def on_closing():
         print("subwindow endded")
         parrentWin.deiconify()
         win.destroy()
        
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()

    return

def refreshAccLiat(lbx_accounts):
        client.request_getAccounts(client.user.ncode)
        lbx_accounts.delete(0,END)
        for i in range(len(client.userAccounts)):
            lbx_accounts.insert(i,str(i+1)+". "+(client.userAccounts[i].prettyStr()))
        
        return