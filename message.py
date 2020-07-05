#!/usr/bin/env python3


import re

class message(object):
    def __init__(self):
        self.__text = False
        self.__match = False
        self.__request = False
        return;

    def set_text(self, text):
        self.__text = text.strip()
        return;

    def get_request(self):
        if self.__request == False:
            raise TypeError("validate input first!")
        return self.__request;

    def validate(self):
        if self.__text == False:
            raise TypeError("set text first!")
        elif self.__text == "":
            raise TypeError("empty string!")
        self.__match = re.match("^([0-9]{1,})$", self.__text)
        if self.__match == None:
            raise TypeError("not an integer")
        self.__request = int(self.__match.group(1))
        return;

def get_message(name, text):
    name = message()
    name.set_text(text)
    try:
        name.validate()
        return name.get_request();
    except TypeError as error:
        print("Error: invalid input, {0}".format(error))