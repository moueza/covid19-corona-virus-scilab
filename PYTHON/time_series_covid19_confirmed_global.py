# python3
#exec(open('time_series_covid19_confirmed_global.py').read())


# *file mag Login pratique blanc no 10 [1] p23 :
#                                 classes p14
#                                 p08 IDLE IDE!
#                                 p09 guillemets triples
#                                 p10 modules import polymorphisme  RPN ie prefixe calculatrice
#                                 p11 upper
#                                 p12 listes piles fonctions
#                                 p13 tokens
#                                 p15  PlusOperator
#                                 p16 ie infixe
#                                 p17 strip split lambda
#         p18 filtres listes map regexp (ie strings)
#         p19 slice  surcharge d operateur
#         p20 operateurs  nombres complexes  surcharge
#         p24 wxpython
#         editeur p30 nav p32 reseau p36 threads p38
#                                sexe boobs tits p24, p26, p31
#                                svg graph XML p40
#                                p43 svg
#                                recherches Google p52
#                                SOAP LDAP p54
#                                Gmail p56
#                                p58 MySQL database

#                                Zope ( Plone ) server p64
#                                modeles p76 bookmarks p78
# *mag Linux magazine no 49H jaune [2]:
#                                p05 unit tests
#                                p12 objets dyn
#                                p18 slots metaclass
#                                p20 decorators annotations  functions
#                                p23 virtualenv
#                                p70 tracked

#                                p74 planets  collision
# decorateurs p20 memoized cache
#                                pip + virtual env +h versions p26 (cf repo Kubernetes Python)
#                                Redis p32
#                                chaines listes 34 sort lrange
#                                ens p37
#                                cookies p42
#                                Nginx p43
#                                schedulers 48 brokers 49 git 59
# *mag Linux France bleu no 40H [3]:
#                                p13 append [112]
#                                p16 fortran g95 heritage de classe
#                                p17 map decorators closures
#                                p19 // parallelisme
#                                p22 map
#                                p31 p32 ITK VTK
#                                p54 packager et diffuser son application
#                                p62 Decorateurs annotations
#                                p65 3D imaging (jpg,) DOM XML
#                                p69 Zope adaptateurs
#                                p70 interfaces
# [4]   https://cs231n.github.io/python-numpy-tutorial/ replace append pop enumerate

import numpy as np
import csv
import matplotlib.pyplot as plt
from comingFamily import *


