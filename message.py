#!/usr/bin/env python3


import re

class message(object):
    def __init__(self):
        self.__text = False
        self.__match_coin = False
        self.__match_die = False
        self.__request = False
        return;

    def set_text(self, text):
        self.__text = text.strip()
        return;

    def get_request(self):
        if self.__match_coin == False and self.__match_dice == False:
            raise TypeError("validate input first!")
        return self.__request;

    def validate(self):
        if self.__text == False:
            raise TypeError("set text first!")
        elif self.__text == "":
            raise TypeError("empty string!")
        self.__match_coin = re.search("([0-9]{1,2}|)( |)c(oin(s|)|)( |)(w(eight|)|)( |)([0-9]{1,2}:[0-9]{1,2}(:[0-9]{1,2}|)|)", self.__text)
        self.__match_dice = re.search("([0-9]{1,2}|)( |)d(ice|ie|)( |)([0-9]{1,2}|)( |)(w(eight|)|)( |)([0-9]{1,2}( [0-9]{1,2}:[0-9]{1,2}(:[0-9]{1,2}|)|)|)( |)((\+|\-|\/|\*)[0-9]{1,2}|)", self.__text)
        if self.__match_coin == None and self.__match_dice == None:
            raise TypeError("no match")
        return;

    def set_matches(self):
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