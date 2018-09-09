import time
import pandas as pd
from random_words import RandomWords
import names
import random
from datetime import datetime


rwob = RandomWords()

input = "./in.csv"
output= "./out.json"
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
LENGHT = len(data)

tuple = 0
## We iterate across each unique table as we want to make create table utable

outstring = ["{\r\n\t"]
utables = data.ix[:,0].unique()
print(utables)
index = 0
# Get all the rows with the current utable
rows = data.ix[:,0]

# We want, for each column/attrib, iterate through.

open(output, "w").close()
for utable in utables:
    outstring.append("\""+ utable + "\":{\r\n\t\t")
    while index < len(rows):
        cols = data.ix[0,:]
        jndex = 1
        outstring.append("\"" + str(data.ix[index,1]) + "\": {\r\n\t\t\t")
        while jndex < len(cols):
            # We want to see if a certain column (say student_id) already has been defined for this unit/table/relation.
            outstring.append("\"" + header[jndex] + "\":\"" + str(data.ix[index,jndex]) + "\"")
            jndex += 1

            if (jndex == len(cols)):
                outstring.append("\r\n\t\t")
            else:
                outstring.append(",\r\n\t\t\t")
        index += 1
        if (index == len(rows)):
            outstring.append("}\r\n\t}\r\n")
        else:
            outstring.append("},\r\n\t\t")

outstring.append("}")
with open(output,"a") as out:
    # Here we write to the outputfile
    jndex = 0
    while jndex < len(outstring):
        out.write(outstring[jndex])
        jndex += 1
    out.close()
