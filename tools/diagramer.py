import pandas as pd

# input:
# Different initial symbols declare what kind that cell is (pointer to node, value, ignore etc.)
# [Head]: Id;(|*|@|!)\w+;(|*|@|!)\w+;...
# [Body]: uniqueID;.*;.*;...
# ...
#
# output:
# _:uniqueID <predicate> _:node|"string/int/boolean"|@lang
# ...

# Default Schema:
# name: string @index(term) .
# column: uid @reverse @count .
# TYPE: string @index(term) .

file="test"
input="/Users/simon/Docs/olandr/detamata/tools/" + file + ".csv"
output="/Users/simon/Docs/olandr/detamata/tools/"  + file + ".rdf"
print(input, output)

data = pd.read_csv(input, sep=';', header=0)
# Gather the header row (first row; specifief by header=0 above)
header = list(data)

# We have four tables, two are the unique table nams and column names. And two are not.
utables = data.ix[:,0].unique()
ucolumns = data.ix[:,1].unique()
tables = data.ix[:,0]
columns = data.ix[:,1]

langs = ["da","nl","en","fi","fr","de","hu","it","no","pt","ro","ru","es","sv","tr","zh","ja","ko"]

open(output, "w").close()
with open(output, "a") as out:
    row = 0
    # We do not want to remove a line unecessary (poor perfomance). So we add make an empty string initially, and change it later.
    linebreak = ""

    while row < tables.size:
        L = 0
        # We assume that the zeroth column is the uniqueID coulumn (in this case, Table names).
        col = 1

        while col < len(header):

            ignore = False
            tab = tables[row]
            predicate = header[col]
            relation = data.iat[row,col]
            if type(relation) == str:
                remove = 1
                id = predicate[0]
                if id == '*':
                    relation = "_:" + relation
                elif id == '@':
                    if L+1 > len(langs):
                        predicate += "*ERROR_ALL_LANGS_USED*"
                    else:
                        relation = "\"" + relation + "\"@" + langs[L]
                        L += 1
                elif id == '!':
                    ignore = True
                elif id == '#':
                    out.write(" (" + predicate[1:]+"=\""+relation+ "\")")
                    ignore = True
                else:
                    relation = "\"" + relation + "\""
                    remove = 0
                if ignore == False:
                    # We do not want to add a \s.\n on the first line.
                    if row != 0 or col != 1:
                        linebreak = " .\n"
                    out.write(linebreak + "_:" + tab + " <" + predicate[remove:] + "> " + relation )

            col += 1
        row += 1

    outstring = []
    for table in utables:
        outstring.append("_:" + table + " <name> \"" + table + "\" .\n_:" + table + " <TYPE> \"TABLE\"")
    for column in ucolumns:
        outstring.append("_:" + column + " <name> \"" + column + "\" .\n_:" + column + " <TYPE> \"COLUMN\"")
    # We need to add .\n at the end of each line, but this does not occur for the last line. Unless we have one last (empty string) in outstring.
    outstring.append('')
    for os in outstring:
        out.write(" .\n" + os)

out.close()
