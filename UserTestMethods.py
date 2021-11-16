import unittest
from User import Opinion, User

class UserTestMethods(unittest.TestCase):
    opinion = Opinion("Movies", "A", 3)

    # Tests whether data members are initialized to the correct values
    def test_data_members(self):
        first_user = User(123)
        self.assertEqual(first_user._userID, 123)
    # Tests whether opinion is correctly added to the User _interests_ dictionary
    def test_add_opinion(self, opinion):
        self.AddOpinion(opinion)
        self.assertEqual(self._interests_[opinion.category][opinion.item], [opinion.rating])
    # Tests if opinion is correctly added to the User _interests_ dictionary
    def test_delete_opinion(self, opinion):
        self.DeleteOpinion(opinion)
        self.assertFalse(self._interests_[opinion.category][opinion.item])


if __name__ == '__main__':
    unittest.main()
