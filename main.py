# -*- coding: utf-8 -*-

from item.standard_item import StandardItem
from item.aging_item import AgingItem
from item.sulfuras_item import SulfurasItem
from item.event_item import EventItem
from item.conjured_item import ConjuredItem
from store import Store


class GildedRoseStore():
    def open_store(self):
        items = [
            StandardItem("+5 Dexterity Vest", 10, 20),
            AgingItem("Aged Brie", 2, 0),
            StandardItem("Elixir of the Mongoose", 5, 7),
            SulfurasItem("Sulfuras, Hand of Ragnaros", 0, 80),
            SulfurasItem("Sulfuras, Hand of Ragnaros", -1, 80),
            EventItem("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            EventItem("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            EventItem("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            # this conjured item does not work properly yet
            ConjuredItem("Conjured Mana Cake", 3, 6)
        ]

        self.store = Store(items)
        self.pass_day()

    def pass_day(self):
        self.store.update_items()
        print("It's a new day")


if __name__ == '__main__':
    gildedRose = GildedRoseStore()
    gildedRose.open_store()
