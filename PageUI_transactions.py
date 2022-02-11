from tkinter import *
from tkinter import messagebox
import client
import PageUI_dashboard

def makeTransactionUI(parrentWin):
    parrentWin.withdraw()
    win=Tk()
    win.geometry("400x200")
    win.title("transactions")

    lbx_transactions=Listbox(win , width=40)
    lbx_transactions.place(x=20 , y=40)

    ret = client.request_Transactions(client.user.ncode)
    lbx_transactions.delete(0,END)
    for i in range(len(ret)):
        lbx_transactions.insert(i,str(i+1)+". "+(ret[i].prettyStr()))
    
    def on_closing():
         #print("subwindow endded")
         parrentWin.deiconify()
         win.destroy()
        
    win.protocol("WM_DELETE_WINDOW", on_closing)
    win.mainloop()

    return