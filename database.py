import sqlite3
from User import Opinion, User
from Friend import Friend

#------------------THIS IS TO CREATE THE TABLES -----------------------

#Create 3 Tables

#c.execute("""CREATE TABLE users (
#        password text
#    )""")

    
#c.execute("""CREATE TABLE opinions (
#        User_id INTEGER,
#        category text,
#        item text,
#        rating INTEGER
#    )""")
#conn = sqlite3.connect('socialnetwork.db')
#c = conn.cursor()
#c.execute("""CREATE TABLE friends (
#        user1_id INTEGER,
#        user2_id INTEGER,
#        Movie_proximity REAL,
#        Music_proximity REAL,
#        Sports_proximity REAL,
#        Food_proximity REAL,
#        Travel_proximity REAL,
#        default_proximity REAL
#    )""")

#-------------------------------------------------------------------

#-----------------------------------------Using Network.py functions-----------------------------------


def get_available_userid():
    #Connect to database
    conn = sqlite3.connect('socialnetwork.db')
    #Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("Select rowid, * FROM users")
    items = c.fetchall()

    id = 1
    for item in items:
        id = item[0] + 1
    
    #commit our command
    conn.commit()
    #close connection
    conn.close()
    return id

def get_available_friend_id():
    #Connect to database
    conn = sqlite3.connect('socialnetwork.db')
    #Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("Select rowid, * FROM friends")
    items = c.fetchall()

    id = 1
    for item in items:
        id = item[0] + 1
    
    #commit our command
    conn.commit()
    #close connection
    conn.close()
    return id


#---------------------------------------User table functions----------------------------------------------------------
def get_all_users():
    #Connect to database
    conn = sqlite3.connect('socialnetwork.db')
    #Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("Select rowid, * FROM users")
    items = c.fetchall()

    for item in items:
        print(item)
    
    #commit our command
    conn.commit()
    #close connection
    conn.close()


def add_user_to_users(password):
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(?)", (password,))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

def delete_user_from_users (user_id) :
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("DELETE from users WHERE rowid = (?)", (user_id,))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

#-------------------------------------------------------------------------------------------------------------------
#------------------------------------------Friend table functions--------------------------------------------------

def add_friendship_to_friends( user1_id, user2_id,Movie_proximity,Music_proximity,Sports_proximity,Food_proximity,Travel_proximity,default_proximity ):
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("INSERT INTO friends VALUES(?,?,?,?,?,?,?,?)", 
    ( user1_id, user2_id,Movie_proximity,Music_proximity,Sports_proximity,Food_proximity,Travel_proximity,default_proximity))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

def delete_friendship_from_friends (friend_id) :
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("DELETE from users WHERE rowid = (?)", (friend_id,))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

def delete_friendship_only_userids (user1, user2):
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("DELETE from users WHERE (user1_id = (?) OR user1_id = (?)) AND (user2_id = (?) OR user2_id = (?))", (user1,user2,user1,user2))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

def delete_friendship_only_one_userid (user1):
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("DELETE from users WHERE (user1_id = (?) OR user2_id = (?))", (user1,user1))
    #commit our command
    conn.commit()
    #close connection
    conn.close()


def get_all_friends():
    #Connect to database
    conn = sqlite3.connect('socialnetwork.db')
    #Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("Select rowid, * FROM friends")
    items = c.fetchall()

    for item in items:
        print(item)
    
    #commit our command
    conn.commit()
    #close connection
    conn.close()


#-----------------------------------------------------------------------------------
#------------------------------------------Opinion Table functions-------------------------------------------------


def add_opinion_to_opinions(User_id,category,item,rating):
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("INSERT INTO opinions VALUES(?,?,?,?)", (User_id,category,item,rating))
    #commit our command
    conn.commit()
    #close connection
    conn.close()


def delete_opinion_from_opinions (user_id) :
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("DELETE from opinions WHERE User_id = (?)", (user_id,))
    #commit our command
    conn.commit()
    #close connection
    conn.close()





def get_all_opinions():
    #Connect to database
    conn = sqlite3.connect('socialnetwork.db')
    #Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("Select rowid, * FROM opinions")
    items = c.fetchall()

    for item in items:
        print(item)
    
    #commit our command
    conn.commit()
    #close connection
    conn.close()

#---------------------------------Deleting a table----------

def delete_friend_table():
    #Connect to database
    conn = sqlite3.connect('socialnetwork.db')
    #Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("DROP TABLE friends")
    
    #commit our command
    conn.commit()
    #close connection
    conn.close()

