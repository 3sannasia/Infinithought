import networkx as nx
from networkx.classes.function import all_neighbors
from Friend import Friend
from User import User
import database

class Network:
    def __init__(self) -> None:
        self._netwk = nx.Graph()
        self._netwk.add_nodes_from(Context.GetAllUsers())
        all_friends = Context.GetAllFriends()
        for friend in all_friends:
            self._netwk.add_edge(friend.users[0], friend.users[1], {"friend" : friend})

    @property
    def network(self)->nx:
        return self._netwk
    
    def AddUser(self, loginInfo, listOfOpinions)->None:
        # 1. Asks the database for ID for the user
        user_id = database.get_available_userid()
        # 2. Creates user object using the ID
        created_user = User(user_id)
        # 3. Adds opinions to the user object

        # 4. Stores the user object into the Database
        database.add_user_to_users(loginInfo)
        # 5. Finds a friend for the user
            #need this function to do the rest -> set this other user = found_friend, I made a dummy User that is the friend - Aryan
        found_friend = User(user_id+1)
        # 6. Asks Database for ID for the friend object
        friend_id = database.get_available_friend_id()
        # 7. Creates friend object using ID
        friendship = Friend(friend_id,user_id,user_id+1)
        # 8. Stores friend object in the Database
            #Need to store the proximity values into the friend table - Aryan
        pass
    

    def DeleteUser(self, userID)->None:
        # 1. Looks for the User in the Network and deletes the node
        # 2. Deletes all edges of the node while maintainging a list of all friend IDs
        # 3. Deletes user from the Database using UserID
        database.delete_user_from_users(userID)
        # 4. Delete opinions from the Database using UserID
        database.delete_opinion_from_opinions(userID)
        # 5. Delete friends from the Database using FriendID
        database.delete_friendship_only_one_userid(userID)
        pass

    def AddOpinion(self, user, opinion)->None:
        # 1. Adds Opinion in the Opinion Table of the Database
        database.add_opinion_to_opinions(user.userID, opinion.category, opinion.item, opinion.rating) # would this work and would we need to add userID as a parameter
        # 2. Adds or Updates Opinion to the User Object in the Network
        user.AddOpinion(opinion)
        # 3. Updates Proximity values for all adjacent friend objects
                        #pseudocode: iterate through all the edges connected to this user node and run GetDefProx
        # 4. Updates all friend objects in the Database where one of the users is user
        pass
    
    def RemoveOpinion(self, user, opinion)->None:
        # 1. Removes Opinion from the Opinion Table of the Database
        # 2. Removes Opinion to the User Object in the Network
        # 3. Updates Proximity values for all adjacent friend objects
        # 4. Updates all friend objects in the Database where one of the users is user
        pass

    def MakeFriend(self, user1, user2)->None:
        # 1. Asks Database for ID for the friend object
        friend_id = database.get_available_friend_id()
        # 2. Creates friend object using ID
        friendship = Friend(friend_id,user1,user2)
        # 3. Adds friend object to database
            #Need to store the proximity values into the friend table - Aryan
        # 4. Creates edge between the users in the Graph
        pass
    
    def UnFriend(self, user1, user2)->None:
        # 1. Deletes Friend from Database
        database.delete_friendship_only_userids(User.userID(user1), User.userID(user2))
        # 2. Deletes edge from Network
        pass

    def FindMatch(self, current_user, category):
        pass

