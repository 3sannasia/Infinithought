
from Friend import Friend
from User import Opinion, User
import database
import Network


import matplotlib.pyplot as plt
import unittest

class NetworkAndDatabaseTestMethods(unittest.TestCase):
    # Network class utilizes functions within the Database class
    def AddUser(self):
        network = Network()
        logininfo1 = "password1"
        logininfo2 = "password2"
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2)
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo1, listOfOpinions)
        self.assertEqual(int(database.get_available_userid()), 2)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo2, listOfOpinions)
        self.assertEqual(int(database.get_available_userid()), 3)
    
    def DeleteUser(self):
        network = Network()
        logininfo1 = "password1"
        logininfo2 = "password2"
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2)
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo1, listOfOpinions)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo2, listOfOpinions)
        network.DeleteUser(2)
        self.assertEqual(int(database.get_available_userid()), 2)

    def DatabaseAddOpinion(self):
        network = Network()
        logininfo1 = "password1"
        logininfo2 = "password2"
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2) 
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo1, listOfOpinions)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo2, listOfOpinions)
        opinion_to_add = Opinion("Movies", "Frozen", 10)
        database.add_opinion_to_opinions(2, opinion_to_add)
        self.assertEqual(database.get_opinions_for_user(2), [opinion1, opinion2, opinion3, opinion_to_add])
    
    def DatabaseRemoveOpinion(self):
        network = Network()
        logininfo1 = "password1"
        logininfo2 = "password2"
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2) 
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo1, listOfOpinions)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo2, listOfOpinions)
        opinion_to_add = Opinion("Movies", "Frozen", 10)
        database.add_opinion_to_opinions(2, opinion_to_add)
        self.assertEqual(database.get_opinions_for_user(2), [opinion1, opinion2, opinion3, opinion_to_add])
        database.delete_opinion_from_opinions_for_user(opinion_to_add, 2)
        self.assertEqual(database.get_opinions_for_user(2), listOfOpinions)

    
    
    def get_available_userid(self):
            first_user = User(123)
        first_user.AddOpinion(opinion)
        get
        
        

    def get_available_friend_id(self):
    
    def get_all_users(self):

    def add_users_to_users(self):

    def delete_user_from_users(self):

    def add_friendship_to_friends(self):

    def delete_friendship_from_friends(self):

    def delete_friendship_only_userids (user1, user2):
    
    def delete_friendship_only_one_userid (user1):
    
    def get_all_friends():
    
    def add_opinion_to_opinions(User_id,opinion:Opinion):

    def delete_opinion_from_opinions (user_id:int) :
    
    def delete_opinion_from_opinions_for_user (opinion:Opinion, uid:int) :

    def get_opinions_for_user(user_id):

    def get_all_opinions():

    def delete_all_tables():


if __name__ == '__main__':
    unittest.main()