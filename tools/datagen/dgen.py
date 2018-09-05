import pandas as pd
from random_words import RandomWords
import names
import random
from datetime import datetime


rwob = RandomWords()

input = ".\in.csv"
output=".\out.csv"
#input="/Users/simon/Docs/olandr/detamata/tools/datagen/in.csv"
#output="/Users/simon/Docs/olandr/detamata/tools/datagen/out.csv"
print(input, output)

'''
print(rwob.random_word('y'))
print(names.get_full_name())
'''

data = pd.read_csv(input, sep=';', header=0, encoding="utf-8-sig")
# Gather the header row (first row; specifief by header=0 above)
header = list(data)

utables = data.ix[:,0].unique()
# VARCHAR(SIZE)
SIZE = "255"

outstring = []
# Delete contents of output file

open(output, "w").close()
with open(output, "a") as out:


    ## We iterate across each unique table as we want to make create table utable
    for utable in utables:
        ind = 1
        # Get all the rows with the current utable
        rows = data[data['*table'] == utable]
        # We want, for each column/attrib, iterate through.
        while ind <= len(rows):
            #Initialisation of CREATE TABLE
            # Case consideration
            if ((rows['!type'][ind-1:ind] == 'datetime').bool()):
                outstring.append(str(datetime(random.randint(1970,2018), random.randint(1,12), random.randint(1,28))))
            if ((rows['!type'][ind-1:ind] == 'string').bool()):
                outstring.append(rwob.random_word())
            if ((rows['!type'][ind-1:ind] == 'int').bool()):
                outstring.append(str(184000+ind))

            if (ind == len(rows)):
                outstring.append(";\n")
            else:
                outstring.append(";")
            ind += 1

    # Here we write to the outputfile
    jndex = 0
    while jndex < len(outstring):
        out.write(outstring[jndex])
        jndex += 1

out.close()
