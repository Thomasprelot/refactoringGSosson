# -*- coding: utf-8 -*-
class Store(object):
    """
      A store contains many items
    """
    def __init__(self, items):
        self.items = items

    def update_items(self):
        for item in self.items:
            item.update()
