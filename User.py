from typing import Dict

class Opinion:
    def __init__(self, category, item, rating) -> None:
        self.category = str(category)
        self.item = str(item)
        self.rating = int(rating)


class User:

    def __init__(self, uid) -> None:
        self._userId = int(uid)
        movie_opinions = {}
        music_opinions = {}
        sports_opinions = {}
        food_opinions = {}
        travel_opinions = {}
        self._interests_ = {
            "Movies" : movie_opinions,
            "Music" : music_opinions,
            "Sports" : sports_opinions,
            "Food" : food_opinions,
            "Travel" : travel_opinions
        }
    
    @property
    def userID(self) -> int:
        return self._userId
        
    @property
    def interests(self) -> Dict:
        return self._interests_

    def AddOpinion(self, opinion : Opinion) -> None:
        self._interests_[opinion.category][opinion.item] = [opinion.rating]

    def DeleteOpinion(self, opinion: Opinion) -> None:
        del self._interests_[opinion.category][opinion.item]
