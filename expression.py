#!/usr/bin/env python3


import re
from . import test

class expression(object):
    def __init__(self):
        self.__text = False
        self.__match_coin = False
        self.__match_dice = False
        self.__matches_coin = []
        self.__matches_dice =[]
        self.__matches = []
        return;

    def set_text(self, text):
        self.__text = (text.strip()).lower()
        print(self.__text)
        return;

    def get_request(self):
        print(self.__matches)
        if self.__matches == []:
            raise TypeError("set matches first!")
        return self.__matches;

    def validate(self):
        if self.__text == False:
            raise TypeError("set text first!")
        elif self.__text == "":
            raise TypeError("empty string!")
        self.__match_coin = re.search("(([0-9]+) ?)?c(oin(s)?)?( ?w(eight)? ?([0-9]+):([0-9]+)(:([0-9]+))?)?", self.__text)
        self.__match_dice = re.search("(([0-9]+) ?)?d(ice)?( ?([0-9]+)(,([0-9]+),([0-9]+))?)?( ?w(eight)? ?([0-9]+) ([0-9]+):([0-9]+)(:([0-9]+))?)?( ?(\+|\-|\*|\/) ?([0-9]+))?", self.__text)
        print(self.__match_coin)
        print(self.__match_dice)
        return;

    def set_matches(self):
        if self.__match_coin == False or self.__match_dice == False:
            raise TypeError("validate input first!")
        if self.__match_coin is not None:
            iterator = 0
            for item in self.__match_coin.group(2, 7, 8, 10):
                self.__matches_coin.append(item)
                iterator += 1
        if self.__match_dice is not None:
            iterator = 0
            for item in self.__match_dice.group(2, 5, 7, 8, 11, 12, 13, 15, 17, 18):
                self.__matches_dice.append(item)
                iterator += 1
        print(self.__matches_coin)
        print(self.__matches_dice)
        if self.__match_coin is not None and self.__match_dice is not None:
            if len(self.__match_coin.group(0)) <= len(self.__match_dice.group(0)):
                self.__matches = self.__matches_dice
            else:
                self.__matches = self.__matches_coin
        elif self.__match_coin is None:
            self.__matches = self.__matches_dice
        elif self.__match_dice is None:
            self.__matches = self.__matches_coin
        else:
            self.__matches = None
        return;

    def get_message(self, text):
        self.set_text(text)
        try:
            self.validate()
            self.set_matches()
            return self.get_request();
        except TypeError as error:
            print("Error: invalid input, {0}".format(error))
