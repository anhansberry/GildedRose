# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_Aged_Brie(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)
        self.assertEquals(1, items[0].sell_in)
    
    def test_Sulfuras(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)
        self.assertEquals(0, items[0].sell_in)


        
if __name__ == '__main__':
    unittest.main()