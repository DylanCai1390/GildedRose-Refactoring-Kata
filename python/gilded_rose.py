# -*- coding: utf-8 -*-

# =============================================================================
# Strategy Design Pattern
# =============================================================================
# Each item type has its own "updater" strategy class that encapsulates the
# specific rules for how that item's quality and sell_in values change.
# This makes the code modular, readable, and easy to extend with new item types.
# =============================================================================


class ItemUpdater:
    """Base strategy for normal items.

    Normal items:
    - Quality degrades by 1 each day before the sell date.
    - Quality degrades by 2 each day after the sell date.
    - Quality is never negative.
    - Quality is never more than 50.
    """

    def update(self, item):
        self._update_quality(item)
        self._update_sell_in(item)
        self._clamp_quality(item)

    def _update_quality(self, item):
        item.quality -= 1
        if item.sell_in <= 0:
            item.quality -= 1

    def _update_sell_in(self, item):
        item.sell_in -= 1

    def _clamp_quality(self, item):
        item.quality = max(0, min(50, item.quality))


class AgedBrieUpdater(ItemUpdater):
    """Strategy for Aged Brie.

    Aged Brie increases in Quality the older it gets.
    After the sell date, it increases twice as fast.
    """

    def _update_quality(self, item):
        item.quality += 1
        if item.sell_in <= 0:
            item.quality += 1


class SulfurasUpdater(ItemUpdater):
    """Strategy for Sulfuras, a legendary item.

    Sulfuras never has to be sold and never decreases in Quality.
    Its Quality is always 80.
    """

    def update(self, item):
        pass  # Sulfuras never changes


class BackstagePassUpdater(ItemUpdater):
    """Strategy for Backstage passes.

    - Quality increases by 1 when there are more than 10 days left.
    - Quality increases by 2 when there are 10 days or less.
    - Quality increases by 3 when there are 5 days or less.
    - Quality drops to 0 after the concert (sell_in <= 0).
    """

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
    """Strategy for Conjured items.

    Conjured items degrade in Quality twice as fast as normal items.
    - Quality degrades by 2 each day before the sell date.
    - Quality degrades by 4 each day after the sell date.
    """

    def _update_quality(self, item):
        item.quality -= 2
        if item.sell_in <= 0:
            item.quality -= 2


class GildedRose(object):
    """Main class that uses the Strategy pattern to update item quality.

    The UPDATER_MAP dictionary maps item names to their specific updater
    strategy. If an item name is not found, the default ItemUpdater is used.
    Adding a new item type only requires creating a new updater class and
    adding it to the map - no need to modify existing code (Open/Closed Principle).
    """

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
