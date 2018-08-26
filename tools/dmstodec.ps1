# input:
# N\d+°\d+'\d+" E\d+°\d+'\d+"
# N\d+°\d+'\d+" E\d+°\d+'\d+"
# ...
# output:
# N: [float], E: [float]
# N: [float], E: [float]
# ...

cls
$file = "test"
$input = "E:\User\Simon\document\GitHubE\olandr\detamata\tools\$($file).txt"
$output = "E:\User\Simon\document\GitHubE\olandr\detamata\tools\$($file)out.txt"
echo $input $output
rm $output -ea ig

foreach($line in (Get-Content $input)) {
  $d = $line.Split("(°|`'|`"| )")
  #Ndegrees $d[0]
  #Nmins $d[2]
  #Nsec $d[3]
  #Edegrees $d[5]
  #Emins $d[7]
  #Esec $d[8]
  $north = [int]$d[0] + [int]$d[2]/60 + [int]$d[3]/3600
  $east = [int]$d[5] + [int]$d[7]/60 + [int]$d[8]/3600
  ac $output "N: $($north), E: $($east)" -Encoding UTF8
}
