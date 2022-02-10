from calendar import day_abbr
import random
import PageUI_login
import database
import time

user=""
userAccounts=""
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
        pass
        #update old acount
        #create new account

    return

def request_deleteAccount(AccNumber):
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
    if(len(res1.entries) == 0 or int(res1.entries[0].balance) <= int(amount)):
        res1.message="not enough money in host acc"
        return res1
    
    accountFrom = res1.entries[0]

    
    query2 = "SELECT FROM accounts WHERE (accnumber==\"{accto}\")"
    query2 = query2.format(accto = accTo)
    res2 = database.handleQuery(query2)
    if(res2.result == "unsuccess"):
        return res2

    accountTo = res1.entries[0]


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

    return







    

request_Transfer(30713458 , 30713451 , 10)