#!/usr/bin/env python3


from . import expression
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
        content = False
        text = message['content']

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
Dice; @randy {<times> }d{ice <faces>,<stop>,<step> weight <number> <load>:<rest>:<clumsy> <operand>}
Examples; long:- `@randy 20 dice 16,24,2 weight 16 20:10:30 +89`, short:- `@randy 20d16,24,2w15 20:10:30+89`
------------
Times - the number of times the action will be performed, with dice all results will be automatically accumulated and a final result given.
Coin - the command used to define a coin flip.
Dice - the command used to define a dice roll.
Faces - the number of faces you want the die to have, becomes dice start value when stop and step are defined, with a default of 1.
Stop - defines what number to stop at when deciding the size of the dice.
Step - defines what the increments on the dice should be.
Weight - the command given to inform that you wish to edit the weightings.
Number - the number on the dice you wish to load. This must be followed by a space and then the ratio else it will default to 2:1.
Heads - the weighting you wish heads to have. Weightings should be integer ratios, larger numbers mean it is more likely lower is less likely.
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
        
        else:
            print(text)
            command = expression.expression()
            matches = command.get_message(text)
            if matches == None:
                matches = []

            # detects coin input
            if len(matches) == 4:
                times = test.test(matches[0])
                heads = test.test(matches[1])
                tails = test.test(matches[2])
                clumsy = test.test(matches[3])
                operand = ""
                item = coin.coin()
                print("times = {0}\nheads = {1}\ntails = {2}\nclumsy = {3}".format(times.value, heads.value, tails.value, clumsy.value))
                results = item.parseCoin(times, heads, tails, clumsy)
                slug = "You flipped a coin " + str(times.value) +  " times, the result was:\n"

            # detects dice input
            elif len(matches) == 10:
                times = test.test(matches[0])
                faces = test.test(matches[1])
                stop = test.test(matches[2])
                step = test.test(matches[3])
                number = test.test(matches[4])
                load = test.test(matches[5])
                rest = test.test(matches[6])
                clumsy = test.test(matches[7])
                operand = matches[8]
                value = test.test(matches[9])
                try:
                    if stop.value == "":
                        faces.ifExists(6)
                        item = die.createSimpleDie(faces.value)
                    else:
                        faces.ifExists(1)
                        stop.ifExists(6)
                        step.ifExists(1)
                        item = die.die(faces.value, stop.value, step.value)
                except TypeError as error:
                    content = error
                else:
                    print("times = {0}\nfaces = {1}\nstop = {2}\nstep = {3}\nnumber = {4}\nload = {5}\nrest = {6}\nclumsy = {7}\noperand = {8}\nvalue = {9}\n".format(times.value, faces.value, stop.value, step.value, number.value, load.value, rest.value, clumsy.value, operand, value.value))
                    results = item.parseDice(times, number, load, rest, clumsy)
                    slug = "You rolled a D" + str(item.faces) + " " + str(times.value) + " times, the result was:\n"

            # catches any other kind of input
            else:
                content = "I'm sorry what was that? I don't understand.\nType `help` to see the commands I know."

            # parses output in message friendly way
            if content == False:
                content = ""
                acc = 0
                for item in results:
                    if isinstance(item, int):
                        acc += item
                    content += ", " + str(item)
                content = content[2:]
                content = slug + content
                if operand is None and len(matches) == 10:
                    content += " = " + str(acc)
                elif operand is not None and len(operand) != 0:
                    value.ifExists(1)
                    try:
                        if operand == "+":
                            acc += value.value
                        elif operand == "-":
                            acc -= value.value
                        elif operand == "*":
                            acc *= value.value
                        elif operand == "/":
                            acc /= value.value
                    except ZeroDivisionError:
                            content = "divide by zero? how dumb do you think I am?!"
                    else:
                        content += " " + operand + " " + str(value.value) + " = " + str(acc)

            # sends completed message and ends
            bot_handler.send_reply(message, content)
            return;

handler_class = Randy