class MaladType:
    def __init__(self, natureOfMaladdPrefix):
        #radical of prefix suffix
        self.nature = natureOfMaladdPrefix
    # model poub

    def printModel(self):
        print (self.model)  # parenth oblig

    def main(self):
        # set no index
        ages = {2, 5}
        listIndex = [2, 5]
        # print(listIndex[1]) OK
        # https://realpython.com/python-csv/#reading-csv-files-with-csv

        # with open('../time_series_covid19_deaths_global.csv') as csv_fileDeath:
        #with open('../time_series_covid19_confirmed_global.csv') as csv_fileConfirmed:
        with open('../'+self.nature+'.csv') as csv_fileConfirmed:
            csv_reader = csv.reader(csv_fileConfirmed, delimiter=',')
            line_count = 0
            # print(f'longh = {line_count.length}')
            # print(f'longh = {len(line_count)}') KO
            # print(len(csv_reader)) KO
            # https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html
            #matt = np.matrix('1 2; 3 4')
            matt = np.matrix('')
            arrayMoi = []
            for roww in csv_reader:
                if line_count != 0:
                    print(f'\t {line_count} {roww[1]} {int(roww[4]) + 1000}')
                    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.column_stack.html
                    # matt=np.column_stack((matt,roww))
                    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array
                    # arrayMoi[0]=roww
                    # [112]
                    arrayMoi.append(roww)
                line_count += 1
                # print(f'\t{roww[1]}')
                # if line_count == 0:
                #    print(f'Column names are {", ".join(row)}')
                #    line_count += 1
                # else:
                #    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                #    line_count += 1
                # line[1]=row
                # print(f'\t {ages[1]}') TypeError: 'set' object does not support indexing
                # print(ages) OK

                # print(f'\t {line_count} {roww[1]} {int(roww[4]) + 1000}')

        # print(f'Processed {line_count} lines.')
        # print(arrayMoi[0])
        print('\nlbl45')
        print("arrayMoi=", arrayMoi)
        print('\nlbl50')
        # print(arrayMoi[:][4:]
        arrayMoiArray = np.asarray(arrayMoi)
        arrayMoiMatrix = np.matrix(arrayMoi)
        # TODO convert to np.array https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array
        subArray = arrayMoiArray[0:1000][4:1000]  # KO
        subMatrix = arrayMoiMatrix[0:1000][4:1000]  # KO rien

        # subArray2
        subMatrix2 = arrayMoiMatrix[1:, 4:]
        # subArray.flatten()
        # subMatrix.flatten()

        # https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html
        def myfunc(x):
            "Return a-b if a>b, otherwise return a+b"
            return int(x)
        vfunc = np.vectorize(myfunc)

        #vfunc(subArray, 2)
        # vfunc(subArray) #KO rien finalement
        #vfunc(subMatrix, 2)
        # vfunc(subMatrix) #KO rien finalement
        print("subMatrix2=", subMatrix2)  # concat

        subMatInt2 = vfunc(subMatrix2)

        # affich array en ligne
        a = np.array([[0,  1,  2,  3], [10, 11, 12, 13], [
                     20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]])
        # a[:][1]KO
        m = np.matrix(a)
        # TODO col des 4 par append

        ####GRAPHS##############

        print('\nlbl60')

        ###
        indexFranceOri = 118  # ori = from ancient from Scilab file
        # 118 -2 car -1 index 0 , et -1 car sub = trunc lignes et col
        YfranceMat = subMatInt2[indexFranceOri-2-1, :]
        # ci-dessus+1 car ce n est pas une sub dc pas de trunc title
        YfranceLabel = arrayMoiMatrix[indexFranceOri-2+1]
        ###
        indexGermanyOri = 122
        YgermanyMat = subMatInt2[indexGermanyOri-2-1, :]
        YgermanyLabel = arrayMoiMatrix[indexGermanyOri-2+1]
        ###
        ###
        indexItalyOri = 139
        self.YitalyMat = subMatInt2[indexItalyOri-2-1, :]
        YitalyLabel = arrayMoiMatrix[indexItalyOri-2+1]
        ###
        ###
        indexUsOri = 227
        self.YusMat = subMatInt2[indexUsOri-2-1, :]
        YusLabel = arrayMoiMatrix[indexUsOri-2+1]
        ###

        ###
        #    chines  = np.array(coming("51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 "))
        # TODO modularize
        # coming : to commas np.array or matrix by regex floats recursive

        lm = ListeMoi()
        l2 = lm.coming(str)
        ###
        chines = lm.coming("""51    52 53
            5 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 """)  # triples guillemets
        print("chines=",chines)
        indexxMatChines = np.matrix(chines)  # to enable -2 with matrix below
        YchinesMatsTripl = subMatInt2[indexxMatChines-2-1, :]  # !!!!!!!!vector triple
        YchinesMatsDouble = YchinesMatsTripl[0]
        # np.append(q.tolist(),x.tolist(),axis=0)
        # YindiaMat=subMatInt2[indexFranceOri-2,:]
        self.YchinesMat = YchinesMatsDouble.sum(axis=0)
        ###
        frances = lm.coming("""109 110 111 112 113 114 115 116 117 118 """)
        afriques = [195, 202, 212, 144, 158, 190, 201,
                    210, 216,                       202,   106]
        # A=np.matrix([afrique1,afrique2,afrique3])OK
        # A[[0,2],:] #no range row selection, non consecutive selection

        uks = lm.coming("""219 220 221 222 223 224 225  """)
        maghrebs = [218, 215]
        russia = [189]
        # tests
        m = np.matrix([[0,  1,  2,  3],
                       [10, 11, 12, 13],
                       [20, 21, 22, 23],
                       [30, 31, 32, 33],
                       [40, 41, 42, 43]])
        n = np.matrix([[0, 1]])
        o = m[n+1, :]  # triple
        oL = (o[0]).tolist()
        val = [100, 101, 102, 103]
        qARR = np.append(oL, (np.matrix(val)).tolist(), axis=0)  # add a row
        qARR.sum(axis=0)
        ###
        india = [133]
        indexxMat = np.matrix(india)  # to enable -2 with matrix below
        YindiaMatsTripl = subMatInt2[indexxMat-2-1, :]  # !!!!!!!!vector triple
        YindiaMatsDouble = YindiaMatsTripl[0]
        # np.append(q.tolist(),x.tolist(),axis=0)
        # YindiaMat=subMatInt2[indexFranceOri-2,:]
        YindiaMat = YindiaMatsDouble.sum(axis=0)
        ###
        southKorea = [145]
        ###
        # plt.plot(YfranceMat.T,YgermanyMat.T, label='linear')KO
        # plt.plot(YfranceMat.T,YgermanyMat.T)KO
        # https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html?highlight=plot#matplotlib.pyplot.plot
        # plt.plot(YfranceMat.T,label='linear',YgermanyMat.T,label='linear')#draw .T +++++++++ car que mat colKO
        ###
        print(YfranceLabel)

        print(YitalyLabel)
        print(YusLabel)
        print(YgermanyLabel)

        ###
        plt.xlabel('days from 2020/1/22')
        plt.ylabel('items')
        plt.title("Covid19 evolution of confirmed cases from 2020/1/22")

        colonnIndxMax = self.YusMat.shape[1]-1
        plt.xlim(0, colonnIndxMax)
        #plt.ylim(0, self.YusMat[0, colonnIndxMax])#scale lim
        plt.ylim(0, 1000000)

        # plt.plot(YfranceMat.T,'b.',label='linear',self.YitalyMat.T,'ro',label='linear',self.YusMat.T,'b.',label='linear',YgermanyMat.T,'b.',label='linear')
        # linestyle='-' options https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html?highlight=plot#matplotlib.pyplot.plot
        plt.plot(YfranceMat.T, 'b-', label='France',
                 linewidth=2, markersize=12, )
        plt.plot(self.YitalyMat.T, 'r-', label='Italy')
        plt.plot(self.YusMat.T, 'k-', label='USA')
        plt.plot(YgermanyMat.T, 'c-', label='German')
        plt.plot(self.YchinesMat.T, 'g-', label='China')


        plt.legend()  # AP plot++++++OK ssi chn color etc st !=
        #plt.show()

        #strAllMerged=self.nature+'.pdf'
        #https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/usetex_fonteffects.html#sphx-glr-gallery-text-labels-and-annotations-usetex-fonteffects-py
        #plt.savefig(self.nature+'.pdf')
        #print('strAllMerged=',strAllMerged)
        plt.savefig(self.nature+'.png')
        plt.savefig(self.nature+'.svg')
        plt.savefig(self.nature+'.jpg')
        ###
        # fig = plt.figure()  # an empty figure with no axes
        # fig.suptitle('No axes on this figure')  # Add a title so we know which it is

        # fig, ax_lst = plt.subplots(1, 1)  # a figure with a 2x2 grid of Axes

        print('\nlbl70')
        #plt.xlabel('x label')
        #plt.ylabel('y label')
        print('\nlbl80')

        print('\nlbl85')
        # https://matplotlib.org/3.1.0/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
        # https://stackoverflow.com/questions/59346731/no-handles-with-labels-found-to-put-in-legend

        print('\nlbl90')

        print('\nlbl100')

        # YfranceLabel

        # plt.legend(YfranceMat,['fr'])#draw
        #plt.plot(x, x, label='linear')
        # TODO a;b;c;d;e; = print(a);print(2)


natureAnalyzed = MaladType("time_series_covid19_confirmed_global")
natureAnalyzed.main()

natureAnalyzed = MaladType("time_series_covid19_deaths_global")
natureAnalyzed.main()

natureAnalyzed = MaladType("time_series_covid19_recovered_global")
natureAnalyzed.main()