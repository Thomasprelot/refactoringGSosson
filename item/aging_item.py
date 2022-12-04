from item.standard_item import StandardItem


class AgingItem(StandardItem):
    """
      AgingItems quality increases over time, up to a maximum of 50
    """
    def __init__(self, name, days_left, quality):
        # test that initial value are valid inputs
        self.name = name
        self.days_left = days_left
        self.quality = quality
        self.default_quality_change = 1
        self.expired_quality_change = 2

    def update(self):
        if self.days_left == 0:
            self._update_quality(self.expired_quality_change)
            return
        self.days_left -= 1
        self._update_quality(self.default_quality_change)

    def _update_quality(self, increase):
        if self.quality + increase > 50:
            self.quality = 50
        else:
            self.quality += increase
