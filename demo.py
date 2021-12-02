from Network import Network
from User import Opinion
import database




# Repository of Opinions
o1 = Opinion("Movies", "Lion King", 2)
o2 = Opinion("Movies", "Lion King", 6)
o3 = Opinion("Movies", "Lion King", 10)

o4 = Opinion("Movies", "Matilda", 2)
o5 = Opinion("Movies", "Matilda", 6)
o6 = Opinion("Movies", "Matilda", 10)

o7 = Opinion("Movies", "The Kissing Booth", 2)
o8 = Opinion("Movies", "The Kissing Booth", 6)
o9 = Opinion("Movies", "The Kissing Booth", 10)

o10 = Opinion("Movies", "Avatar", 2)
o11 = Opinion("Movies", "Avatar", 6)
o12 = Opinion("Movies", "Avatar", 10)

# Populates database and Network
def demo1()->None:
    

    # Refresh Database
    database.delete_all_tables()
    database.make_tables()

    # Creating a network object
    network = Network()

    # Add User function
    # Changes should be reflected in network and all database tables
    network.AddUser("password1", [o1, o4, o7])
    network.AddUser("password2", [o2, o5, o8])
    network.AddUser("password3", [o3, o6, o9])
    network.AddUser("password4", [o2, o4, o9])
    network.AddUser("password5", [o11, o2, o9])
    network.AddUser("password6", [o5, o8, o1])
    network.AddUser("password7", [o3, o6, o9])
    network.AddUser("password8", [o7, o12, o4])
    network.AddUser("password9", [o5, o8, o1])
    network.AddUser("password10", [o3, o6, o9])
    network.AddUser("password11", [o7, o12, o4])
    network.AddUser("password12", [o5, o9, o2])
    network.AddUser("password13", [o3, o6, o9])
    network.AddUser("password14", [o7, o11, o4])
    network.AddUser("password15", [o7, o4, o1])
    network.AddUser("password16", [o3, o5, o9])
    network.AddUser("password17", [o9, o12, o4])

    network.Draw()

# Reads from the database, makes changes that are reflected in the database and the Network
def demo2()->None:

    # Creating a network object
    network = Network()

    # Delete User
    network.DeleteUser(5)
    network.DeleteUser(3)
    network.DeleteUser(2)

    # Add opinion to user
    u4 = network.GetUser(4)
    u6 = network.GetUser(6)
    u7 = network.GetUser(7)
    u8 = network.GetUser(8)
    u11 = network.GetUser(11)
    print("Movie Proximity for 4-6 and 4-7:")
    print(network.MakeFriend(u4, u6).proximity["Movies"])
    print(network.MakeFriend(u4, u7).proximity["Movies"])
    network.AddOpinion(u4, o6)
    print("Movie Proximity for 4-6 and 4-7 after opinion is added:")
    print(network.network[u4][u6]["friend"].proximity["Movies"])
    print(network.network[u4][u7]["friend"].proximity["Movies"])


    #Remove opinion from user
    network.RemoveOpinion(u4, o6)
    print("Movie Proximity for 4-6 and 4-7 after opinion is added:")
    print(network.network[u4][u6]["friend"].proximity["Movies"])
    print(network.network[u4][u7]["friend"].proximity["Movies"])

    # Make Friend and UnFriend
    print("Friends of 4")
    print(list(network.network.adj[u4]))
    network.MakeFriend(u6, u4)
    network.MakeFriend(u8, u4)
    network.MakeFriend(u8, u11)
    network.UnFriend(u4, u6)
    print("Friends of 4 after execution")
    print(list(network.network.adj[u4]))
    print(u6)
    print(u8)
    
    print("Find Match for User4:")
    print(network.FindMatch(u4,"Movies"))

def demo3()->None:
    # Refresh Database
    database.delete_all_tables()
    database.make_tables()

    # Creating a network object
    network = Network()

    try:
        network.AddUser("password1", [])
        network.AddUser("password2", [])
    except:
        print("DUMMMMASS")
    print("Yo")




# Demo Execution

# demo1()
# demo2()
demo3()

