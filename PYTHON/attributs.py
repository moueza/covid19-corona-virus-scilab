# python3
# exec(open('time_series_covid19_confirmed_global.py').read())


import numpy as np
import csv
import matplotlib.pyplot as plt
from comingFamily import *


class Attributs:
    def __init__(self, natureOfMaladd):
        self.nature = natureOfMaladd
    # model poub

    def printModel(self):
        print (self.model)  # parenth oblig

    # set no index
    ages = {2, 5}
    print("age in class=", ages)
    listIndex = [2, 5]

    def nulle(self):
        pass  # vital


natureAnalyzed = Attributs("../time_series_covid19_confirmed_global.csv")

print("ages=", natureAnalyzed.ages)

natureAnalyzed.nulle()
