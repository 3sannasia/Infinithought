import unittest

from networkx.algorithms import matching
from networkx.algorithms.shortest_paths.dense import reconstruct_path
from User import Opinion, User
from Friend import Friend
from User import Opinion, User
import database
from Network import Network
from MatchAlg import MatchAlgorithm

class MatchAlgorithmTestMethods(unittest.TestCase):
    # def test_Length(self):
    #     database.make_tables()
    #     match = MatchAlgorithm()
    #     network = Network()
    #     opinion1= Opinion("Movies", "Matilda", 2)
    #     opinion2 = Opinion("Movies", "The Kissing Booth", 2)
    #     opinion3 = Opinion("Movies", "Avatar", 10)
    #     opinion3_version2 = Opinion("Movies", "Avatar", 1)

    #     listOfOpinions = [opinion1, opinion2, opinion3]
    #     listOfOpinions2 = [opinion1, opinion2, opinion3_version2]

    #     network.AddUser("password1", listOfOpinions)
    #     network.AddUser("password2", listOfOpinions2)
    #     length = match.Length(network._netwk, network.GetUser(1), network.GetUser(2), "Music")
    #     print(length)
    #     self.assertEqual(length, 5.196152422706632)
    #     self.assertEqual(match.Length(network._netwk, network.GetUser(1), network.GetUser(2), "Sports"), 5.196152422706632 )
    #     database.delete_all_tables()

    # def test_GetDijkstraList(self):
    #     database.make_tables()
    #     network = Network()
    #     match_alg = MatchAlgorithm()
    #     opinion1 = [Opinion("Movies", "Lion King", 5)]
    #     opinion2 = [Opinion("Movies", "Lion King", 6)]
    #     opinion3 = [Opinion("Movies", "Lion King", 0)]
    #     opinion4 = [Opinion("Movies", "Lion King", 7)]
    #     network.AddUser("password", opinion1)
    #     network.AddUser("password", opinion2)
    #     network.AddUser("password", opinion3)
    #     network.AddUser("password", opinion4)
    #     dictionary = match_alg.GetDijkstraList(network._netwk,"Movies", network.GetUser(1))
    #     self.assertEqual((dictionary[network.GetUser(2)]), 1.0)
    #     self.assertEqual((dictionary[network.GetUser(4)]), 2.0)
    #     self.assertEqual((dictionary[network.GetUser(3)]), 5.0)
    #     database.delete_all_tables()
        
    # def test_PotentialMatches(self):
    #     database.make_tables()
    #     network = Network()
    #     match_alg = MatchAlgorithm()
    #     opinion1 = [Opinion("Movies", "Lion King", 10)]
    #     opinion2 = [Opinion("Movies", "Frozen", 6)]
    #     network.AddUser("password", opinion1)
    #     network.AddUser("password", opinion2)
    #     dictionary = match_alg.GetDijkstraList(network._netwk,"Movies", network.GetUser(1))
    #     reccomendation_list = match_alg.GetPotentialMatches(dictionary, network.GetUser(1), "Movies")
    #     self.assertEqual(len(reccomendation_list), 1)
    #     self.assertEqual(reccomendation_list[0], "Frozen" )
    #     database.delete_all_tables()
    #     database.make_tables()
    #     network = Network()
    #     match_alg = MatchAlgorithm()
    #     opinion1 = [Opinion("Movies", "Lion King", 10)]
    #     opinion2 = [Opinion("Movies", "Lion King", 6)]
    #     network.AddUser("password", opinion1)
    #     network.AddUser("password", opinion2)
    #     dictionary = match_alg.GetDijkstraList(network._netwk,"Movies", network.GetUser(1))
    #     reccomendation_list = match_alg.GetPotentialMatches(dictionary, network.GetUser(1), "Movies")
    #     self.assertEqual(len(reccomendation_list), 0)
    #     database.delete_all_tables()


    # def test_GetWeightedDictionary(self):
    #     database.make_tables()
    #     network = Network()
    #     match_alg = MatchAlgorithm()
    #     opinion1 = [Opinion("Movies", "Lion King", 5)]
    #     opinion2 = [Opinion("Movies", "Lion King", 6)]
    #     opinion3 = [Opinion("Movies", "Lion King", 0)]
    #     opinion4 = [Opinion("Movies", "Lion King", 7)]
    #     network.AddUser("password", opinion1)
    #     network.AddUser("password", opinion2)
    #     network.AddUser("password", opinion3)
    #     network.AddUser("password", opinion4)
    #     dictionary = match_alg.GetDijkstraList(network._netwk,"Movies", network.GetUser(1))
    #     weighted_dictionary = match_alg.GetWeightedDict(dictionary)
    #     self.assertEqual(len(weighted_dictionary), 3)
    #     self.assertNotEqual(max(dictionary.values()), 0)
    #     self.assertNotEqual(max(dictionary.values()), 20)
    #     self.assertNotEqual(max(dictionary.values()), 21)
    #     database.delete_all_tables()

    # def test_GetPotentialFriends(self):
    #     database.make_tables()
    #     network = Network()
    #     match_alg = MatchAlgorithm()
    #     opinion1 = [Opinion("Movies", "Lion King", 10)]
    #     opinion2 = [Opinion("Movies", "Frozen", 6)]
    #     network.AddUser("password", opinion1)
    #     empty_dictionary = match_alg.GetDijkstraList(network._netwk,"Movies", network.GetUser(1))
    #     empty_potential_friends_list = match_alg.GetPotentialFriends(empty_dictionary, network.GetUser(1), network._netwk)
    #     self.assertEqual(len(empty_potential_friends_list), 0) 
    #     network.AddUser("password", opinion2)
    #     network.AddUser("password", opinion2)
    #     dictionary = match_alg.GetDijkstraList(network._netwk,"Movies", network.GetUser(1))
    #     potential_friends_list = match_alg.GetPotentialFriends(dictionary, network.GetUser(1), network._netwk)
    #     # Since when a user added, he/she is made friends with a random user, it cannot be precisely predicted, which is a good thing 3)
    #     self.assertLessEqual(len(potential_friends_list), 1) 
    #     database.delete_all_tables()

    def test_GetSumOfDictionary(self):
        database.make_tables()
        network = Network()
        match_alg = MatchAlgorithm()
        opinion1 = [Opinion("Movies", "Lion King", 10)]
        opinion2 = [Opinion("Movies", "Frozen", 6)]
        network.AddUser("password", opinion1)
        network.AddUser("password", opinion2)
        dictionary = match_alg.GetDijkstraList(network._netwk,"Movies", network.GetUser(1))
        weighted_dictionary = match_alg.GetWeightedDict(dictionary)
        reccomendation_list = match_alg.GetPotentialMatches(dictionary, network.GetUser(1), "Movies")
        sum_of_dictionary = match_alg.GetSumDict(weighted_dictionary, reccomendation_list, "Movies")
        self.assertDictEqual(sum_of_dictionary, {'Frozen': [0.0]})
        database.delete_all_tables()
        database.make_tables()
        network = Network()
        match_alg = MatchAlgorithm()
        opinion1 = [Opinion("Movies", "Lion King", 10)]
        opinion2 = [Opinion("Movies", "Lion King", 6)]
        network.AddUser("password", opinion1)
        network.AddUser("password", opinion2)
        dictionary = match_alg.GetDijkstraList(network._netwk,"Movies", network.GetUser(1))
        weighted_dictionary = match_alg.GetWeightedDict(dictionary)
        reccomendation_list = match_alg.GetPotentialMatches(dictionary, network.GetUser(1), "Movies")
        sum_of_dictionary = match_alg.GetSumDict(weighted_dictionary, reccomendation_list, "Movies")
        self.assertDictEqual(sum_of_dictionary, {})
        database.delete_all_tables()


    def test_GetBestMatch(self):
        

        




if __name__ == '__main__':
    unittest.main()
    



