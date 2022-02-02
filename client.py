from calendar import day_abbr
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

