import pandas as pd


input="/Users/simon/Docs/olandr/detamata/tools/datagen/in.csv"
output="/Users/simon/Docs/olandr/detamata/tools/datagen/out.csv"
print(input, output)

data = pd.read_csv(input, sep=';', header=0)
# Gather the header row (first row; specifief by header=0 above)
header = list(data)

# We have four tables, two are the unique table nams and column names. And two are not.
utables = data.ix[:,0].unique()
ucolumns = data.ix[:,1].unique()




SIZE = "255"
outstring = []
open(output, "w").close()
with open(output, "a") as out:
    for utable in utables:
        row = data[data.table == utable]
        print(row.type)
        index = 0
        for row in rows:
            if (types[index] == "datetime"):
                outstring.append("DATETIME")
            if (types[index] == "string"):
                outstring.append("VARCHAR(" + SIZE + ")")
            if (types[index] == "int"):
                outstring.append("INT")

            if (index == len(columns)-1):
                outstring.append(")")
                break
            else:
                outstring.append(",")
            index += 1

    jndex = 0
    while jndex < len(outstring)-1:
        out.write(outstring[jndex] + outstring[jndex +1] + "\n")
        jndex += 2

out.close()
