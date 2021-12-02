from flask import Flask, render_template, request
import sqlite3
import os
from Network import Network
from User import Opinion
import database

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
#app.secret_key="__privatekey__"

#--------------------------------------------------------------HomePage and IndexPage------------------------------------------

@app.route("/")
def index():
    return render_template('index.html')

#home page
@app.route('/home')
def home():
    return render_template('index.html')

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------Add User and Delete User ----------------------------------------------------

#add user page
@app.route('/add_user')
def add_user():
    return render_template('Add_User.html')

#actually adding the user
@app.route("/savedetails_addUser",methods = ["POST","GET"])  
def saveDetails_addUser():  
    msg = "msg" 
    if request.method == "POST":    
            category = request.form["category"]  
            item = request.form["item"]  
            password = request.form["password"]  
            rating = request.form["rating"]

            #checking for right user inputs
            if (int(rating) > 10 or int(rating) < 1):
                raise ValueError
            if (category != "Movies" and category != "Sports" and category != "Travel" and category != "Music" and category != "Food"):
                raise ValueError

            #adding to the network
            o1 = Opinion(category, item, int(rating))  
            network.AddUser(password,[o1])

            #showing the output of user being added and user id

            user_id = int(database.get_available_userid())
            msg = "User is successfully added! User ID is: " + str(user_id - 1) 
            return render_template("success.html",msg = msg)    

#delete user page
@app.route('/delete_user')
def delete_user():
    return render_template('Delete_User.html')


@app.route("/savedetails_deleteUser",methods = ["POST","GET"])  
def saveDetails_deleteUser():  
    msg = "msg" 
    if request.method == "POST":   
            userid = request.form["user_id"]

            #deleting from network to the network  
            network.DeleteUser(int(userid))
            msg = "User: " + userid + " is successfully deleted!"
            return render_template("success.html",msg = msg) 

#show all user page
@app.route('/show_users')
def show_users():
    return render_template('show_Users.html')


@app.route("/savedetails_showUsers",methods = ["POST","GET"])  
def saveDetails_showUsers():  
    msg = "" 
    if request.method == "POST":
            password = request.form["password"]   
            list = database.get_all_users()
            for user in list:
                msg += "|UserId: " + str(user.userID)  + " |\n"
            
            if(msg == ""):
                msg = "No users have been added"
            if(password != "password"):
                msg = "wrong password" 
            
            return render_template("success.html",msg = msg)   
    
#----------------------------------------------------------------------------------------------
#-------------------------------------------Add and Remove Opinions-----------------------------

#remove opinion page
@app.route('/remove_opinion')
def remove_opinion():
    return render_template('Remove_Opinion.html')

#removing opinion through network
@app.route("/savedetails_deleteOpinion",methods = ["POST","GET"])  
def saveDetails_removeOpinion():  
    msg = "msg" 
    if request.method == "POST":   
            category = request.form["category"]  
            item = request.form["item"]  
            userid = request.form["user_id"]  
            rating = request.form["rating"]
            #checking for right user inputs
            if (int(rating) > 10 or int(rating) < 1):
                raise ValueError
            if (category != "Movies" and category != "Sports" and category != "Travel" and category != "Music" and category != "Food"):
                raise ValueError
            #adding opinion to the network
            u1 = network.GetUser(int(userid))
            o1 = Opinion(category, item, int(rating))  
            network.RemoveOpinion(u1,o1)
            msg = "Opinion is successfully removed! Opinion removed is for UserId: " + userid + " and the opinion category is:" + category
            return render_template("success.html",msg = msg) 

#add opinion page
@app.route('/add_opinion')
def add_opinion():
    return render_template('Add_Opinion.html')

#adding opinion through network
@app.route("/savedetails_addOpinion",methods = ["POST","GET"])  
def saveDetails_addOpinion():  
    msg = "msg" 
    if request.method == "POST":  
            category = request.form["category"]  
            item = request.form["item"]  
            userid = request.form["user_id"]  
            rating = request.form["rating"]

            #checking for right user inputs
            if (int(rating) > 10 or int(rating) < 1):
                raise ValueError
            if (category != "Movies" and category != "Sports" and category != "Travel" and category != "Music" and category != "Food"):
                raise ValueError

            #adding opinion to the network
            u1 = network.GetUser(int(userid))
            o1 = Opinion(category, item, int(rating))  
            network.AddOpinion(u1,o1)
            msg = "Opinion is successfully added for UserId: " + userid  
            return render_template("success.html",msg = msg) 

#show all friends page
@app.route('/show_friends')
def show_friends():
    return render_template('show_Friends.html')


