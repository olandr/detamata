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

cls
$file = "test"
$input = "E:\User\Simon\document\GitHubE\olandr\detamata\tools\$($file).csv"
$output = "E:\User\Simon\document\GitHubE\olandr\detamata\tools\$($file).rdf"
echo $input $output
rm $output -ea ig

$header = (Get-Content $input | Select-Object -First 1).split(";")
$csv = Import-csv $input -Delimiter ";"

# Stores all the possible unique identifiers --- i.e. the first cell on each row.
$tables = $csv."$($header[0])"
$columns = $csv."$($header[1])"
$noTables = 0;
$noColumns = 0;
$distinct = @()

foreach ($table in $tables) { if ($distinct -notcontains $table) {$distinct += $table; $noTables++} }
foreach ($column in $columns) { if ($distinct -notcontains $column) {$distinct += $column} }

$noColumns = $distinct.length - $noTables

$langs = "da","nl","en","fi","fr","de","hu","it","no","pt","ro","ru","es","sv","tr","zh","ja","ko"
$L = 0
#tables defines the length of the csv file (the left most column). I suppose there is a bijection, so $columns could possibly also work.
for ($row = 0; $row -lt $tables.length; $row++){
  # We reset all the lang if need be
  $L = 0

  for ($col = 1; $col -lt $header.length-1; $col++){

    $ignore = $false
    $tab = $tables[$row]
    $predicate = $header[$col]
    $relation = $csv[$row]."$predicate"
    $remove = 1;
    # We need to differentiate whether the attribute is a uid-relation, multiple alternative (@lang), ignore, facets or just a value.
    # This identifier is removed in the output.
    switch ("$predicate"[0]) {
      "*" {$relation = "_:$($relation)"}
      "@" {if ($L+1 -gt $langs.length) {$predicate += "*ERROR_ALL_LANGS_USED*"}; $relation = "`"$($relation)`"@$($langs[$L])";$L++}
      "!" {$ignore = $true}
      "#" {ac $output "`($($predicate.Substring(1, $predicate.length -1))=$($relation)`) " -Encoding UTF8 -NoNewLine; $ignore = $true}
      default {$relation = "`"$($relation)`"";$remove = 0}
    }
    if (-Not ($ignore)) {ac $output ".`r`n_:$tab <$($predicate.Substring($remove))> $relation " -Encoding UTF8 -NoNewLine}
  }
}
# Due to iterative newline-dot creation I have to append one dot independently to the other ones, prior to adding names.
ac $output "."
$tableCounter = 1;
foreach ($dist in $distinct) {
  $outString = "_:$dist <name> `"$dist`" ."
  if ($tableCounter -le $noTables) {
    $outString += "`r`n_:$dist <TYPE> `"TABLE`" ."
  }
  Else {
    $outString += "`r`n_:$dist <TYPE> `"COLUMN`" ."
  }
  ac $output $outString -Encoding UTF8
  $tableCounter++
}
# In this verison, I append a .\r\n on every line (that is not ignored). This means that the first line gets a .\r\n. This needs to be removed:
Get-Content $output | select -Skip 1 | Set-Content "$output-temp"
move $output-temp $output -Force
