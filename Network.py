import networkx as nx
from Friend import Friend
from User import Opinion, User
import database
from MatchAlg import MatchAlgorithm
import random
import matplotlib.pyplot as plt

class Network:
    def __init__(self) -> None:
        self._netwk = nx.Graph()
        self._netwk.add_nodes_from(database.get_all_users())
        all_friends = database.get_all_friends()
        for friend in all_friends:
            self._netwk.add_edge(friend.users[0], friend.users[1])
            self._netwk[friend.users[0]][friend.users[1]]["friend"] = friend

    @property
    def network(self)->nx:
        return self._netwk
    
    def AddUser(self, loginInfo, listOfOpinions)->None: #redo.
        # 1. Asks the database for ID for the user
        user_id = int(database.get_available_userid())
        # 2. Creates user object using the ID
        created_user = User(user_id)
        # 3. Adds opinions to the user object
        for opinion in listOfOpinions:
            created_user.AddOpinion(opinion)
            database.add_opinion_to_opinions(user_id, opinion)
        # 3.5. Adds User object to Network as Node
        self._netwk.add_node(created_user)
        # 4. Stores the user object into the Database
        database.add_user_to_users(created_user, loginInfo)
        # 5. Finds a friend for the user
        all_users = list(self._netwk.nodes)
        if len(all_users) == 1:
            return
        
        found_friend = all_users[random.randint(1, len(all_users)-1) - 1]
        # 6. Asks Database for ID for the friend object
        friend_id = database.get_available_friend_id()
        # 7. Creates friend object using ID
        friendship = Friend(friend_id,created_user,found_friend)
        friendship.FindProximity()
        # 8. Stores friend object in the Database
        database.add_friendship_to_friends(friendship)
        # 9. Adds edge to graph
        self._netwk.add_edge(friendship.users[0], friendship.users[1])
        self._netwk[friendship.users[0]][friendship.users[1]]["friend"] = friendship
    

    def DeleteUser(self, userId)->None: #test
        # 1. Looks for the User in the Network and deletes the node
        users = list(self._netwk.nodes)
        for user in users:
            if (userId == user.userID):
                self._netwk.remove_node(user)
        # 2. Deletes user from the Database using UserID
        database.delete_user_from_users(userId)
        # 3. Delete opinions from the Database using UserID
        database.delete_opinion_from_opinions(userId)
        # 4. Delete friends from the Database using FriendID
        database.delete_friendship_only_one_userid(userId)

    def AddOpinion(self, user:User, opinion:Opinion)->None: #test
        # 1. Adds Opinion in the Opinion Table of the Database
        database.add_opinion_to_opinions(user.userID, opinion)
        # 2. Adds or Updates Opinion to the User Object in the Network
        user.AddOpinion(opinion)
        # 3. Updates Proximity values for all adjacent friend objects
        # 4. Updates all friend objects in the Database where one of the users is user
        neighbours = list(self._netwk.adj[user])
        for neighbour in neighbours:
            f:Friend = self._netwk[user][neighbour]["friend"]
            f.FindProximity()
            database.add_friendship_to_friends(f)
    
    def RemoveOpinion(self, user:User, opinion:Opinion)->None: #test
        # 1. Removes Opinion from the Opinion Table of the Database
        database.delete_opinion_from_opinions_for_user(opinion, user.userID)
        # 2. Removes Opinion to the User Object in the Network
        user.DeleteOpinion(opinion)
        # 3. Updates Proximity values for all adjacent friend objects
        # 4. Updates all friend objects in the Database where one of the users is user
        neighbours = list(self._netwk.adj[user])
        for neighbour in neighbours:
            f:Friend = self._netwk[user][neighbour]["friend"]
            f.FindProximity()
            database.add_friendship_to_friends(f)

    def MakeFriend(self, user1, user2)->Friend: #test
        # 1. Asks Database for ID for the friend object
        friend_id = database.get_available_friend_id()
        # 2. Creates friend object using ID
        friendship = Friend(friend_id,user1,user2)
        friendship.FindProximity()
        # 3. Adds friend object to database
        database.add_friendship_to_friends(friendship)
        # 4. Creates edge between the users in the Graph
        self._netwk.add_edge(user1, user2)
        self._netwk[user1][user2]["friend"] = friendship
        return friendship
    
    def UnFriend(self, user1, user2)->None: #test
        # 1. Deletes Friend from Database
        database.delete_friendship_from_friends(self._netwk[user1][user2]["friend"].friendID)
        # 2. Deletes edge from Network
        self._netwk.remove_edge(user1, user2)

    # Wrapper for executing the match algorithm.
    def FindMatch(self, current_user, category):
        # 1. Get a list of tuples :- (User, Dijkstra's Distance)
        dijkstra_list = MatchAlgorithm.GetDijkstraList(self._netwk, category, current_user)
        # 2. Identify at least 8 items such that they are taken from complete concentric distances
        potential_matches = MatchAlgorithm.GetPotentialMatches(dijkstra_list, current_user, category)
        # 3. Change the Dijkstra's Distance to Weightage using the MAX - Dist.
        
        weighted_dict = MatchAlgorithm.GetWeightedDict(dijkstra_list)
        
        # 4. Create a dictionary of those items that map to lists
        sum_dict = MatchAlgorithm.GetSumDict(weighted_dict, potential_matches, category)
        # 5. Walk the list again, for every "User" store the user's rating * Weightage for everything in the map
        # 6. Iterate throuh the map and turn all lists into a peentage rating
        # 7. Return top. 
        best_match = MatchAlgorithm.GetBestMatch(sum_dict)
        return best_match

    def Draw(self)->None:
        nx.draw(self._netwk)
        plt.savefig("nw.png")

    def GetUser(self, uid:int)->User:
        users = list(self._netwk.nodes)
        for user in users:
            if (user.userID == uid):
                return user
    

    


    

    



    
