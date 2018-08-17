#!/bin/bash
function pause(){
   read -p "$*"
}

rm complete.rdf.gz
rm data/complete.rdf
cat *.rdf >> complete.rdf
cp complete.rdf data/complete.rdf
gzip complete.rdf

osascript -e 'tell app "Terminal" to do script "cd /Users/simon/Docs/kthgraph/workingExample; dgraph zero"'
osascript -e 'tell app "Terminal" to do script "cd /Users/simon/Docs/kthgraph/workingExample; dgraph server --lru_mb 2048 --zero localhost:5080"'
osascript -e 'tell app "Terminal" to do script "cd /Users/simon/Docs/kthgraph/workingExample; dgraph-ratel"'
curl -X POST localhost:8080/alter -d '{"drop_all": true}'
sleep 8
dgraph live -r complete.rdf.gz -s she.schema
pause 'Press any key to continue...'
