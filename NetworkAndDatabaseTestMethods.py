from Friend import Friend
from User import Opinion, User
import database
from Network import Network

import unittest


class NetworkAndDatabaseTestMethods(unittest.TestCase):

    def test_add_user(self):
        logininfo1 = "password1"
        logininfo2 = "password2"
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2)
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        database.make_tables()
        network = Network()
        network.AddUser(logininfo1, [])
        self.assertEqual(int(database.get_available_userid()), 2)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo2, [])
        self.assertEqual(int(database.get_available_userid()), 3)
        self.assertEqual(len(database.get_all_users()), 2)
        database.delete_all_tables()

    def test_DeleteUser(self):
        logininfo1 = "password1"
        logininfo2 = "password2"
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2)
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        database.make_tables()
        network = Network()
        network.AddUser(logininfo1, listOfOpinions)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo2, listOfOpinions)
        network.DeleteUser(2)
        self.assertEqual(int(database.get_available_userid()), 2)
        database.delete_all_tables()

    def test_DatabaseAddOpinion(self):
        logininfo1 = "password1"
        logininfo2 = "password2"
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2) 
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        database.make_tables()
        network = Network()
        network.AddUser(logininfo1, listOfOpinions)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo2, listOfOpinions)
        opinion_to_add = Opinion("Movies", "Frozen", 10)
        database.add_opinion_to_opinions(1, opinion_to_add)
        counter = 0
        for opinions in database.get_opinions_for_user(2):
            counter = counter + 1
            self.assertEqual(opinions.category, "Movies")
            if counter == 1:
                self.assertEqual(opinions.item, "Matilda")
                self.assertEqual(opinions.rating, 2)
            elif counter == 2:
                self.assertEqual(opinions.item, "The Kissing Booth")
                self.assertEqual(opinions.rating, 2)
            elif counter == 3:
                self.assertEqual(opinions.item, "Avatar")
                self.assertEqual(opinions.rating, 10)
            elif counter == 4:
                self.assertEqual(opinions.item, "Frozen")
                self.assertEqual(opinions.rating, 10)
        database.delete_all_tables()


    
    def test_DatabaseRemoveOpinion(self):
        logininfo1 = "password1"
        logininfo2 = "password2"
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2) 
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        database.make_tables()
        network = Network()
        network.AddUser(logininfo1, listOfOpinions)
        opinion_to_add = Opinion("Movies", "Frozen", 10)
        listOfOpinions2 = [opinion1, opinion2, opinion3, opinion_to_add]
        network.AddUser(logininfo2, listOfOpinions2)
        counter = 0
        for opinions in database.get_opinions_for_user(2):
            counter = counter + 1
            self.assertEqual(opinions.category, "Movies")
            if counter == 1:
                self.assertEqual(opinions.item, "Matilda")
                self.assertEqual(opinions.rating, 2)
            elif counter == 2:
                self.assertEqual(opinions.item, "The Kissing Booth")
                self.assertEqual(opinions.rating, 2)
            elif counter == 3:
                self.assertEqual(opinions.item, "Avatar")
                self.assertEqual(opinions.rating, 10)
            elif counter == 4:
                self.assertEqual(opinions.item, "Frozen")
                self.assertEqual(opinions.rating, 10)
        database.delete_all_tables()
        
    def test_NetworkAddOpinion(self):
        database.make_tables()
        network = Network()
        network.AddUser("password", [])
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2) 
        opinion3 = Opinion("Movies", "Avatar", 10)

        network.AddUser("password2", [opinion1, opinion2])
        network.MakeFriend(network.GetUser(1), network.GetUser(2))
        network.AddOpinion(network.GetUser(2), opinion3)
        counter = 0
        for opinions in database.get_opinions_for_user(2):
            counter = counter + 1
            self.assertEqual(opinions.category, "Movies")
            if counter == 1:
                self.assertEqual(opinions.item, "Matilda")
                self.assertEqual(opinions.rating, 2)
            elif counter == 2:
                self.assertEqual(opinions.item, "The Kissing Booth")
                self.assertEqual(opinions.rating, 2)
            elif counter == 3:
                self.assertEqual(opinions.item, "Avatar")
                self.assertEqual(opinions.rating, 10)
        database.delete_all_tables()

    
    def test_get_available_userid(self):
        opinion1 = Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "Frozen", 2)
        database.make_tables()
        network = Network()
        self.assertEqual(database.get_available_userid(), 1)
        network.AddUser("password1", [opinion1, opinion2])
        self.assertEqual(database.get_available_userid(), 2)
        network.AddUser("password2", [opinion1, opinion2])
        self.assertEqual(database.get_available_userid(), 3)
        database.delete_all_tables()


    def test_get_available_friend_id_and_make_friend(self):
        database.make_tables()
        network = Network()
        self.assertEqual(database.get_available_friend_id(), 1)
        opinion1 = Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "Frozen", 2)
        self.assertEqual(database.get_available_userid(), 1)
        network.AddUser("password1", [opinion1, opinion2])
        self.assertEqual(database.get_available_userid(), 2) #Not one because when a user is added, a friend connection is automatically made
        network.AddUser("password2", [opinion1, opinion2])
        self.assertEqual(database.get_available_friend_id(), 2)
        network.MakeFriend(network.GetUser(1), network.GetUser(2))
        self.assertEqual(database.get_available_friend_id(), 3)
        database.delete_all_tables()

    def test_get_all_users(self): 
        database.make_tables()
        network = Network()
        logininfo1 = "password1"
        logininfo2 = "password1"
        self.assertEqual(database.get_all_users(), [])
        opinion1= Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2) 
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo1, listOfOpinions)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo2, listOfOpinions)
        self.assertEqual(len(database.get_all_users()), 2)
        database.delete_all_tables()

    def test_add_users_to_users(self):
        user1 = User(1);
        database.make_tables()
        opinion1 = Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2)
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network = Network()
        network.AddUser("password", listOfOpinions)
        database.add_user_to_users(user1, "password")
        self.assertEqual(database.get_available_userid(), 2)
        database.delete_all_tables()

    def test_delete_user_from_users(self):
        database.make_tables()
        user1 = User(1)
        database.add_user_to_users(user1, "password")
        self.assertEqual(database.get_available_userid(), 2)
        database.delete_user_from_users(1)
        self.assertEqual(database.get_available_userid(), 1)
        database.delete_all_tables()

    def test_add_friendship_to_friends(self):
        database.make_tables()
        user1 = User(1)
        user2 = User(2)
        friend_relationship1 = Friend(1, user1, user2)
        database.add_friendship_to_friends(friend_relationship1)
        self.assertEqual(database.get_available_friend_id(), 2)
        database.delete_all_tables()

    def test_delete_friendship_from_friends_and_UnFriend(self):
        database.make_tables()
        user1 = User(1)
        user2 = User(2)
        network = Network()
        #friend relationship automatically made then below another added
        friend_relationship1 = Friend(1, user1, user2)
        database.add_friendship_to_friends(friend_relationship1)
        self.assertEqual(database.get_available_friend_id(), 2)
        network.MakeFriend(user1, user2)
        self.assertEqual(database.get_available_friend_id(), 3)
        network.UnFriend(user1, user2); #1 deleted
        self.assertEqual(database.get_available_friend_id(), 1)
        database.delete_all_tables()
    
    def test_get_all_friends(self):      
        database.make_tables()
        network = Network()
        logininfo1 = "password1"
        logininfo2 = "password2"
        opinion1 = Opinion("Movies", "Matilda", 2)
        opinion2 = Opinion("Movies", "The Kissing Booth", 2)
        opinion3 = Opinion("Movies", "Avatar", 10)
        listOfOpinions = [opinion1, opinion2, opinion3]
        network.AddUser(logininfo1, listOfOpinions)
        network.AddUser(logininfo2, listOfOpinions)
        self.assertEqual(len(database.get_all_friends()), 1)
        network.AddUser("password3", listOfOpinions)
        self.assertEqual(len(database.get_all_friends()), 2)
        network.AddUser("password4", listOfOpinions)
        self.assertEqual(len(database.get_all_friends()), 3)
        database.delete_all_tables()

    def test_delete_opinion_from_opinions_for_user(self):
        database.make_tables()
        network = Network()
        opinion = Opinion("Movies", "Frozen", 10)
        opinion2 = Opinion("Movies", "Banana", 10)
        opinion_list = [opinion, opinion2]
        network.AddUser("password", opinion_list)
        database.delete_opinion_from_opinions_for_user(opinion, 1)
        updated_opinions_list = database.get_opinions_for_user(1)
        self.assertEqual(len(updated_opinions_list), 1)
        database.delete_all_tables()
        
    def test_get_opinions_for_user(self):
        # database.delete_all_tables()
        # return
        database.make_tables()
        self.assertEqual(len(database.get_opinions_for_user(1)), 0)
        first_user = User(1)
        opinion = Opinion("Movies", "Frozen", 10)
        first_user.AddOpinion(opinion)
        network = Network()
        network.AddUser("password", [opinion])
        network.AddUser("password1", [opinion])
        database.add_user_to_users(first_user, "password")
        self.assertEqual(len(database.get_opinions_for_user(1)), 1 )
        opinions_list = database.get_opinions_for_user(1)
        self.assertEqual(opinions_list[0].category, "Movies")
        self.assertEqual(opinions_list[0].item, "Frozen")
        self.assertEqual(opinions_list[0].rating, 10)
        database.delete_all_tables()

    def test_get_all_opinions(self):
        database.make_tables()
        o1 = Opinion("Movies", "Lion King", 2)
        o2 = Opinion("Movies", "Lion King", 6)
        o3 = Opinion("Movies", "Lion King", 10)

        o4 = Opinion("Movies", "Matilda", 2)
        o5 = Opinion("Movies", "Matilda", 6)
        o6 = Opinion("Movies", "Matilda", 10)
        
        network = Network()
        network.AddUser("password1", [o1, o2, o3])
        network.AddUser("password2", [o4, o5, o6])
        database.delete_all_tables()


if __name__ == '__main__':
    unittest.main()