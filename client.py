from calendar import day_abbr
from hmac import trans_36
import random
import threading
import PageUI_login
import database
import time

user=""
userAccounts=""
userLoans=""
#this method is called inside ui
def request_login(username , password):
    # create a select query and ask database
    query = "SELECT FROM users WHERE (ncode==\"{uname}\" AND pass==\"{upass}\")"
    query = query.format(uname = username , upass=password)
    res = database.handleQuery(query)
    if(res.result == "success"):
        global user
        user = res.entries[0]
    #print(query)
    return res


def request_signup(name, ncode, _pass, phone, email):
    query = "INSERT INTO users VALUES ({uname},{uncode},{upass},{uphone},{uemail},{utime});"
    query = query.format(uname = name , uncode=ncode , upass=_pass , uphone=phone, uemail=email , utime=time.time())
    res=database.handleQuery(query)

    k=9
    return res

def request_getAccounts(ncode):
    query = "SELECT FROM accounts WHERE (ownerNcode==\"{ncode}\")"
    query = query.format(ncode = ncode)
    res = database.handleQuery(query)
    global userAccounts
    userAccounts = res.entries
    return res

def request_openFirstAccount(ncode , alias):
    query = "INSERT INTO accounts VALUES ({accnumber},{uncode},{balance},{alias1},{fav},{utime});"
    rand=random.SystemRandom()
    query = query.format(accnumber = rand.randint(10000000, 99999999) , uncode=ncode , balance=rand.randint(50, 100) , alias1=alias ,fav='False' , utime=time.time())
    res = database.handleQuery(query)
    if(res.result == "success"):
        ret=request_getAccounts(ncode)
        global userAccounts
        userAccounts = ret.entries
        return ret
    else:
        return res

def request_addMoreAccount(ncode , alias, AccNumber, initBalance):
    #print(ncode , alias , AccNumber , initBalance)
    if(int(initBalance) > int(AccNumber.split()[3])):
        return database.Response("unsuccess" , "initial balance should be less than host acount balance" , [])
    else:
        query = "INSERT INTO accounts VALUES ({accnumber},{uncode},{balance},{alias1},{fav},{utime});"
        rand=random.SystemRandom()
        newAccNumber=rand.randint(10000000, 99999999)
        query = query.format(accnumber =newAccNumber  , uncode=ncode , balance=0 , alias1=alias ,fav='False' , utime=time.time())
        res = database.handleQuery(query)
        if(res.result == "success"):
            ret=request_getAccounts(ncode)
            global userAccounts
            userAccounts = ret.entries
            #update old acount
            #create new account

        res =request_Transfer(AccNumber.split()[1] , newAccNumber, initBalance)
        if(res.result == "success"):
            ret=request_getAccounts(ncode)
            return ret

    return

def request_deleteAccount(AccNumber ,targetAccNumber):
    
    query = "SELECT FROM accounts WHERE (accnumber==\"{accnumber}\")"
    query = query.format(accnumber = AccNumber)
    res = database.handleQuery(query)

    if (res.result=="unsuccess"):
        return res

    deleteAcc=res.entries[0]

    query2 = "SELECT FROM accounts WHERE (accnumber==\"{accnumber}\")"
    query2 = query2.format(accnumber = targetAccNumber)
    res2 = database.handleQuery(query2)

    if (res2.result=="unsuccess"):
        res2.message="target account not found"
        return res2

    targetAcc=res2.entries[0]


    res3 = request_Transfer(AccNumber , targetAccNumber , deleteAcc.balance)
    if (res3.result=="unsuccess"):
        res3.message="transfer unsuccessful, try again later"
        return res3
    
    query = "DELETE FROM accounts WHERE (accnumber==\"{accnumber}\")"
    query = query.format(accnumber = AccNumber)
    res = database.handleQuery(query)
    if (res.result=="success"):
        global userAccounts
        userAccounts=res.entries
    return res

def request_updateAccount(AccNumber):
    query = "UPDATE accounts WHERE (accnumber==\"{accnumber}\") VALUES a,b,c,d,e,f"
    query = query.format(accnumber = AccNumber)
    res = database.handleQuery(query)
    if (res.result=="success"):
        global userAccounts
        userAccounts=res.entries
    return res


def request_Transfer(accFrom , accTo , amount):
    query1 = "SELECT FROM accounts WHERE (accnumber==\"{accfrom}\")"
    query1 = query1.format(accfrom = accFrom)
    res1 = database.handleQuery(query1)

    if(res1.result == "unsuccess"):
        return res1
    if(len(res1.entries) == 0 or int(res1.entries[0].balance) < int(amount)):
        res1.message="not enough money in host acc"
        return res1
    
    accountFrom = res1.entries[0]

    
    query2 = "SELECT FROM accounts WHERE (accnumber==\"{accto}\")"
    query2 = query2.format(accto = accTo)
    res2 = database.handleQuery(query2)
    if(res2.result == "unsuccess"):
        return res2

    accountTo = res2.entries[0]

    if(accountFrom.accnumber == accountTo.accnumber):
        res2.message="you cant trasfer to same account, selcet another account"
        res2.result="unsuccess"
        return res2


    query3 = "UPDATE accounts WHERE (accnumber==\"{accfrom}\") VALUES {v1},{v2},{v3},{v4},{v5},{v6}"
    query3 = query3.format(accfrom = accFrom ,v1 = accountFrom.accnumber , v2 = accountFrom.ownerNcode,v3 = int(accountFrom.balance) - int(amount),v4 = accountFrom.alias,v5 = accountFrom.fav,v6 = accountFrom.createTime)
    res3 = database.handleQuery(query3)
    if(res3.result == "unsuccess"):
        return res3


    query4 = "UPDATE accounts WHERE (accnumber==\"{accto}\") VALUES {v1},{v2},{v3},{v4},{v5},{v6}"
    query4 = query4.format(accto = accTo,v1 = accountTo.accnumber , v2 = accountTo.ownerNcode,v3 = int(accountTo.balance) + int(amount),v4 = accountTo.alias,v5 = accountTo.fav,v6 = accountTo.createTime)
    res3 = database.handleQuery(query4)
    if(res3.result == "unsuccess"):
        return res3


    query5 = "INSERT INTO transaction VALUES ({v1},{v2},{v3},{v4},{v5});"
    rand=random.SystemRandom()
    newAccNumber=rand.randint(10000000, 99999999)
    query5 = query5.format(v1 =accFrom  , v2=accTo , v3=amount , v4=time.time() ,v5='Description')
    res5 = database.handleQuery(query5)
    if(res5.result == "unsuccess"):
        return res5

    return res5

