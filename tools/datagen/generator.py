import pandas as pd


input="/Users/simon/Docs/olandr/detamata/tools/datagen/in.csv"
output="/Users/simon/Docs/olandr/detamata/tools/datagen/out.sql"
print(input, output)

data = pd.read_csv(input, sep=';', header=0, encoding="utf-8-sig")
# Gather the header row (first row; specifief by header=0 above)
header = list(data)

utables = data.ix[:,0].unique()


db = "homework"

# VARCHAR(SIZE)
SIZE = "255"

outstring = []
# Delete contents of output file
open(output, "w").close()
with open(output, "a") as out:
    # We iterate across each unique table as we want to make CREATE TABLE utable (...)
    for utable in utables:
        ind = 1
        # Get all the rows with the current utable
        rows = data[data['*table'] == utable]
        outstring.append("CREATE TABLE " + utable + "(\n")
        # We want, for each column/attrib, iterate through.
        while ind <= len(rows):
            #Initialisation of CREATE TABLE
            outstring.append("\t" + rows['*column'][ind-1:ind].all() + " ")
            # Case consideration
            if ((rows['!type'][ind-1:ind] == 'datetime').bool()):
                outstring.append("DATETIME")
            if ((rows['!type'][ind-1:ind] == 'string').bool()):
                outstring.append("VARCHAR(" + SIZE + ")")
            if ((rows['!type'][ind-1:ind] == 'int').bool()):
                outstring.append("INT")
            if (ind == len(rows)):
                outstring.append("\n);\n")
            else:
                outstring.append(",\n")
            ind += 1

    # Here we write to the outputfile
    jndex = 0
    out.write("DROP DATABASE " + db + ";\nCREATE DATABASE " + db + " CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;\nUSE "+ db + ";\n")
    while jndex < len(outstring):
        out.write(outstring[jndex])
        jndex += 1
out.close()
