#!/usr/bin/env python3


import random
from . import test

class die:
    def __init__(self, start, stop, step):
      self.faces = int((stop - start) / step)
      self.weights = {}
      for a in range(start, stop, step):
        self.weights[a] = 1
      self.clumsy = 0
      return;

    def setWeight(self, face, weight):
      self.weights[face] = weight
      return;

    def setClumsy(self, weight):
      self.clumsy = weight
      return;

    def __rollDie(self):
        n = 0
        for a in self.weights.values():
            n += a
        n += self.clumsy
        pseudodie = random.randrange(n + 1)
        valueSum = 0
        for key, value in self.weights.items():
            valueSum += value
            if pseudodie <= valueSum:
                result = key
                break
        return result;

    def rollDice(self, quantity):
        dice = [self.__rollDie() for a in range(quantity)]
        return dice;

    def parseDice(self, times, number, load, rest, clumsy:
        times.ifExists(1)
        number.ifExists(1)
        load.ifExists(1)
        rest.ifExists(1)
        clumsy.ifExists(0)
        for face in self.weights:
            self.setWeight(face, rest.value)
        self.setWeight(number.value, load.value)
        self.setClumsy(clumsy.value)
        results = self.rollDice(times.value)
        return results;

def createSimpleDie(sides):
    return die(1, sides + 1, 1);
