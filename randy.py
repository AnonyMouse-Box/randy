#!/usr/bin/env python3


import random
import re
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

        # put input into lowercase and strip extra whitespace
        text = message['content'].lower()
        text = text.strip()


        # set up regex matches
        match_coin = re.search("([0-9]{1,2}|)( |)c(oin(s|)|)( |)(w(eight|)|)( |)([0-9]{1,2}:[0-9]{1,2}(:[0-9]{1,2}|)|)", text)
        match_dice = re.search("([0-9]{1,2}|)( |)d(ice|ie|)( |)([0-9]{1,2}|)( |)(w(eight|)|)( |)([0-9]{1,2}( [0-9]{1,2}:[0-9]{1,2}(:[0-9]{1,2}|)|)|)( |)((\+|\-|\/|\*)[0-9]{1,2}|)", text)

        # detects coin input
        if match_coin:
            a = coin.coin()
            times = match_coin.group(1)
            if times == "":
                times = 1
            else:
                times = int(times)
            heads = match_coin.group(1)
            tails = match_coin.group(1)
            clumsy = match_coin.group(1)
            print("heads = {0}\ntails = {1}\nclumsy = {2}".format(heads, tails, clumsy))
            results = a.flipCoins(times)
            slug = "You flipped a coin " + str(times) + " times, the result was:\n"

        # detects dice input
        elif match_dice:
            faces = match_dice.group(5)
            if faces == "" or int(faces) < 1:
                faces = 6
            else:
                faces = int(faces)
            a = die.createSimpleDie(faces)
            times = match_dice.group(1)
            if times == "":
                times = 1
            else:
                times = int(times)
            number = match_dice.group(1)
            load = match_dice.group(1)
            rest = match_dice.group(1)
            clumsy = match_dice.group(1)
            operand = match_dice.group(1)
            value = match_dice.group(1)
            print("number = {0}\nload = {1}\nrest = {2}\nclumsy = {3}\noperand = {4}\nvalue = {5}\n".format(number, load, rest, clumsy, operand, value))
            results = a.rollDice(times)
            slug = "You rolled a D" + str(faces) + " " + str(times) + " times, the result was:\n"


        # detects help message
        if "help" in text:
            content =   """
Name: Randy
Synopsis:
{curly braces define optional input}
------------
Coin; @randy {<times> }c{oins weight <heads>:<tails>:<clumsy>}
Examples; long:- `@randy 20 coin weight 20:10:30`, short:- `@randy 20cw2:1:3`
------------
Dice; @randy {<times> }d{ice <faces> weight <number> <load>:<rest>:<clumsy> <operand>}
Examples; long:- `@randy 20 dice 17 weight 15 20:10:30 +89`, short:- `@randy 20d17w15 20:10:30+89`
------------
Times - the number of times the action will be performed, with dice all results will be automatically accumulated and a final result given.
Coin - the command used to define a coin flip.
Dice - the command used to define a dice roll.
Faces - the number of faces you want the die to have.
Weight - the command given to inform that you wish to edit the weightings.
Number - the number on the dice you wish to load. This must be followed by a space and then the ratio else it will default to 2:1.
Heads - the weighting you wish heads to have. Weightings should be from 0 to 99, larger numbers mean it is more likely lower is less likely.
Load - the weighting you wish the load number to have.
Tails - the weighting you wish tails to have.
Rest - the weighting you wish the rest of the numbers to have.
Clumsy - this is a weighting with a default of 0 that allows the potential for the item to be lost during operation.
Operand - this defines an operand  `+`, `-`, `/`, or `*` that you can perform upon the accumulated dice rolls. This is mostly useful for applying buffs or debuffs.
"""

        # prints purpose
        elif "purpose" in text:
            content = "My purpose is as a random item generator, I provide coin flips and dice rolls upon request, try `help` to to learn my commands."

        # responds to null input so you can check it's listening
        elif text == "" or text == "?":
            content = "yes?"

        # catches any other kind of input
        elif results == "":
            content = "I'm sorry what was that? I don't understand.\nType `help` to see the commands I know."

        # parses output in message friendly way
        else:
            content = ""
            for item in results:
                content += ", " + str(item)
            content = content[2:]
            content = slug + content


        # sends completed message and ends
        bot_handler.send_reply(message, content)
        return;

handler_class = Randy
