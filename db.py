import sqlite3 as driver
from pydantic import BaseModel

DATABASE_URL = 'db/database.db'

class User (BaseModel):

    id: int
    username: str
    password: str

def get_last_id(list_of_id):

    return list_of_id[-1].id

def create_tables():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS USERS (ID INT, USERNAME TEXT, PASSWORD TEXT)")

def clear_tables():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor(DATABASE_URL)
    cursor.execute("DELETE FROM USERS")
    database.commit

def get_users():

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor(DATABASE_URL)
    cursor.execute('SELECT * FROM USERS')
    users = cursor.fetchall()
    database.commit()
    userForm = []

    for user in users:

        userForm.append(User(id = user[0], username = user[1], password = user[2]))

    return userForm

def add_user(username, password):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor(DATABASE_URL)
    cursor.execute(f"INSERT INTO USERS (ID, Username, Password) VALUES ('{get_last_id(get_users()+1)}', '{username}', '{password}')")
    database.commit()

def remove_user(id):

    database = driver.connect(DATABASE_URL)
    cursor = database.cursor(DATABASE_URL)
    cursor.execute(f"DELETE FROM QUESTIOSN WHERE ID = '{id}'")