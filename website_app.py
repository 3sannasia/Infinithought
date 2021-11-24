from flask import Flask, render_template, request
import sqlite3
import os
#from Network import Network
#from User import Opinion
#import database
#import json

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
#app.secret_key="__privatekey__"

@app.route("/")
def index():
    return render_template('index.html')

#home page
@app.route('/home')
def home():
    return render_template('index.html')

#add user page
@app.route('/add_user')
def add_user():
    return render_template('Add_User.html')

#delete user page
@app.route('/delete_user')
def delete_user():
    return render_template('Delete_User.html')

#remove opinion page
@app.route('/remove_opinion')
def remove_opinion():
    return render_template('Remove_Opinion.html')

#add opinion page
@app.route('/add_opinion')
def add_opinion():
    return render_template('Add_Opinion.html')

#make friend page
@app.route('/make_friend')
def make_friend():
    return render_template('Make_Friend.html')

#unfriend page
@app.route('/un_friend')
def un_friend():
    return render_template('Un_Friend.html')

#find match page
@app.route('/find_match')
def find_match():
    return render_template('Find_Match.html')

if __name__ == "__main__" :
    app.run()





