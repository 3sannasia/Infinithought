import unittest
from User import Opinion, User

class MatchAlgorithmTestMethods(unittest.TestCase):
    def TestLength(self):
        u1 = User(123)
        u2 = User(234)
        network = Network()
        o1 = Opinion("Sports", "A", 3)
        o2 = Opinion("Sports", "B", 5)
        o2k = Opinion("Sports", "B", 5)
        o3 = Opinion("Sports", "C", 4)
        o4 = Opinion("Sports", "D", 4)
        o5 = Opinion("Travel", "D", 10)
        self.assertEqual(self.Length(network, u1, u2, "Movies"), 12.0)
        u1.AddOpinion(o1)
        u1.AddOpinion(o2)
        u1.AddOpinion(o3)
        u2.AddOpinion(o2k)
        u2.AddOpinion(o3)
        u2.AddOpinion(o4)
        u2.AddOpinion(o5)
        friend_relationship1 = Friend(123, u1, u2)
        self.assertEqual(self.Length(network, u1, u2, "Movies"), 4.949747468305833)
        

    def TestGetDijkstraList(self):
        # Need Ayaan
    def TestPotentialMatches(self):
        # Need Ayaan
    def TestGetWeightedDictionary(self):
        # Need Ayaan
    def GetDictionarySum(self):
        # Need Ayaan
    def GetBestMatch(self):
        # Need Ayaan
        



    



