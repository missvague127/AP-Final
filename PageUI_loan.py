from tkinter import *
from tkinter import messagebox
import client
import PageUI_dashboard

def makeLoanUI(parrentWin):
    parrentWin.withdraw()
    win=Tk()
    win.geometry("400x200")
    win.title("loan")

    lbx_loans=Listbox(win , width=40)
    lbx_loans.place(x=20 , y=40)

    client.request_getLoans(client.user.ncode)
    if(len(client.userLoans)==0):
        #lbl_name.config(text=client.user.name+"\nyou have no account yet")
        pass
    else:
        lbx_loans.delete(0,END)
        for i in range(len(client.userLoans)):
            lbx_loans.insert(i,str(i+1)+". "+(str(client.userLoans[i])))

        

    def on_closing():
         #print("subwindow endded")
         parrentWin.deiconify()
         win.destroy()
        
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()

    return