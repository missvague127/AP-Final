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
