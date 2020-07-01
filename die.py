#!/usr/bin/env python3


import random

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

def createSimpleDie(sides):
    return die(1, sides + 1, 1);
