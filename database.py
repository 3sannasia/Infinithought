import sqlite3
from typing import List
from User import Opinion, User
from Friend import Friend

#------------------THIS IS TO CREATE THE TABLES -----------------------




#Create 3 Tables

# conn = sqlite3.connect('socialnetwork.db')
# c = conn.cursor()

# c.execute("""CREATE TABLE users (
#        User_id INTEGER,
#        password text
#    )""")

    
# c.execute("""CREATE TABLE opinions (
#        User_id INTEGER,
#        category text,
#        item text,
#        rating INTEGER
#    )""")

# c.execute("""CREATE TABLE friends (
#        Friend_id INTEGER,
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
    c.execute("Select User_id, * FROM users")
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
    c.execute("Select Friend_id, * FROM friends")
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

# Ideally, this is supposed to create user objects from the database data and return a list of them.
def get_all_users()->List:
    #Connect to database
    conn = sqlite3.connect('socialnetwork.db')
    #Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("Select User_id, * FROM users")
    items = c.fetchall()

    users = []

    for item in items:
        u = User(int(item))
        opinions = get_opinions_for_user(int(item))
        for opinion in opinions:
            u.AddOpinion(opinion)
        users.append(u)
    
    #commit our command
    conn.commit()
    #close connection
    conn.close()

    return users


def add_user_to_users(user:User, password):
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(?,?)", (user.userID, password))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

def delete_user_from_users (user_id) :
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("DELETE from users WHERE User_id = (?)", (user_id))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

#-------------------------------------------------------------------------------------------------------------------
#------------------------------------------Friend table functions--------------------------------------------------

def add_friendship_to_friends( f:Friend ):
    # Since this is also an update function it deletes an old entry if any
    delete_friendship_from_friends(f.friendID)
    
    # Unpacks the friend object
    friend_id = f.friendID
    user1_id = f.users[0].userID
    user2_id = f.users[1].userID
    Movie_proximity = f.proximity["Movies"]
    Music_proximity = f.proximity["Music"]
    Sports_proximity = f.proximity["Sports"]
    Food_proximity = f.proximity["Food"]
    Travel_proximity = f.proximity["Travel"]
    default_proximity = f.proximity["Default"]

    # Creates the cursor and stuff
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("INSERT INTO friends VALUES(?,?,?,?,?,?,?,?,?)", 
    (friend_id, user1_id, user2_id,Movie_proximity,Music_proximity,Sports_proximity,Food_proximity,Travel_proximity,default_proximity))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

def delete_friendship_from_friends (friend_id) :
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("DELETE from users WHERE Friend_id = (?)", (friend_id,))
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
    c.execute("Select Friend_id, user1_id, user2_id, Movie_proximity ,Music_proximity, Sports_proximity, Food_proximity, Travel_proximity, default_proximity, * FROM friends")
    items = c.fetchall()

    

    # Creates a dictionary of all users mapped to their UserID (To find the users for the friend object)
    users = get_all_users()
    user_dict = {}
    for user in users:
        users[user.userID] = user

    # Creates a list of all friend objects
    friends = []
    for item in items:
        u1 = user_dict.get(item[1])
        u2 = user_dict.get(item[2])
        f = Friend(item[0], u1, u2)
        f.AddProximity(item[3], item[4],item[5],item[6],item[7],item[8])
        friends.append(f)
    
    #commit our command
    conn.commit()
    #close connection
    conn.close()

    return friends


#-----------------------------------------------------------------------------------
#------------------------------------------Opinion Table functions-------------------------------------------------


def add_opinion_to_opinions(User_id,opinion:Opinion):
    
    delete_opinion_from_opinions(opinion)

    category = opinion.category
    item = opinion.item
    rating = opinion.rating
    
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("INSERT INTO opinions VALUES(?,?,?,?)", (User_id,category,item,rating))
    #commit our command
    conn.commit()
    #close connection
    conn.close()


def delete_opinion_from_opinions (user_id:int) :
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("DELETE from opinions WHERE User_id = (?)", (user_id))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

def delete_opinion_from_opinions (opinion:Opinion) :
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("DELETE from opinions WHERE (category = (?)) AND (item = (?))", (opinion.category, opinion.item))
    #commit our command
    conn.commit()
    #close connection
    conn.close()

def get_opinions_for_user(user_id):
    conn = sqlite3.connect('socialnetwork.db')
    c = conn.cursor()
    c.execute("SELECT from opinions WHERE User_id = (?)", (user_id))
    rows = c.fetchall()
    opinions = []

    for row in rows:
        o = Opinion(str(row[1]), str(row[2]), int(row[3]))
        opinions.append(o)

    #commit our command
    conn.commit()
    #close connection
    conn.close()

    return opinions


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

def delete_user_table():
    #Connect to database
    conn = sqlite3.connect('socialnetwork.db')
    #Create a cursor
    c = conn.cursor()

    #Query the Database
    c.execute("DROP TABLE users")
    
    #commit our command
    conn.commit()
    #close connection
    conn.close()
