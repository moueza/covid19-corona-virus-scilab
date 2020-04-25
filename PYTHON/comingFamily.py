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
    def inty(self,chnn):
        return int(chnn)
    def coming(self,chnn):
        # """ to list of String
        #print ( self.model ) #parenth oblig
        l=chnn.split()
        return self.intyFunc(l)
    def plus(self,a,b):
        return a+b
    def intyFunc(self,listt):
        #sur list pas array
        mapStructure=map(self.inty,listt)
        return list(mapStructure)
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

lm= ListeMoi()

l2=lm.coming(str)
print("str=",str)
print("str coming=",l2)



chinesComing = lm.coming("""51    52 53
            5 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 """)  # triples guillemets

print("chines=",chinesComing)
     
import numpy as np
arr=np.array(l2)

l2.append(256)
print(l2) #print a variable in a string https://stackoverflow.com/questions/17153779/how-can-i-print-variable-and-string-on-same-line-in-python

chiness=['51', '52', '53', '5', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83']
chinessInt=map(lm.inty,chiness)
print(chinessInt)
addadd=map(lm.plus,[1,2,3],[10,10,10])#conversion to int https://stackoverflow.com/questions/44461551/how-to-print-map-object-with-python-3
print(list(addadd))
def plus2(a,b):
        return a+b

addadd2=map(plus2,[1,2,3],[10,10,10])
print(list(addadd2))