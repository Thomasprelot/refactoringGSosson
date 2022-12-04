# -*- coding: utf-8 -*-

from standard_item import StandardItem
from store import Store


class Rose():
    def foo(self):
        items = [
            StandardItem("+5 Dexterity Vest", 10, 20),
            StandardItem("Aged Brie", 2, 0),
            StandardItem("Elixir of the Mongoose", 5, 7),
            StandardItem("Sulfuras, Hand of Ragnaros", 0, 80),
            StandardItem("Sulfuras, Hand of Ragnaros", -1, 80),
            StandardItem("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            StandardItem("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            StandardItem("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            # this conjured item does not work properly yet
            StandardItem("Conjured Mana Cake", 3, 6)
        ]

        gilded_rose = Store(items)
        gilded_rose.update_items()
        assert items[0].name == "+5 Dexterity Vest"
        print('ok')


if __name__ == '__main__':
    gildedRose = Rose()
    gildedRose.foo()
