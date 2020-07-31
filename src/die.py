#!/usr/bin/env python3


import random
import test

class die:
    def __init__(self, start, stop, step):
      if stop < start:
          raise TypeError("stop less than start? what're you trying to do? make an anti-dice?! XD")
      if (stop - start) % step != 0:
          raise TypeError ("hey dufus! might wanna check your math, that ain't a valid dice.")
      self.faces = int((stop + 1 - start) / step)
      self.weights = {}
      for a in range(start, stop + 1, step):
        self.weights[a] = 1
      self.clumsy = 0
      return;

    def setWeight(self, face, weight):
      if face not in self.weights.keys():
          raise TypeError ("yo genius, that number isn't on the dice, get a clue!")
      self.weights[face] = weight
      return;

    def setClumsy(self, weight):
      self.clumsy = weight
      return;

    def __rollDie(self):
        n = 1
        for a in self.weights.values():
            n += a
        n += self.clumsy
        pseudodie = random.randrange(n)
        valueSum = 0
        result = "lost"
        for key, value in self.weights.items():
            valueSum += value
            if pseudodie <= valueSum:
                result = key
                break
        return result;

    def rollDice(self, quantity):
        dice = [self.__rollDie() for a in range(quantity)]
        return dice;

    def parseDice(self, times, start, number, load, rest, clumsy):
        times.ifExists(1)
        number.ifExists(start.value)
        load.ifExists(1)
        rest.ifExists(1)
        clumsy.ifExists(0)
        for face in self.weights.keys():
            self.setWeight(face, rest.value)
        self.setWeight(number.value, load.value)
        self.setClumsy(clumsy.value)
        results = self.rollDice(times.value)
        return results;

def createSimpleDie(sides):
    return die(1, sides, 1);
