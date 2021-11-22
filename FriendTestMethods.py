import unittest
from User import Opinion, User
from Friend import Friend

class FriendTestMethods(unittest.TestCase):
    user1 = User(123)
    user2 = User(234)
    friend_relationship1 = Friend(123, user1, user2)
    opinion = Opinion("Movies", "Frozen", 10)
    opinion1 = Opinion("Movies", "A", 3)
    opinion2 = Opinion("Movies", "B", 3)
    opinion3 = Opinion("Movies", "Z" , 10)
    opinion4 = Opinion("Movies", "C", 4)
    opinion5 = Opinion("Movies", "D", 4)
    user1.AddOpinion(opinion)
    user1.AddOpinion(opinion1)
    user1.AddOpinion(opinion2)
    user2.AddOpinion(opinion3)
    user2.AddOpinion(opinion4)
    user2.AddOpinion(opinion5) 
    friend_relationship1.proximity["Movies"]

    u1 = User(123)
    u2 = User(234)
    o1 = Opinion("Sports", "A", 3)
    o2 = Opinion("Sports", "B", 5)
    o2k = Opinion("Sports", "B", 5)
    o3 = Opinion("Sports", "C", 4)
    o4 = Opinion("Sports", "D", 4)
    u1.AddOpinion(o1)
    u1.AddOpinion(o2)
    u1.AddOpinion(o3)
    u2.AddOpinion(o2k)
    u2.AddOpinion(o3)
    u2.AddOpinion(o4)
    friend_relationship2 = Friend(123, u1, u2)
    print(friend_relationship2.proximity["Sports"])

    def test_data_members(self):
        self.assertEqual(self._first, user1)
        self.assertEqual(self._second, user2)
        self.assertEqual(self._friendId, 123)
        
    def test_find_proximity(self):
        self.assertEqual(friend_relationship1.proximity["Movies"], 4.949747468305833)
        self.assertEqual(friend_relationship1.proximity["Default"], 4.949747468305833)
        self.assertEqual(friend_relationship1.proximity["Default"], 12.0)
        self.assertEqual(friend_relationship2.proximity["Sports"], 0.0)

if __name__ == '__main__':
    unittest.main()