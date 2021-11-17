import unittest
from User import Opinion

class UserTestMethods(unittest.TestCase):   
    def test_private_data_members(self):
        opinion1 = Opinion("Movies", "Frozen", 10)
        self.assertEqual(opinion1.category, "Movies")
        self.assertEqual(opinion1.item, "Frozen")
        self.assertEqual(opinion1.rating, 10)
        with self.assertRaises(ValueError):
            Opinion("Movies", "Frozen", 11)
        with self.assertRaises(ValueError):
            Opinion("Movies", "Frozen", -1)
        with self.assertRaises(ValueError):
            Opinion("Movies", "Frozen", -1)
        with self.assertRaises(Exception):
            Opinion("Banana", "Frozen", 5)


if __name__ == '__main__':
    unittest.main()