rm complete.rdf.gz
cd data
rm complete.rdf
cd ..
type *.rdf > data\complete.rdf
cd data
copy complete.rdf ..\complete.rdf
cd ..
gzip complete.rdf
rmdir /Q /S p
rmdir /Q /S w
rmdir /Q /S zw

start dgraph zero
start dgraph server --lru_mb 2048 --zero localhost:5080
start dgraph-ratel
timeout /t 8
dgraph live -r complete.rdf.gz -s she.schema
pause