@app.route("/savedetails_showFriends",methods = ["POST","GET"])  
def saveDetails_showFriends():  
    msg = "" 
    if request.method == "POST":
            password = request.form["password"]   
            list = database.get_all_friends()
            for friend in list:
                msg += "|UserId: " + str(friend.users[0].userID) + " UserId: " + str(friend.users[1].userID) + " FriendId: " + str(friend.friendID) + "|\n"
            
            if(msg == ""):
                msg = "No friends have been added in the database"
            if(password != "password"):
                msg = "wrong password" 
            
            return render_template("success.html",msg = msg) 

#--------------------------------------------------------------------------------------------------
#------------------------------------------------Make and Remove Friendships---------------------------------

#make friend page
@app.route('/make_friend')
def make_friend():
    return render_template('Make_Friend.html')

#creating frienship through network
@app.route("/savedetails_makeFriend",methods = ["POST","GET"])  
def saveDetails_makeFriend():  
    msg = "msg" 
    if request.method == "POST":  
            userid1 = request.form["user_id1"] 
            userid2 = request.form["user_id2"] 
            
            #adding opinion to the network
            u1 = network.GetUser(int(userid1))
            u2 = network.GetUser(int(userid2)) 
            network.MakeFriend(u1,u2)
            friend_id = int(database.get_available_friend_id())
            msg = "Friendship is successfully added! Friend ID is: " + str(friend_id - 1) 
            return render_template("success.html",msg = msg) 

#unfriend page
@app.route('/un_friend')
def un_friend():
    return render_template('Un_Friend.html')

#deleting frienship through network
@app.route("/savedetails_deleteFriend",methods = ["POST","GET"])  
def saveDetails_deleteFriend():  
    msg = "msg" 
    if request.method == "POST":   
            userid1 = request.form["user_id1"] 
            userid2 = request.form["user_id2"] 
            
            #adding opinion to the network
            u1 = network.GetUser(int(userid1))
            u2 = network.GetUser(int(userid2)) 
            network.UnFriend(u1,u2)
            msg = "Friendship is successfully deleted!"
            return render_template("success.html",msg = msg) 

#show all opinions page
@app.route('/show_opinions')
def show_opinions():
    return render_template('show_Opinions.html')


@app.route("/savedetails_showOpinions",methods = ["POST","GET"])  
def saveDetails_showOpinions():  
    msg = "" 
    if request.method == "POST":
            userid = request.form["userid"]   
            list = database.get_opinions_for_user(userid)
            for opinion in list:
                msg += "|Category: " + str(opinion.category) + " Item: " + str(opinion.item) + " Rating:" + str(opinion.rating) + "|\n"
            
            if(msg == ""):
                msg = "No opinions have been added for this user" 
            
            return render_template("success.html",msg = msg) 
    
#-----------------------------------------------------------------------
#--------------------------Find Match and Find Friend--------------------------------------------

#find match page
@app.route('/find_match')
def find_match():
    return render_template('Find_Match.html')

#using network to find match
@app.route("/savedetails_findMatch",methods = ["POST","GET"])  
def saveDetails_findMatch():  
    msg = "msg" 
    if request.method == "POST":   
            userid1 = request.form["user_id1"] 
            category = request.form["category"] 

            #checking for right user inputs
            if (category != "Movies" and category != "Sports" and category != "Travel" and category != "Music" and category != "Food"):
                raise ValueError
            
            #adding opinion to the network
            u1 = network.GetUser(int(userid1))
            list = network.FindMatch(u1,category)
            if(list == None):
              msg = "Match was not found :( "
              return render_template("success.html",msg = msg)   
    
            msg = "Match is successfully found: " + list 
            return render_template("success.html",msg = msg) 


#find friend page
@app.route('/find_friend')
def find_friend():
    return render_template('Find_Friend.html')


@app.route("/savedetails_findFriend",methods = ["POST","GET"])  
def saveDetails_findFriend():  
    msg = "" 
    if request.method == "POST":
            userid = request.form["userid"] 
            u1 = network.GetUser(int(userid))
            if(u1 == None):
                msg = "UserId not found"
                return render_template("success.html",msg = msg)
             
            msg += "User " + str((network.FindFriend(u1)).userID) + " is a friend we found for you!"
            if(msg == ""):
                msg = "No friend has been found :(" 
            
            return render_template("success.html",msg = msg) 

#---------------------------------------------------------------------------------

#runs the application
if __name__ == "__main__" :
    database.delete_all_tables()
    database.make_tables()
    network = Network()
    app.run(debug = True)





