from item.standard_item import StandardItem


class EventItem(StandardItem):
    def __init__(self, name, days_left, quality):
        # test that initial value are valid inputs
        self.name = name
        self.days_left = days_left
        self.quality = quality
        self.default_quality_change = 1
        self.timed_quality = {10: 2, 5: 3}
        self.expired_quality_changed = 0

    def update(self):
        if self.days_left == 0:
            self.quality = 0
            return
        self.days_left -= 1
        increase = self._find_quality_increase()
        self._update_quality(increase)

    def _update_quality(self, increase):
        if self.quality + increase > 50:
            self.quality = 50
        else:
            self.quality += increase

    def _find_quality_increase(self):
        currentPeriod = None
        for period in sorted(self.timed_quality.keys(), reverse=True):
            if self.days_left <= period:
                currentPeriod = period
        if currentPeriod == None:
            return self.default_quality_change
        return self.timed_quality[currentPeriod]
