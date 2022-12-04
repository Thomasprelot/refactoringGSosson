import unittest
from conjured_item import ConjuredItem


class ConjuredItemTest(unittest.TestCase):
    def test_item_init(self):
        item = ConjuredItem('test', 10, 20)
        self.assertEqual(item.days_left, 10)

    def test_standard_item_update_ok(self):
        item = ConjuredItem('test', 10, 20)
        item.update()
        self.assertEqual(item.days_left, 9)
        self.assertEqual(item.quality, 18)

    def test_standard_item_update_expired(self):
        item = ConjuredItem('test', 0, 20)
        item.update()
        self.assertEqual(item.days_left, 0)
        self.assertEqual(item.quality, 16)

    def test_standard_item_low_quality(self):
        item = ConjuredItem('test', 0, 1)
        item.update()
        self.assertEqual(item.days_left, 0)
        self.assertEqual(item.quality, 0)


if __name__ == '__main__':
    unittest.main()
