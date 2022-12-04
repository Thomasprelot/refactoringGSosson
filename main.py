# -*- coding: utf-8 -*-

from gilded_rose import Item, GildedRose

class Rose():
  def foo(self):
    items = [Item("+5 Dexterity Vest", 10, 20),   
             Item("Aged Brie", 2, 0), 
             Item("Elixir of the Mongoose", 5, 7),
             Item("Sulfuras, Hand of Ragnaros", 0, 80),
             Item("Sulfuras, Hand of Ragnaros", -1, 80),
             Item("Backstage passes to a TAFKAL80ETC concert", 15, 20), 
             Item("Backstage passes to a TAFKAL80ETC concert", 10, 49), 
             Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            # this conjured item does not work properly yet
             Item("Conjured Mana Cake", 3, 6)]
  
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "+5 Dexterity Vest"
    print('ok')  

if __name__ == '__main__':
  gildedRose = Rose()
  gildedRose.foo()