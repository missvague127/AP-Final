import PageUI_login
import database

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
    return




