import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="fletapp",
        auth_plugin="mysql_native_password"   # force plugin
    )
    return conn