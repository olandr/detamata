import time
import pandas as pd
from random_words import RandomWords
import names
import random
from datetime import datetime


rwob = RandomWords()

input = "./in.csv"
output= "./out.csv"
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
GENERATE = 100
# SEED is the offset for unique values i.e. some_unique value = SEED + id
SEED = 1951379
id = -1

for utable in utables:
    open("tables/" + utable + ".csv", "w").close()
tuple = 0
## We iterate across each unique table as we want to make create table utable
while tuple < GENERATE:
    dictionary = {}
    # Parent unique-id (the unique base for this table)
    id += 1
    tuple += 1      # I use 1-indexexing hence 1 tuple IS 1 one row (not 0 tuples/rows)
    print(tuple)
    for utable in utables:
        outstring = []
        index = 1
        # Get all the rows with the current utable
        rows = data[data['*table'] == utable]
        # We want, for each column/attrib, iterate through.
        while index <= len(rows):
            typer = rows['!type'][index-1:index]
            # We want to see if a certain column (say student_id) already has been defined for this unit/table/relation.
            if ((rows['#key'][index-1:index].str.contains('primary|foreign|unique', regex=True)).any()):
                # Saves the name of this attribut/column
                col = rows['*column'][index-1:index].any()
                # We check this by validating student_id in dictionary. Where e.g. dictionary = {"student_id":183418}
                    # If it already has been assigned, we do not want to generate a new id. We append THAT dictionary-value to outstringself.
                    # Else we generate a new, and append that instead.
                if (rows['*column'][index-1:index].any() in dictionary):
                    outstring.append(dictionary.get(col)+ ";")

                else:
                    # Each child unique-value needs to be incremented.
                    id += 1
                    # Generate a new seed and save to dictionary
                    newid = str(SEED + id)
                    dictionary[col] = newid
                    outstring.append(newid + ";")
                if (index == len(rows)):
                    outstring.append("\n")
                index += 1
                continue

            # Case consideration for different datatypes.

            # DATETIME CASE:
            if ( (typer == 'datetime').bool()):
                # We want a random datetime
                outstring.append(str(datetime(random.randint(1970,2018), random.randint(1,12), random.randint(1,28))))

            # STRING CASE:
            if ((typer == 'string').bool()):
                # We want some strings to be "names", and some to be regular random words.
                if ((rows['*column'][index-1:index].str.contains("name")).bool()):
                    outstring.append(names.get_full_name())
                else:
                    outstring.append(rwob.random_word())

            # UNIQUE INT CASE --- EXCLUDING primary/foregin keys (these are saved above)
            if ((typer == 'int').bool() and not (rows['#key'][index-1:index].str.contains('primary|foreign|unique', regex=True)).any()):
                outstring.append(str(random.randint(1,100000)))

            if (len(outstring) != 0 and (rows['!IS_NULLABLE'][index-1:index] == 'YES').bool()):
                if(random.getrandbits(1)):
                    outstring.pop()
            if (index == len(rows)):
                outstring.append(";\n")
            else:
                outstring.append(";")
            index += 1

        with open("tables/" + utable + ".csv", "a") as out:
            # Here we write to the outputfile
            jndex = 0
            while jndex < len(outstring):
                out.write(outstring[jndex])
                jndex += 1

            out.close()
