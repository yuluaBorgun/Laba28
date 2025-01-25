import unittest
from Main import *

class TestFlowerShop(unittest.TestCase):

    def setUp(self):
        self.flower = Flower("Роза", 100, 10)
        add_flower("Роза", 100, 10)

    def test_add_flower(self):
        self.assertEqual(len(flowers), 1)

    def test_update_flower(self):
        update_flower("Роза", price=120)
        self.assertEqual(flowers[0].price, 120)

    def test_delete_flower(self):
        delete_flower("Роза")
        self.assertEqual(len(flowers), 0)

if __name__ == '__main__':
    unittest.main()