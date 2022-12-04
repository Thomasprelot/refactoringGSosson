import unittest
from store import Store, Item


class StoreTest(unittest.TestCase):
    def testStoreCreation(self):
        items = [Item("item1", 10, 20)]
        store = Store(items)
        self.assertEqual(store.items[0].name, "item1")


if __name__ == '__main__':
    unittest.main()