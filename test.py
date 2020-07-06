#!/usr/bin.env python3


class test:
    def __init__(self, value):
        self.value = value
        return;

    def ifExists(self, default):
        if self.value == "" or self.value is None:
            self.value = default
        else:
            self.value = int(self.value)
        return;
