from flask import Flask, render_template, request
import sqlite3
import os
from Network import Network
from User import Opinion
#import database
#import json

currentdirectory = os.path.dirname(os.path.abspath(__file__))
network = Network()

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
        try:  
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
#*************   network.AddUser(password,[o1]) ****************** NOT WORKING
            msg = "User is successfully added!"
        except:   
            msg = "We can not add the user to the database" 
        finally:  
            return render_template("success.html",msg = msg)    

#delete user page
@app.route('/delete_user')
def delete_user():
    return render_template('Delete_User.html')


@app.route("/savedetails_addUser",methods = ["POST","GET"])  
def saveDetails_deleteUser():  
    msg = "msg" 
    if request.method == "POST":  
        try:  
            userid = request.form["user_id"]

            #deleting from network to the network  
            network.DeleteUser(int(userid))
            msg = "User is successfully deleted!"
        except:   
            msg = "We can not delete the user from the database" 
        finally:  
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
        try:  
            category = request.form["category"]  
            item = request.form["item"]  
            userid = request.form["user_id"]  
            rating = request.form["rating"]

            #checking for right user inputs
            if (int(rating) > 10 or int(rating) < 1):
                raise ValueError
            if (category != "Movies" and category != "Sports" or category != "Travel" or category != "Music" or category != "Food"):
                raise ValueError

            #adding opinion to the network
            u1 = network.GetUser(int(userid))
            o1 = Opinion(category, item, int(rating))  
            network.RemoveOpinion(u1,o1)
            msg = "Opinion is successfully removed!"
        except:   
            msg = "We can not remove the opinion from the database" 
        finally:  
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
        try:  
            category = request.form["category"]  
            item = request.form["item"]  
            userid = request.form["user_id"]  
            rating = request.form["rating"]

            #checking for right user inputs
            if (int(rating) > 10 or int(rating) < 1):
                raise ValueError
            if (category != "Movies" and category != "Sports" or category != "Travel" or category != "Music" or category != "Food"):
                raise ValueError

            #adding opinion to the network
            u1 = network.GetUser(int(userid))
            o1 = Opinion(category, item, int(rating))  
            network.AddOpinion(u1,o1)
            msg = "Opinion is successfully added!"
        except:   
            msg = "We can not add the opinion to the database" 
        finally:  
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
        try:   
            userid1 = request.form["user_id1"] 
            userid2 = request.form["user_id2"] 
            
            #adding opinion to the network
            u1 = network.GetUser(int(userid1))
            u2 = network.GetUser(int(userid2)) 
            network.MakeFriend(u1,u2)
            msg = "Friendship is successfully created!"
        except:   
            msg = "We can not create the friendship in the database" 
        finally:  
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
        try:   
            userid1 = request.form["user_id1"] 
            userid2 = request.form["user_id2"] 
            
            #adding opinion to the network
            u1 = network.GetUser(int(userid1))
            u2 = network.GetUser(int(userid2)) 
            network.UnFriend(u1,u2)
            msg = "Friendship is successfully deleted!"
        except:   
            msg = "We can not delete the friendship in the database" 
        finally:  
            return render_template("success.html",msg = msg) 
    
#-----------------------------------------------------------------------
#--------------------------Find Match--------------------------------------------

#find match page
@app.route('/find_match')
def find_match():
    return render_template('Find_Match.html')

#using network to find match
@app.route("/savedetails_findMatch",methods = ["POST","GET"])  
def saveDetails_findMatch():  
    msg = "msg" 
    if request.method == "POST":  
        try:   
            userid1 = request.form["user_id1"] 
            category = request.form["category"] 

            #checking for right user inputs
            if (category != "Movies" and category != "Sports" or category != "Travel" or category != "Music" or category != "Food"):
                raise ValueError
            
            #adding opinion to the network
            u1 = network.GetUser(int(userid1))
            list = network.FindMatch(u1,category)
            #NEED TO WORK ON SHOWING BESTMATCH
            msg = "Match is successfully found!"
        except:   
            msg = "We can not find a match in the database" 
        finally:  
            return render_template("success.html",msg = msg) 

#---------------------------------------------------------------------------------

#runs the application
if __name__ == "__main__" :
    app.run(debug = True)





