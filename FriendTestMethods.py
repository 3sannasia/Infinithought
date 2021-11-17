import unittest
from User import Opinion, User
from Friend import Friend

class FriendTestMethods(unittest.TestCase):
    user1 = User(123)
    user2 = User(234)
    friend_relationship1 = Friend(123, user1, user2)
    opinion = Opinion("Movies", "Frozen", 10)
    o1 = Opinion("Movies", "A", 3)
    o2 = Opinion("Movies", "B", 3)
    o2k = Opinion("Movies", "B", 10)
    o3 = Opinion("Movies", "C", 4)
    o4 = Opinion("Movies", "D", 4)
    user1.AddOpinion(o1)
    user1.AddOpinion(o2)
    user1.AddOpinion(o3)
    user2.AddOpinion(o2k)
    user2.AddOpinion(o3)
    user2.AddOpinion(o4)
    friend_relationship1.proximity["Movies"]


    def test_data_members(self):
        self.assertEqual(self._first, user1)
        self.assertEqual(self._second, user2)
        self.assertEqual(self._friendId, 123)
        
    def test_find_proximity(self):
        self.assertEqual(friend_relationship1.proximity["Movies"], FIND VAL AFTER PRINTING)
        self.assertEqual(friend_relationship1.proximity["Default"], 11.0)

#TO BE FINISHED 

if __name__ == '__main__':
    unittest.main()



#     u1 = User(123)
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