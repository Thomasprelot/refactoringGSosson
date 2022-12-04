from standard_item import StandardItem


class SulfurasItem(StandardItem):
    def __init__(self, name, days_left, quality):
        self.name = name
        self.days_left = days_left
        self.quality = quality

    def update(self):
        # no change during update
        pass
