import unittest
from aging_item import AgingItem


class ItemTest(unittest.TestCase):
    def test_item_init(self):
        item = AgingItem('test', 10, 20)
        self.assertEqual(item.days_left, 10)

    def test_aging_item_update_ok(self):
        item = AgingItem('aging1', 10, 20)
        item.update()
        self.assertEqual(item.days_left, 9)
        self.assertEqual(item.quality, 21)

    def test_aging_item_update_expired(self):
        item = AgingItem('aging2', 0, 20)
        item.update()
        self.assertEqual(item.days_left, 0)
        self.assertEqual(item.quality, 22)

    def test_aging_item_high_quality(self):
        item = AgingItem('test', 0, 49)
        item.update()
        self.assertEqual(item.days_left, 0)
        self.assertEqual(item.quality, 50)


if __name__ == '__main__':
    unittest.main()
