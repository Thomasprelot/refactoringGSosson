class StandardItem:
    def __init__(self, name, days_left, quality):
        # test that initial value are valid inputs
        self.name = name
        self.days_left = days_left
        self.quality = quality
        self.default_quality_change = 1
        self.expired_quality_change = 2

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.days_left, self.quality)

    def update(self):
        if self.days_left == 0:
            self._update_quality(self.expired_quality_change)
            return
        self.days_left -= 1
        self._update_quality(self.default_quality_change)

    def _update_quality(self, decrease):
        if self.quality < decrease:
            self.quality = 0
        else:
            self.quality -= decrease

    def update_global(self):
        if self.name != "Aged Brie" and self.name != "Backstage passes to a TAFKAL80ETC concert":
            if self.quality > 0:
                if self.name != "Sulfuras, Hand of Ragnaros":
                    self.quality = self.quality - 1
        else:
            if self.quality < 50:
                self.quality = self.quality + 1
                if self.name == "Backstage passes to a TAFKAL80ETC concert":
                    if self.days_left < 11:
                        if self.quality < 50:
                            self.quality = self.quality + 1
                    if self.days_left < 6:
                        if self.quality < 50:
                            self.quality = self.quality + 1
        if self.name != "Sulfuras, Hand of Ragnaros":
            self.days_left = self.days_left - 1
        if self.days_left < 0:
            if self.name != "Aged Brie":
                if self.name != "Backstage passes to a TAFKAL80ETC concert":
                    if self.quality > 0:
                        if self.name != "Sulfuras, Hand of Ragnaros":
                            self.quality = self.quality - 1
                else:
                    self.quality = self.quality - self.quality
            else:
                if self.quality < 50:
                    self.quality = self.quality + 1
