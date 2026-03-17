# -*- coding: utf-8 -*-


class ItemUpdater:
    def update(self, item):
        self._update_quality(item)
        self._update_sell_in(item)
        item.quality = max(0, min(50, item.quality))

    def _update_quality(self, item):
        item.quality -= 1
        if item.sell_in <= 0:
            item.quality -= 1

    def _update_sell_in(self, item):
        item.sell_in -= 1


class AgedBrieUpdater(ItemUpdater):
    def _update_quality(self, item):
        item.quality += 1
        if item.sell_in <= 0:
            item.quality += 1


class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass


class BackstagePassUpdater(ItemUpdater):
    def _update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = 0
            return
        item.quality += 1
        if item.sell_in <= 10:
            item.quality += 1
        if item.sell_in <= 5:
            item.quality += 1


class ConjuredUpdater(ItemUpdater):
    def _update_quality(self, item):
        item.quality -= 2
        if item.sell_in <= 0:
            item.quality -= 2


class GildedRose(object):

    UPDATER_MAP = {
        "Aged Brie": AgedBrieUpdater(),
        "Sulfuras, Hand of Ragnaros": SulfurasUpdater(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater(),
        "Conjured Mana Cake": ConjuredUpdater(),
    }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = self.UPDATER_MAP.get(item.name, ItemUpdater())
            updater.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
