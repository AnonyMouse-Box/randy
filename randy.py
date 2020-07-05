#!/usr/bin/env python3


import re
from . import message
from . import coin
from . import die
from . import test

class Randy(object):
    '''
    This bot generates random coins and dice with biases
    '''

    def usage(self):
        return '''This bot generates random coins and dice with biases'''

    def handle_message(self, message, bot_handler):
        # text = get_message("text", message['content'])
        results = ""

        # put input into lowercase and strip extra whitespace
        text = message['content'].lower()
        text = text.strip()


        # set up regex matches
        match_coin = re.search("([0-9]{1,2}|)( |)c(oin(s|)|)( |)(w(eight|)|)( |)([0-9]{1,2}:[0-9]{1,2}(:[0-9]{1,2}|)|)", text)
        match_dice = re.search("([0-9]{1,2}|)( |)d(ice|ie|)( |)([0-9]{1,2}|)( |)(w(eight|)|)( |)([0-9]{1,2}( [0-9]{1,2}:[0-9]{1,2}(:[0-9]{1,2}|)|)|)( |)((\+|\-|\/|\*)[0-9]{1,2}|)", text)

        # detects coin input
        if match_coin:
            times = test.test(match_coin.group(1))
            heads = test.test(match_coin.group(1))
            tails = test.test(match_coin.group(1))
            clumsy = test.test(match_coin.group(1))
            a = coin.coin()
            print("times = {0}\nheads = {1}\ntails = {2}\nclumsy = {3}".format(times.value, heads.value, tails.value, clumsy.value))
            results = a.parseCoin(times, heads, tails, clumsy)
            slug = "You flipped a coin " + str(times.value) +  " times, the result was:\n"

        # detects dice input
        elif match_dice:
            times = test.test(match_dice.group(1))
            faces = test.test(match_dice.group(5))
            number = test.test(match_dice.group(1))
            load = test.test(match_dice.group(1))
            rest = test.test(match_dice.group(1))
            clumsy = test.test(match_dice.group(1))
            operand = test.test(match_dice.group(1))
            factor = test.test(match_dice.group(1))
            faces.ifExists(6)
            a = die.createSimpleDie(faces.value)
            print("times = {0}\nfaces = {1}\nnumber = {2}\nload = {3}\nrest = {4}\nclumsy = {5}\noperand = {6}\nvalue = {7}\n".format(times.value, faces.value, number.value, load.value, rest.value, clumsy.value, operand.value, factor.value))
            results = a.parseDice(times, faces, number, load, rest, clumsy, operand, factor)
            slug = "You rolled a D" + str(faces.value) + " " + str(times.value) + " times, the result was:\n"


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
