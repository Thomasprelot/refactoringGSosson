from item.standard_item import StandardItem


class SulfurasItem(StandardItem):
    """
      SulfurasItems quality is never changing
    """
    def __init__(self, name, days_left, quality):
        self.name = name
        self.days_left = days_left
        self.quality = quality

    def update(self):
        if self.days_left > 0:
            self.days_left -= 1
