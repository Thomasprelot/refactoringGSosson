from item.standard_item import StandardItem


class ConjuredItem(StandardItem):
    def __init__(self, name, days_left, quality):
        # test that initial value are valid inputs
        self.name = name
        self.days_left = days_left
        self.quality = quality
        self.default_quality_change = 2
        self.expired_quality_changed = 4
