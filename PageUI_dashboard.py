from tkinter import *
import client

def makeDashboardUI(parrentWin):
    parrentWin.withdraw()
    win=Tk()
    win.geometry("600x300")
    win.title("dashboard")

    lbl_name=Label(win , text=client.user.name+"\nhere is you accounts")
    lbl_name.place(x=20 , y=20 )

    myAccs=client.request_getAccounts(client.user.ncode)
    if(len(myAccs.entries)==0):
        lbl_name.config(text=client.user.name+"\nyou have no account yet")
    else:
        lbx_accounts=Listbox(win , width=30)
        for i in range(len(myAccs.entries)):
            lbx_accounts.insert(i,(myAccs.entries[i]))
        lbx_accounts.place(x=20 , y=40)
        #ts=""
        #for e in myAccs.entries:
            #ts=ts+str(e)+"\n"
        #lbl_name.config(text=client.user.name+"\n"+ts)

    
    def click_btn_openacc():
        myAccs=client.request_openAccount(client.user.ncode)
        if(len(myAccs.entries)==0):
            lbl_name.config(text=client.user.name+"\nyou have no account yet")
        else:
            ts=""
            for e in myAccs.entries:
                ts=ts+str(e)+"\n"
            lbl_name.config(text=client.user.name+"\n"+ts)
        return

    btn_openacc = Button(win , text = "   open new Acount   " , command=click_btn_openacc )
    btn_openacc.place(relx=1 , x=-5 ,y=20 , anchor = NE)


    

    def on_closing():
         print("subwindow endded")
         parrentWin.deiconify()
         win.destroy()
        
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()

    return