#name of file you want to import
import numpy as np

def NodesAtRadius(start_node, radius):
    print("working")
    nodes_at_radius = np.array([1,2])
    return nodes_at_radius

def RecommendationList(user_list, nodes_at_radius):
    found = False
    for x in nodes_at_radius:
        #for data of the category
        #for y in data
        for z in user_list:
           # if x == y 
           found = True
                #Continue
        if found:
            np.append(user_list, z)

    recommendations = np.array(["apples","bananas"])
    return recommendations

def BreathFirst(network, start_node):

def CalculateMatchPercentage(rating, distance_from_user):
    
def main():
    NodesAtRadius(2,2)


if __name__ == "__main__":
    main()
