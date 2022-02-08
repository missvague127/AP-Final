from tkinter import *
from tkinter import messagebox
import client
import PageUI_newFirstAcc
import PageUI_newAcc

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
        
        #ts=""
        #for e in myAccs.entries:
            #ts=ts+str(e)+"\n"
        #lbl_name.config(text=client.user.name+"\n"+ts)

    
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
        res = client.request_deleteAccount(lbx_accounts.get(lbx_accounts.curselection()[0]).split()[1])
        refreshAccLiat(lbx_accounts)
        return

    btn_deleteacc = Button(win , text = "   delete Acount   " , command=click_btn_deleteacc )
    btn_deleteacc.place(relx=1 , x=-5 ,y=50 , anchor = NE)

    
    

    def on_closing():
         print("subwindow endded")
         parrentWin.deiconify()
         win.destroy()
        
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()

    return

def refreshAccLiat(lbx_accounts):
        lbx_accounts.delete(0,END)
        for i in range(len(client.userAccounts)):
            lbx_accounts.insert(i,str(i+1)+". "+(client.userAccounts[i].prettyStr()))
        
        return