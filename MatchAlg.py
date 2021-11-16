import networkx as nx
from networkx import node_connected_component
from networkx.algorithms.components.connected import connected_components
from Friend import Friend
from User import Opinion, User
import database
import numpy as np

class MatchAlgorithm:

    def Length(graph:nx.Graph, u1:User, u2:User, category:str)->float:
        f:Friend = graph[u1][u2]["friend"]
        if (f.proximity[category] != 12.0):
            return f.proximity[category]
        return f.proximity["Default"]

    def GetDijkstraList(graph:nx.Graph, category:str, current_user:User)->dict:
        all_nodes:set = node_connected_component(graph, current_user)
        shortest_path = {}
        for node in all_nodes:
            shortest_path[node] = np.inf
        shortest_path[current_user] = 0

        while all_nodes:
            current_min = None
            for node in all_nodes:
                if current_min == None:
                    current_min = node
                elif shortest_path[node] < shortest_path[current_min]:
                    current_min = node
            
            neighbours = list(graph.adj[current_min])
            for neighbour in neighbours:
                if neighbour in all_nodes:
                    tentative_dist = shortest_path[current_min] + MatchAlgorithm.Length(graph, current_min, neighbour, category)
                    if tentative_dist < shortest_path[neighbour]:
                        shortest_path[neighbour] = tentative_dist
            
            all_nodes.remove(current_min)
        
        del shortest_path[current_user]
        return shortest_path

    def GetPotentialMatches(dijkstra_dict:dict, current_user:User, category:str)->list:
        dijkstra_list = list(dijkstra_dict.items())
        dijkstra_list.sort(key = lambda x: x[1])
        matches = []
        for item in dijkstra_list:
            user:User = item[0]
            user_items:list = list(user.interests[category].keys())
            current_user_items:list = list(current_user.interests[category].keys())
            for user_item in user_items:
                if user_item in current_user_items:
                    pass
                elif user_item in matches:
                    pass
                else:
                    matches.append(user_item)
                if len(matches) >= 8:
                    break
            
            if len(matches) >= 8:
                break

        return matches

    def GetWeightedDict(dijkstra_dict:dict)->dict:
        
        dijkstra_list = list(dijkstra_dict.values())
        max_value = 0.0
        for item in dijkstra_list:
            if item > max_value:
                max_value = item
        
        for item in dijkstra_dict:
            dijkstra_dict[item] = max_value - item
        
        return dijkstra_dict

    def GetSumDict(weighted_dict:dict, potential_matches:list, category:str)->dict:
        sum_dict = {}
        users = list(weighted_dict.keys())
        for match in potential_matches:
            sum_dict[match] = []
            for user in users:
                if match in list(user.interests[category].keys()):
                    weight = weighted_dict[user]
                    sum_dict[match].append(float(weight * user.interests[category][match]))
        
        return sum_dict

    def GetBestMatch(sum_dict:dict)->list:
        for item in sum_dict:
            
        pass



    g = nx.Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(1,2)
    print(node_connected_component(g, 2))
