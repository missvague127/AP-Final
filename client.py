import PageUI_login
import database


def request_login(username , password):
    # create a select query and ask database
    query = "SELECT FROM users WHERE username==\"{uname}\" AND password==\"{upass}\""
    query = query.format(uname = username , upass=password)

    print(query)
    return