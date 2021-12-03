from typing import Dict
import networkx as nx
from networkx import node_connected_component
from networkx.algorithms.components.connected import connected_components
from Friend import Friend
from User import Opinion, User
import database
import numpy as np

class MatchAlgorithm:

    def Length(self, graph:nx.Graph, u1:User, u2:User, category:str)->float:
        f:Friend = graph[u1][u2]["friend"]
        if (f.proximity[category] != 12.0):
            return f.proximity[category]
        return f.proximity["Default"]

# Returns a dictionary where users are mapped against Dijkstra's Distance
    def GetDijkstraList(self, graph:nx.Graph, category:str, current_user:User)->dict:
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

    def GetPotentialMatches(self, dijkstra_dict:dict, current_user:User, category:str)->list:
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

    def GetWeightedDict(self, dijkstra_dict:dict)->dict:
        
        max_value = max(dijkstra_dict.values())
        
        dijkstra_keys = list(dijkstra_dict.keys())
        for item in dijkstra_keys:
            dijkstra_dict[item] = max_value - dijkstra_dict[item]
        
        return dijkstra_dict

    def GetSumDict(self, weighted_dict:dict, potential_matches:list, category:str)->dict:
        sum_dict = {}
        users = list(weighted_dict.keys())
        for match in potential_matches:
            sum_dict[match] = []
            for user in users:
                if match in list(user.interests[category].keys()):
                    weight:float = weighted_dict[user]
                    sum_dict[match].append(weight * float(user.interests[category][match][0]))
        
        return sum_dict

    def GetBestMatch(self, sum_dict:dict)->list:
        matches = list(sum_dict.keys())
        best_match = None
        max_score = 0
        for match in matches:
            match_sum:list = sum_dict[match]
            if len(match_sum) == 0:
                break
            else:
                score = sum(match_sum) / len(match_sum)
            if score > max_score:
                best_match = match
                max_score = score
        
        return best_match

    def GetPotentialFriends(self, dijkstra_dict:dict, current_user:User, network:nx.Graph)->list:
        dijkstra_list = list(dijkstra_dict.items())
        dijkstra_list.sort(key = lambda x: x[1])
        current_user_friends:list = list(network.adj[current_user])
        matches = []
        for item in dijkstra_list:
            user:User = item[0]
            if (user in current_user_friends):
                pass
            else:
                matches.append(user)
            if len(matches) >= 8:
                break

        return matches




    # g = nx.Graph()
    # g.add_node(1)
    # g.add_node(2)
    # g.add_node(3)
    # g.add_edge(1,2)
    # print(node_connected_component(g, 2))
