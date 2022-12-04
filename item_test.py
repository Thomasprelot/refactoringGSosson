import unittest
from gilded_rose import Item


class ItemTest(unittest.TestCase):
    def testItemCreation(self):
        item = Item('test', 10, 20)
        self.assertEqual(item.days_left, 10)


if __name__ == '__main__':
    unittest.main()
