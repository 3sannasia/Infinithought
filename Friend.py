from User import Opinion, User
from typing import Dict
from typing import List
import math

class Friend:
    def __init__(self, fid, u1:User, u2:User) -> None:
        self._friendId = int(fid)
        self._first = u1
        self._second = u2
    
    @property
    def users(self)->List:
        return [self._first, self._second]

    @property
    def friendID(self)->int:
        return self._friendId

    @property
    def proximity(self)->Dict:
        return self._prox

    def AddProximity(self, movies, music, sports, food, travel, default) -> None:
        self._prox = {
            "Movies" : movies,
            "Music" : music,
            "Sports" : sports,
            "Food" : food,
            "Travel" : travel,
            "Default" : default
        }

    def FindProximity(self)->None:
        self._prox = {
            "Movies" : self._GetProx("Movies"),
            "Music" : self._GetProx("Music"),
            "Sports" : self._GetProx("Sports"),
            "Food" : self._GetProx("Food"),
            "Travel" : self._GetProx("Travel"),
            "Default" : self._GetDefProx()
        }

    def _GetProx(self, category)->float:
        u1_items = self._first.interests.get(category).keys()
        u2_items = self._second.interests.get(category).keys()
        overlap_items = [value for value in u1_items if value in u2_items]
        
        if (len(overlap_items) == 0):
            return 11.0

        total = 0
        
        for item in overlap_items:
            a = sum(self._first.interests.get(category).get(str(item)))
            b = sum(self._second.interests.get(category).get(str(item)))
            total += (a-b)**2
        total /= len(overlap_items)
        return math.sqrt(total)

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



    