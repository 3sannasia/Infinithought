from User import Opinion, User
from typing import Dict
from typing import List
import math

# Friend class represents edges between nodes(User Objects), to represent the friend relationship
class Friend:
    def __init__(self, fid, u1:User, u2:User) -> None:
        self._friendId = int(fid)                         # Initializes the friendID of the Friend
        self._first = u1                                  # Initializes the source connection of the Friend edge to first user passed
        self._second = u2                                 # Initializes the destination of the connection of the Friend edge to the second user passed
        self.FindProximity()                              # Calculates the proximity between the the two users connected by this "friend" edge
    
    # Returns array of the first and second user that are connected by this Friend object edge
    @property
    def users(self)->List:
        return [self._first, self._second]

    # Returns array of the first and second user that are connected by this Friend object edge    
    @property
    def friendID(self)->int:
        return self._friendId

    # Returns proximity of this Friend relationship between two nodes in the social network
    @property
    def proximity(self)->Dict:
        return self._prox

    # Void function that finds proximity of each dictionary of opinions for each category in the social network nodes
    def FindProximity(self)->None:
        self._prox = {
            "Movies" : self._GetProx("Movies"),
            "Music" : self._GetProx("Music"),
            "Sports" : self._GetProx("Sports"),
            "Food" : self._GetProx("Food"),
            "Travel" : self._GetProx("Travel"),
            "Default" : self._GetDefProx()
        }

    # Calculates the proximity of the specific category passed into it
    def _GetProx(self, category)->float:
        default_proximity = 11.0
        u1_items = self._first.interests.get(category).keys()
        u2_items = self._second.interests.get(category).keys()
        overlap_items = [value for value in u1_items if value in u2_items]
        
        if (len(overlap_items) == 0):     #if no overlap in items between User 1 and User 2 in the friend relationship, default proximity assigned
            return default_proximity
        
        total = 0
        
        # Calculates proximity by taking into account the items shared by User 1 and User 2
        for item in overlap_items:
            a = sum(self._first.interests.get(category).get(str(item)))
            b = sum(self._second.interests.get(category).get(str(item)))
            total += (a-b)**2
        total /= len(overlap_items)
        return math.sqrt(total)

    # Gets the definitive total proximity of all the categories within the interests of User 1 and User 2 collectively into one proximity value
    # Returns that definitive total proximity in the friend relationship
    def _GetDefProx(self)->float:
        categories = ["Movies", "Music", "Sports", "Food", "Travel"] 
        total = 0
        valid = 0
        for cat in categories:
            prox = self._GetProx(cat)
            if (prox != 11.0):
                valid += 1
                total += prox

        if (valid == 0):
            return 11.0
        else:
            return total/valid
        
# u1 = User(123)
# u2 = User(234)
# o1 = Opinion("Movies", "A", 3)
# o2 = Opinion("Movies", "B", 3)
# o2k = Opinion("Movies", "B", 10)
# o3 = Opinion("Movies", "C", 4)
# o4 = Opinion("Movies", "D", 4)
# u1.AddOpinion(o1)
# u1.AddOpinion(o2)
# u1.AddOpinion(o3)
# u2.AddOpinion(o2k)
# u2.AddOpinion(o3)
# u2.AddOpinion(o4)
# f = Friend(123, u1, u2)
# print(f.proximity["Movies"])
# print(f.proximity["Default"])

