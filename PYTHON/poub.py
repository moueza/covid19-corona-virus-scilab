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
#https://realpython.com/python-csv/#reading-csv-files-with-csv
with open('../time_series_covid19_deaths_global.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        row
        #if line_count == 0:
        #    print(f'Column names are {", ".join(row)}')
        #    line_count += 1
        #else:
        #    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        #    line_count += 1
		#line[1]=row
		
    #print(f'Processed {line_count} lines.')
    
