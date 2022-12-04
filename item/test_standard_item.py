import unittest
from standard_item import StandardItem


class StandardItemTest(unittest.TestCase):
    def test_item_init(self):
        item = StandardItem('test', 10, 20)
        self.assertEqual(item.days_left, 10)

    def test_item_creation_error(self):
        #test with negative quality or days left
        pass

    def test_standard_item_update_ok(self):
        item = StandardItem('test', 10, 20)
        item.update()
        self.assertEqual(item.days_left, 9)
        self.assertEqual(item.quality, 19)

    def test_standard_item_update_expired(self):
        item = StandardItem('test', 0, 20)
        item.update()
        self.assertEqual(item.days_left, 0)
        self.assertEqual(item.quality, 18)

    def test_standard_item_low_quality(self):
        item = StandardItem('test', 0, 1)
        item.update()
        self.assertEqual(item.days_left, 0)
        self.assertEqual(item.quality, 0)


if __name__ == '__main__':
    unittest.main()