def request_TransferByAlias(accFrom , alias , amount):
    query1 = "SELECT FROM accounts WHERE (alias==\"{a}\")"
    query1 = query1.format(a = alias)
    res1 = database.handleQuery(query1)

    if(res1.result == "unsuccess"):
        res1.message="no target account found"
        return res1
    
    accountTo = res1.entries[0]
    return request_Transfer(accFrom , accountTo.accnumber , amount)


def request_Transactions(ncode):
    accounts = request_getAccounts(ncode).entries

    transactions=[]

    
    for i in range(len(accounts)):
        query1 = "SELECT FROM transaction WHERE (accfrom==\"{v1}\" OR accto==\"{v2}\")"
        query1 = query1.format(v1 = accounts[i].accnumber , v2=accounts[i].accnumber)
        res1 = database.handleQuery(query1)
        for j in range(len(res1.entries)):
            transactions.append(res1.entries[j])

    return transactions
        
def request_getLoans(ncode):
    query = "SELECT FROM loan WHERE (ncode==\"{ncode}\")"
    query = query.format(ncode = ncode)
    res = database.handleQuery(query)
    global userLoans
    userLoans = res.entries
    return res

def request_newLoan(ncode , accNumber):

    query1 = "SELECT FROM accounts WHERE (accnumber==\"{accfrom}\")"
    query1 = query1.format(accfrom = accNumber)
    res1 = database.handleQuery(query1)

    if(res1.result == "unsuccess"):
        return res1

    targetAcc= res1.entries[0]

    query4 = "UPDATE accounts WHERE (accnumber==\"{accto}\") VALUES {v1},{v2},{v3},{v4},{v5},{v6}"
    query4 = query4.format(accto = targetAcc.accnumber ,v1 = targetAcc.accnumber , v2 = targetAcc.ownerNcode,v3 = int(targetAcc.balance) + 240 ,v4 = targetAcc.alias,v5 = targetAcc.fav,v6 = targetAcc.createTime)
    res3 = database.handleQuery(query4)
    if(res3.result == "unsuccess"):
        return res3

    query = "INSERT INTO loan VALUES ({uncode},{number},{accnumber},{amount},{remain});"
    rand=random.SystemRandom()
    r=rand.randint(10000000, 99999999)
    query = query.format(uncode=ncode , number=r , accnumber=accNumber ,amount=240 , remain=240)
    res = database.handleQuery(query)
    if(res.result == "unsuccess"):
        return res

    
    newThread = threading.Thread(target=threadFunction , args = (targetAcc.accnumber , r))
    newThread.start()

    return res


def threadFunction (accnumber , loanNumber):
    remain=1
    while (remain > 0):
        time.sleep(3)
        #1. select loan
        query2 = "SELECT FROM loan WHERE (number==\"{num}\")"
        query2 = query2.format(num = loanNumber)
        res2 = database.handleQuery(query2)
        if(res2.result == "unsuccess"):
            return res2

        thisLoan=res2.entries[0]

        if(int(thisLoan.remain) > 0):
            query1 = "SELECT FROM accounts WHERE (accnumber==\"{num}\")"
            query1 = query1.format(num = accnumber)
            res1 = database.handleQuery(query1)

            if(res1.result == "unsuccess"):
                return res1

            targetAcc= res1.entries[0]

            query4 = "UPDATE accounts WHERE (accnumber==\"{num}\") VALUES {v1},{v2},{v3},{v4},{v5},{v6}"
            query4 = query4.format(num = accnumber ,v1 = targetAcc.accnumber , v2 = targetAcc.ownerNcode,v3 = int(targetAcc.balance) - 20,v4 = targetAcc.alias,v5 = targetAcc.fav,v6 = targetAcc.createTime)
            res3 = database.handleQuery(query4)
            if(res3.result == "unsuccess"):
                return res3

            query5 = "UPDATE loan WHERE (number==\"{num}\") VALUES {v1},{v2},{v3},{v4},{v5}"
            query5 = query5.format(num = thisLoan.number ,v1 = thisLoan.ncode , v2 = thisLoan.number, v3 = thisLoan.accnumber ,v4 = thisLoan.amount,v5 = int(thisLoan.remain) - 20 )
            res5 = database.handleQuery(query5)
            if(res5.result == "unsuccess"):
                return res5

            

            remain=int(thisLoan.remain) - 20




    return 



    
#request_Transfer(30713454 , 30713453 , 10)