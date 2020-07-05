#!/usr/bin/env python3


import re
from . import test

class message(object):
    def __init__(self):
        self.__text = False
        self.__match_coin = False
        self.__match_die = False
        self.__matches = []
        return;

    def set_text(self, text):
        self.__text = (text.strip()).lower
        return;

    def get_request(self):
        if self.__matches = []:
            raise TypeError("set matches first!")
        return self.__matches;

    def validate(self):
        if self.__text == False:
            raise TypeError("set text first!")
        elif self.__text == "":
            raise TypeError("empty string!")
        self.__match_coin = re.search("([0-9]+|)( |)c(oin(s|)|)( |)(w(eight|)|)( |)(([0-9]+):([0-9]+)(:([0-9]+)|)|)", self.__text)
        self.__match_dice = re.search("([0-9]+|)( |)d(ice|ie|)( |)([0-9]+|)( |)(w(eight|)|)( |)(([0-9]+)( ([0-9]+):([0-9]+)(:([0-9]+)|)|)|)( |)((\+|\-|\/|\*)([0-9]+)|)", self.__text)
        return;

    def set_matches(self):
        if self.__match_coin == False and self.__match_dice == False:
            raise TypeError("validate input first!")
        elif self.__match_coin != None:
            self.__matches[0] = test.test(match_coin.group(1))
            self.__matches[1] = test.test(match_coin.group(10))
            self.__matches[2] = test.test(match_coin.group(11))
            self.__matches[3] = test.test(match_coin.group(13))
        elif self.__match_die != None:
            self.__matches[0] = test.test(match_dice.group(1))
            self.__matches[1] = test.test(match_dice.group(5))
            self.__matches[2] = test.test(match_dice.group(11))
            self.__matches[3] = test.test(match_dice.group(13))
            self.__matches[4] = test.test(match_dice.group(14))
            self.__matches[5] = test.test(match_dice.group(16))
            self.__matches[6] = test.test(match_dice.group(19))
            self.__matches[7] = test.test(match_dice.group(20))
        else:
            raise TypeError("no match!")
        return;

def get_message(name, text):
    name = message()
    name.set_text(text)
    try:
        name.validate()
        name.set_matches()
        return name.get_request();
    except TypeError as error:
        print("Error: invalid input, {0}".format(error))