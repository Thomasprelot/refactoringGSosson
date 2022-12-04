import unittest
from sulfuras_item import SulfurasItem


class ItemTest(unittest.TestCase):
    def test_item_init(self):
        item = SulfurasItem("Sulfuras test", -1, 20)
        self.assertEqual(item.name, "Sulfuras test")

    def test_sulfuras_item_update_ok(self):
        item = SulfurasItem('Sulfuras', 10, 20)
        item.update()
        self.assertEqual(item.days_left, 10)
        self.assertEqual(item.quality, 20)


if __name__ == '__main__':
    unittest.main()
