from calendar import day_abbr
import random
import PageUI_login
import database
import time

user=""
#this method is called inside ui
def request_login(username , password):
    # create a select query and ask database
    query = "SELECT FROM users WHERE (ncode==\"{uname}\" AND pass==\"{upass}\")"
    query = query.format(uname = username , upass=password)
    res = database.handleQuery(query)
    if(res.result == "success"):
        global user
        user = res.entries[0]
    print(query)
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
    return res

def request_openAccount(ncode):
    query = "INSERT INTO accounts VALUES ({accnumber},{uncode},{balance},{utime});"
    rand=random.SystemRandom()
    query = query.format(accnumber = rand.randint(10000000, 99999999) , uncode=ncode , balance=rand.randint(50, 100) , utime=time.time())
    res = database.handleQuery(query)
    if(res.result == "success"):
        return request_getAccounts(ncode)
    else:
        return res

