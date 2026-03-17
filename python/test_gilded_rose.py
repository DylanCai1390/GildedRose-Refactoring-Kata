# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # =========================================================================
    # 4 Failing Tests for "Conjured" items (these fail with the ORIGINAL code)
    # =========================================================================
    # Requirement: "Conjured" items degrade in Quality twice as fast as
    # normal items.
    # - Before sell date: quality decreases by 2 per day (normal = 1)
    # - After sell date:  quality decreases by 4 per day (normal = 2)
    # =========================================================================

    def test_conjured_before_sell_date(self):
        """Conjured item quality degrades by 2 before the sell date."""
        items = [Item("Conjured Mana Cake", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 18)  # 20 - 2 = 18
        self.assertEqual(items[0].sell_in, 9)

    def test_conjured_after_sell_date(self):
        """Conjured item quality degrades by 4 after the sell date."""
        items = [Item("Conjured Mana Cake", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 16)  # 20 - 4 = 16
        self.assertEqual(items[0].sell_in, -1)

    def test_conjured_quality_never_negative(self):
        """Conjured item quality does not go below 0."""
        items = [Item("Conjured Mana Cake", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)  # would be 3 - 4 = -1, but clamped to 0

    def test_conjured_multiple_days(self):
        """Conjured item quality degrades correctly over multiple days."""
        items = [Item("Conjured Mana Cake", 3, 20)]
        gilded_rose = GildedRose(items)
        # Day 1: sell_in=3 > 0, quality = 20 - 2 = 18, sell_in -> 2
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 18)
        # Day 2: sell_in=2 > 0, quality = 18 - 2 = 16, sell_in -> 1
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 16)
        # Day 3: sell_in=1 > 0, quality = 16 - 2 = 14, sell_in -> 0
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 14)
        # Day 4: sell_in=0, quality = 14 - 4 = 10, sell_in -> -1
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 10)

    # =========================================================================
    # Additional tests to ensure existing items still work correctly
    # =========================================================================

    def test_normal_item_before_sell_date(self):
        """Normal item quality degrades by 1 before the sell date."""
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_normal_item_after_sell_date(self):
        """Normal item quality degrades by 2 after the sell date."""
        items = [Item("+5 Dexterity Vest", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)
        self.assertEqual(items[0].sell_in, -1)

    def test_normal_item_quality_never_negative(self):
        """Normal item quality never goes below 0."""
        items = [Item("Elixir of the Mongoose", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_increases_quality(self):
        """Aged Brie increases in quality over time."""
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)
        self.assertEqual(items[0].sell_in, 4)

    def test_aged_brie_after_sell_date(self):
        """Aged Brie increases in quality twice as fast after sell date."""
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)

    def test_aged_brie_quality_max_50(self):
        """Aged Brie quality never exceeds 50."""
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_sulfuras_never_changes(self):
        """Sulfuras quality and sell_in never change."""
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_backstage_pass_more_than_10_days(self):
        """Backstage pass increases quality by 1 when more than 10 days."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_backstage_pass_10_days_or_less(self):
        """Backstage pass increases quality by 2 when 10 days or less."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_backstage_pass_5_days_or_less(self):
        """Backstage pass increases quality by 3 when 5 days or less."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 23)

    def test_backstage_pass_after_concert(self):
        """Backstage pass quality drops to 0 after the concert."""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)


if __name__ == '__main__':
    unittest.main()
