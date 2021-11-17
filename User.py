from typing import Dict

# The opinion class that will hold the user's opinion 
# Three data members within the opinion, the general category that the opinion is about, the specific item in that category, and the rating for that specific item in the category
# For the rating, 1 is the worst rating(integers) and 10 is the best rating 
# For example "Movies" as the category, "Frozen" as the item, and 10 as the rating
class Opinion:
    def __init__(self, category, item, rating) -> None:
        self.category = str(category)   #initializing the category data member of the opinion object
        self.item = str(item)           #initializing item data member of the opinion object
        self.rating = int(rating)       #initializing the rating data member of the opinion object
# COULD THROW EXCEPTION IF RATING ABOVE 10 AND LESS THAN 0 AND IF CATEGORY INVALID

# Each node in the social network will be represented as a user object
class User:
    def __init__(self, uid) -> None:
        self._userId = int(uid)              #user has a userID
        movie_opinions = {}                  #user has dictionary of movie opinions
        music_opinions = {}                  #user has dictionary of music opinions
        sports_opinions = {}                 #user has dictionary of sports opinions
        food_opinions = {}                   #user has dictionary of food opinions
        travel_opinions = {}                 #user has dictionary of travel opinions
        self._interests_ = {                 #user has a dictionary of interests that holds all the other dictionaries of interests
            "Movies" : movie_opinions,
            "Music" : music_opinions,
            "Sports" : sports_opinions,
            "Food" : food_opinions,
            "Travel" : travel_opinions
        }
    
    # “getter” for a read-only attribute 
    @property                   
    def userID(self) -> int:
        return self._userId
        
    # “getter” for a read-only attribute 
    @property
    def interests(self) -> Dict:
        return self._interests_
    # Adds an Opinion object to the _interests_ dictionary data member of the User node into the specific category specified in the oOpinion object
    # Void function
    def AddOpinion(self, opinion : Opinion) -> None:
        # SHOULD WE CHECK IF NOT A VALID CATEGORY
        self._interests_[opinion.category][opinion.item] = [opinion.rating] 

    # Deletes the passed Opinion object from the the _interests_ dictionary data member of the User node
    # Void function
    def DeleteOpinion(self, opinion: Opinion) -> None:
        # SHOULD WE CHECK IF OPINION DOESNT EXIST
        del self._interests_[opinion.category][opinion.item]