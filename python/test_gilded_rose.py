# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # conjured item tests

    def test_conjured_before_sell_date(self):
        items = [Item("Conjured Mana Cake", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 18)
        self.assertEqual(items[0].sell_in, 9)

    def test_conjured_after_sell_date(self):
        items = [Item("Conjured Mana Cake", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 16)
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_quality_never_negative(self):
        items = [Item("Conjured Mana Cake", 0, 3)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_multiple_days(self):
        items = [Item("Conjured Mana Cake", 3, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 18)
        gr.update_quality()
        self.assertEqual(items[0].quality, 16)
        gr.update_quality()
        self.assertEqual(items[0].quality, 14)
        gr.update_quality()
        self.assertEqual(items[0].quality, 10)

    # normal item tests

    def test_normal_item_before_sell_date(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_normal_item_after_sell_date(self):
        items = [Item("+5 Dexterity Vest", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 8)

    def test_normal_item_quality_never_negative(self):
        items = [Item("Elixir of the Mongoose", 5, 0)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)

    # aged brie tests

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 5, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 11)

    def test_aged_brie_after_sell_date(self):
        items = [Item("Aged Brie", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 12)

    def test_aged_brie_quality_max_50(self):
        items = [Item("Aged Brie", 5, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 50)

    # sulfuras tests

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    # backstage pass tests

    def test_backstage_pass_more_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_backstage_pass_10_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_backstage_pass_5_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 23)

    def test_backstage_pass_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)


if __name__ == '__main__':
    unittest.main()
