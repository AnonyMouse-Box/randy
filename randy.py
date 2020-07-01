#!/usr/bin/env python3


import random
from . import coin
from . import die

class Randy(object):
    '''
    This bot generates random coins and dice with biases
    '''

    def usage(self):
        return '''This bot generates random coins and dice with biases'''

    def handle_message(self, message, bot_handler):
        results = ""

        if message['content'] == "coin":
            a = coin.coin()
            results = a.flipCoins(1)
        elif message['content'] == "dice":
            a = die.createSimpleDie(6)
            results = a.rollDice(1)

        if message['content'] == "help":
            content = "type `coin` for a coin flip or `dice` for a dice roll"
        elif results == "":
            content = "yes?"
        else:
            content = ""
            for item in results:
                content += ", " + str(item)
            content = content[2:]

        bot_handler.send_reply(message, content)
        return;

handler_class = Randy
