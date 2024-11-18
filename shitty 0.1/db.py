import sqlite3

def create_database():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_inventory(
        user TEXT NOT NULL UNIQUE,
        score INTEGER NOT NULL
    """)



def save_player_data():
    conn=sqlite3.connect("database.db") 
    cursor= conn.cursor()
    cursor.execute("""FROM user_data""")
    data=cursor.fetchall()

