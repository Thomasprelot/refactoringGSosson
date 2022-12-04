import unittest
from store import Store
from item import Item


class StoreTest(unittest.TestCase):
    def test_store_init(self):
        items = [Item("item1", 10, 20)]
        store = Store(items)
        self.assertEqual(store.items[0].name, "item1")

    def test_update_items(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        store = Store(items)
        store.update_items()
        self.assertEqual(store.items[0].days_left, 4)
        self.assertEqual(store.items[0].quality, 6)


if __name__ == '__main__':
    unittest.main()
