#file mag Login pratique blanc no 10 p23 :
#                                sexe boobs tits p24, p26, p31
#                                svg graph XML p40
#                                recherches Google p52
#                                SOAP LDAP p54
#                                Gmail p56
#                                Zope ( Plone ) server p64
#mag Linux magazine no 49H jaune :
#                                pip + virtual env +h versions p26 (cf repo Kubernetes Python)
#                                Redis p32
#
####
##mag Linux France bleu no 40H :

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
    for roww in csv_reader:
         #if line_count == 0:
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
         
        print(f'\t {line_count} {roww[1]} {int(roww[4]) + 1000}')
        line_count += 1
    #print(f'Processed {line_count} lines.')
    
