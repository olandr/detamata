cls
$file = "voteringar"
$input = "E:\User\Simon\document\GitHubE\olandr\detamata\tools\$($file).csv"
$output = "E:\User\Simon\document\GitHubE\olandr\detamata\tools\$($file).rdf"
echo $input $output
rm $output -ea ig

$header = (Get-Content $input | Select-Object -First 1).split(";")
$csv = Import-csv $input -Delimiter ";"

# Stores all the possible unique identifiers --- i.e. the first cell on each row.
$uid = $csv."$($header[0])"

$langs = "da","nl","en","fi","fr","de","hu","it","no","pt","ro","ru","es","sv","tr","zh","ja","ko"
$L = 0

for ($row = 0; $row -lt $uid.length; $row++){
  # We reset all the lang if need be
  $L = 0

  for ($col = 1; $col -lt $header.length-1; $col++){
    $ignore = $false
    $uniqueID = $uid[$row]
    $predicate = $header[$col]
    $relation = $csv[$row]."$predicate"

    # We need to differentiate whether the attribute is a uid-relation, multiple alternative (@lang) or just a value.
    # This identifier is removed in the output.
    switch ("$predicate"[0]) {
      "*" {$relation = "_:$($relation)"}
      "@" {if ($L+1 -gt $langs.length) {$predicate += "*ERROR_ALL_LANGS_USED*"}; $relation = "`"$($relation)`"@$($langs[$L])";$L++}
      "!" {$ignore = $true}
      default {$relation = "`"$($relation)`""}
    }
    if (-Not ($ignore)) {ac $output "_:$uniqueID <$($predicate.Substring(1))> $relation ." -Encoding UTF8}
  }
}
