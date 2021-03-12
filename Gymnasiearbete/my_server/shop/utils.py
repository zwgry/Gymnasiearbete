from my_server.databasehandler import create_connection

def is_logged_in():
    if 'logged_in' in session:
        return True
    return False
