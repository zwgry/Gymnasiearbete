from my_server.databasehandler import create_connection
from flask import session

def is_logged_in():
    if 'logged_in' in session:
        return True
    return False

def sql_to_list(objs):
    return_list = []
    for obj in objs:
        return_list.append(obj.as_dict())
    return return_list