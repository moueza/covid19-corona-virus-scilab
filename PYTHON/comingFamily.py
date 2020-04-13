#python3
#exec(open('comingFamily.py').read())
#doc https://docs.python.org/3.6/tutorial/classes.html
class Voiture:
    def __init__(self):
        self.model = "406"
    def printModel(self):
        print ( self.model ) #parenth oblig

class ListeMoi:
    #def __init__(self, listeStringuee):
        #self.chn = listeStringuee

    def __init__(self):
         pass  #nul block
        
    def coming(self,chnn):
        #print ( self.model ) #parenth oblig
        return chnn.split()
    
v = Voiture()
v.printModel()
v.model = "306"
v.printModel()


str= """15
30    28  100"""
#:[1]
print(str.split())  #space KO
l=[1,2,3]
#print l.append(10) KO
l

lm= ListeMoi();

l2=lm.coming(str)

import numpy as np
arr=np.array(l2)

l2.append(256)
print(l2) #print a variable in a string https://stackoverflow.com/questions/17153779/how-can-i-print-variable-and-string-on-same-line-in-python


