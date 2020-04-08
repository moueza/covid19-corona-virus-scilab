
#file mag Login pratique blanc no 10 p23 :
#                                 classes p14
#         filtres listes p18
#         slice p19
#         operateurs
#         p20 wxpython p24
#         editeur p30 nav p32 reseau p36 threads p38
#                                sexe boobs tits p24, p26, p31
#                                svg graph XML p40
#                                recherches Google p52
#                                SOAP LDAP p54
#                                Gmail p56
#                                Zope ( Plone ) server p64
#                                modeles p76 bookmarks p78
#mag Linux magazine no 49H jaune :
#                                slots p18
#decorateurs p20 memoized cache
#                                pip + virtual env +h versions p26 (cf repo Kubernetes Python)
#                                Redis p32
#                                chaines listes 34 sort lrange
#                                ens p37
#                                cookies p42
#                                Nginx p43
####                             schedulers 48 brokers 49 git 59
##mag Linux France bleu no 40H :
#                                p13 append [112]
#                                p16 fortran g95 heritage de classe
#                                p19 // parallelisme
import numpy as np
import csv

#set no index
ages = { 2 , 5 }
listIndex =[ 2 , 5 ]
#print(listIndex[1]) OK
#https://realpython.com/python-csv/#reading-csv-files-with-csv

with open('../time_series_covid19_deaths_global.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    #print(f'longh = {line_count.length}')
    #print(f'longh = {len(line_count)}') KO
    #print(len(csv_reader)) KO
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html
    #matt = np.matrix('1 2; 3 4')
    matt = np.matrix('')
    arrayMoi = []
    for roww in csv_reader:
      if line_count != 0:
          print(f'\t {line_count} {roww[1]} {int(roww[4]) + 1000}')
          #https://docs.scipy.org/doc/numpy/reference/generated/numpy.column_stack.html
          #matt=np.column_stack((matt,roww))
          #https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array
          #arrayMoi[0]=roww
          #[112]
          arrayMoi.append( roww)
      line_count += 1
         #print(f'\t{roww[1]}')
         #if line_count == 0:
         #    print(f'Column names are {", ".join(row)}')
         #    line_count += 1
         #else:
         #    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        #    line_count += 1
	#line[1]=row
        #print(f'\t {ages[1]}') TypeError: 'set' object does not support indexing
        #print(ages) OK
         
        #print(f'\t {line_count} {roww[1]} {int(roww[4]) + 1000}')
      
    #print(f'Processed {line_count} lines.')
    print(arrayMoi[0])
    print('\nlbl45')
    print(arrayMoi)
    print('\nlbl50')
    #print(arrayMoi[:][4:]
    arrayMoiArray=np.asarray(arrayMoi)
    arrayMoiMatrix=np.matrix(arrayMoi)
#TODO convert to np.array https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array
    subArray=arrayMoiArray[0:1000][4:1000] #KO
    subMatrix=arrayMoiMatrix[0:1000][4:1000]# KO rien

    #subArray2
    subMatrix2=arrayMoiMatrix[:,4:]
    
    subArray.flatten()
    subMatrix.flatten()

    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html
    def myfunc(x):
        "Return a-b if a>b, otherwise return a+b"
        return int(x)
    vfunc = np.vectorize(myfunc)
 
    #vfunc(subArray, 2)
    #vfunc(subArray) #KO rien finalement
    #vfunc(subMatrix, 2)
    #vfunc(subMatrix) #KO rien finalement
    subMatInt2=vfunc(subMatrix2)
    
    #affich array en ligne
    a = np.array([[ 0,  1,  2,  3], [10, 11, 12, 13],[20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]])
    # a[:][1]KO
    m=np.matrix(a)
    #TODO col des 4 par append
