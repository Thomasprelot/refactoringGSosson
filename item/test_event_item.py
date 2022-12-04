import unittest
from event_item import EventItem


class ItemTest(unittest.TestCase):
    def test_item_init(self):
        item = EventItem('test', 10, 20)
        self.assertEqual(item.days_left, 10)

    def test_find_quality_increase(self):
        item = EventItem('test', 3, 20)
        self.assertEqual(item._find_quality_increase(), item.timed_quality[5])

    def test_event_item_update_many_days(self):
        item = EventItem('event1', 15, 20)
        item.update()
        self.assertEqual(item.days_left, 14)
        self.assertEqual(item.quality, 21)

    def test_event_item_update_expired(self):
        item = EventItem('event2', 0, 20)
        item.update()
        self.assertEqual(item.days_left, 0)
        self.assertEqual(item.quality, 0)

    def test_event_item_few_days(self):
        item = EventItem('event3', 9, 10)
        item.update()
        self.assertEqual(item.days_left, 8)
        self.assertEqual(item.quality, 12)


if __name__ == '__main__':
    unittest.main()
