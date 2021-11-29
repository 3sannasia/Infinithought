import unittest
from User import Opinion, User

class UserTestMethods(unittest.TestCase):

    # Tests whether data members are initialized to the correct values
    def test_data_members(self):
        first_user = User(123)
        self.assertEqual(first_user._userId, 123)
    # Tests whether opinion is correctly added to the User _interests_ dictionary
    def test_add_opinion(self):
        first_user = User(123)
        opinion = Opinion("Movies", "Frozen", 10)
        first_user.AddOpinion(opinion)
        self.assertEqual(first_user._interests_[opinion.category][opinion.item], [opinion.rating])
    # Tests if opinion is correctly added to the User _interests_ dictionary
    def test_delete_opinion(self):
        first_user = User(123)
        opinion = Opinion("Movies", "Frozen", 10)
        first_user.AddOpinion(opinion)
        first_user.DeleteOpinion(opinion)
        with self.assertRaises(KeyError):
            first_user._interests_[opinion.category][opinion.item]


if __name__ == '__main__':
    unittest.main()
