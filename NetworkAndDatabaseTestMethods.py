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

    def NetworkAddOpinion(self):
        first_user = User(123)
        network = Network()
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2) 
        opinion3 = Opinion("Movies", "Avatar", 10)
        network.AddOpinion(first_user, opinion1)
        network.AddOpinion(first_user, opinion2)
        network.AddOpinion(first_user, opinion3)
        self.assertEqual(database.get_opinions_for_user(123), [opinion1, opinion2, opinion3])    
    
    def get_available_userid(self):
        self.assertEqual(database.get_available_userid(), 1)
        user1 = User(2)
        self.assertEqual(database.get_available_userid(), 3)

    def get_available_friend_id(self):
        user1 = User(1)
        user2 = User(2)
        self.assertEqual(database.get_available_friend_id(), 1)
        friend_relationship1 = Friend(1, user1, user2)
        self.assertEqual(database.get_available_friend_id(), 3)
    
    # def get_all_users(self):
    #     u1 = User(1)
    #     network = Network()
    #     logininfo1 = "password1"
    #     logininfo2 = "password2"
    #     opinion1= Opinion("Movies", "Matilda", 2)
    #     opinion2 = Opinion("Movies", "The Kissing Booth", 2) 
    #     opinion3 = Opinion("Movies", "Avatar", 10)
    #     listOfOpinions = [opinion1, opinion2, opinion3]
    #     network.AddUser(logininfo1, listOfOpinions)
    #     listOfOpinions = [opinion1, opinion2, opinion3]
    #     network.AddUser(logininfo2, listOfOpinions)
    #     self.assertEqual(database.get_all_users, [])

    def add_users_to_users(self):
        user1 = User(1)
        database.add_user_to_users(user1, "password")
        self.assertEqual(database.get_available_userid, 2)

    def delete_user_from_users(self):
        user1 = User(1)
        database.add_user_to_users(user1, "password")
        self.assertEqual(database.get_available_userid, 2)
        database.delete_user_from_users(1)
        self.assertEqual(database.get_available_userid, 1)

    def add_friendship_to_friends(self):
        user1 = User(1)
        user2 = User(2)
        friend_relationship1 = Friend(1, user1, user2)
        database.add_friendship_to_friends(friend_relationship1)
        self.assertEqual(database.get_available_friend_id, 2)

    def delete_friendship_from_friends(self):
        user1 = User(1)
        user2 = User(2)
        friend_relationship1 = Friend(1, user1, user2)
        database.add_friendship_to_friends(friend_relationship1)
        self.assertEqual(database.get_available_friend_id, 2)
        database.delete_friendship_to_friends(1)
        self.assertEqual(database.get_available_friend_id, 1)

    def delete_friendship_only_userids(self):
        user1 = User(1)
        user2 = User(2)
        friend_relationship1 = Friend(1, user1, user2)
        database.add_friendship_to_friends(friend_relationship1)
        database.delete_friendship_only_userids(user1, user2)
        self.assertEqual(database.get_available_friend_id, 1)

    def delete_friendship_only_one_userid(self):
        user1 = User(1)
        user2 = User(2)
        friend_relationship1 = Friend(1, user1, user2)
        database.add_friendship_to_friends(friend_relationship1)
        database.delete_friendship_only_userids(user1, user2)
        self.assertEqual(database.get_available_friend_id, 1)
    
    def get_all_friends(self):
        user1 = User(1)
        user2 = User(2)
        friend_relationship1 = Friend(1, user1, user2)
        database.add_friendship_to_friends(friend_relationship1)
        user3 = User(3)
        user4 = User(4)
        friend_relationship2 = Friend(2, user3, user4)
        database.add_friendship_to_friends(friend_relationship2)
        self.assertEqual(database.get_all_friends(), [friend_relationship1, friend_relationship2])
    
    def delete_opinion_from_opinions_for_user(self):
        first_user = User(1)
        opinion = Opinion("Movies", "Frozen", 10)
        first_user.AddOpinion(opinion)
        database.add_user_to_users(first_user, "password")
        database.delete_opinion_from_opinions_for_user(opinion, 123)
        self.assertEqual(database.get_available_userid(1), 1)
        
    def get_opinions_for_user(self):
        first_user = User(1)
        opinion = Opinion("Movies", "Frozen", 10)
        first_user.AddOpinion(opinion)
        database.add_user_to_users(first_user, "password")
        self.assertEqual(database.get_opinions_for_user(1), 1)

    def get_all_opinions(self):
        o1 = Opinion("Movies", "Lion King", 2)
        o2 = Opinion("Movies", "Lion King", 6)
        o3 = Opinion("Movies", "Lion King", 10)

        o4 = Opinion("Movies", "Matilda", 2)
        o5 = Opinion("Movies", "Matilda", 6)
        o6 = Opinion("Movies", "Matilda", 10)
        
        network = Network()
        network.AddUser("password1", [o1, o2, o3])
        network.AddUser("password2", [o4, o5, o6])

if __name__ == '__main__':
    unittest.main()