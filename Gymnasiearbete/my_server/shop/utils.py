from my_server.databasehandler import create_connection

#utför en sql request och hämtar samtliga resultat, inte skyddad från sql-injektioner!!! ska inte användas av användare
# sql == sql query
def sql_request(sql):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result

# utför en sql request och hämtar samtliga resultat, skyddad från sql-injektioner, kan använads av användare
# sql == sql query
# data = data som ska sökas efter (prepared statment)
def sql_request_prepared(sql,data):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql,data)
    conn.commit()
    result = cur.fetchall()
    conn.close()
    return result