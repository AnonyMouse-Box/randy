#!/usr/bin/env python3


import random
import test

class coin:
    def __init__(self):
        self.weightHeads = 1
        self.weightTails = 1
        self.clumsy = 0
        return;

    def __setHeads(self, weight):
        self.weightHeads = weight
        return;

    def __setTails(self, weight):
        self.weightTails = weight
        return;

    def __setClumsy(self, weight):
        self.clumsy = weight
        return;

    def __flipCoin(self):
        pseudobool = random.randrange(self.weightHeads + self.weightTails + self.clumsy + 1)
        if pseudobool <= self.weightHeads:
            result = "heads"
        elif pseudobool <= self.weightHeads + self.weightTails:
            result = "tails"
        else:
            result = "lost"
        return result;

    def flipCoins(self, quantity):
        coins = [self.__flipCoin() for a in range(quantity)]
        return coins;

    def weightCoin(self, heads, tails, clumsy):
        self.__setHeads(heads)
        self.__setTails(tails)
        self.__setClumsy(clumsy)
        return;

    def parseCoin(self, times, heads, tails, clumsy):
        times.ifExists(1)
        heads.ifExists(1)
        tails.ifExists(1)
        clumsy.ifExists(0)
        self.weightCoin(heads.value, tails.value, clumsy.value)
        results = self.flipCoins(times.value)
        return results;
