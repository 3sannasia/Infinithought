#name of file you want to import
import networkx as nx

#Returns list of recomendations the user does not have
def RecommendationList(network_graph, user, category):
    recomendation_list = []
    all_friends = list(nx.bfs_edges(network_graph, user)) # so list of friend objects
    for friend in all_friends:
        for user_item in user.user.interests[category]:
            for friend_item in friend._second.user.interests[category]:
                if user_item == friend_item:
                    continue
                else:
                    recomendation_list.append(friend_item)
    return recomendation_list

#Returns tuple of each nodes proximities, opinions for that category, and the distance from the user using BFS
def GetProximity_Opinion_Distance_List_Tuple(network_graph, user, category):
    distance_from_user = 0
    proximity_tuple = []
    all_friends = list(nx.bfs_edges(network_graph, user))
    for friend in all_friends:
        distance_from_user += 1
        proximity_tuple.append(friend.proximity[category], friend.u2.interests()[category], distance_from_user)
 #tuple of the friend's proximity, the whole interests for that category specified, and distance from user node
    return proximity_tuple
    
#Calculates and returns a list of match percentages for each node in the provided network graph
def CalculateMatchPercentage(network_graph, proximity_tuple):
    match_percentage_list = []
    total_nodes = network_graph.number_of_nodes()
    for friend_data_tuples in proximity_tuple:
        match_percentage = friend_data_tuples[0] * (friend_data_tuples[2] / total_nodes) #Subject to change
        match_percentage_list.append(match_percentage)
    return match_percentage_list

#returns best match node
def Find_Best_Match(network_graph, user, match_percentage_list):
    best_node_position = 0
    curr_node_position = 0
    max_percentage = match_percentage_list[0]
    for match_percentages in match_percentage_list:
        curr_node_position += 1
        if match_percentages > max_percentage:
            max_percentage = match_percentages
            best_node_position = curr_node_position
    all_friends = GetFriends(network_graph, user)
    return all_friends[best_node_position]

def GetFriends(network_graph, user):
    all_friends = list(nx.bfs_edges(network_graph, user))
    return all_friends

    
    



#def main():


#if __name__ == "__main__":
  #  main()
