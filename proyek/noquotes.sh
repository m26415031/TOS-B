#!/usr/bin/bash

curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php | grep "/saham/grafik/harga" -A13 | grep "<strong>" | cut -d">" -f2 | cut -d"<" -f1 > kodeemiten.txt


curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php | grep "/saham/grafik/harga" -A13 | grep "%<" | cut -d ">" -f3 | cut -d "<" -f1 > persenselisih.txt

curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php?periode=$waktu | grep "/saham/grafik/indeks_bei/harga" -A13 | grep "<strong>" | cut -d">" -f3 | cut -d"<" -f1 > sektor.txt

sectors=()
while IFS= read -r line

do
    
	sectors+=("$line") 
done < sektor.txt

companies=() 
while IFS= read -r line

do
    
	companies+=("$line") 
done < kodeemiten.txt

percents=() 
while IFS= read -r line

do
    
	percents+=("$line") 
done < persenselisih.txt

counter=0
now="$(date +'%Y%m%d')"
for((i=0;i<90;i++))
{
	if(($i % 10 == 0))&&(($i != 0))
	then
	{
		counter=$((counter + 1))
	}
	fi
	echo $((i + 1)) "," ${sectors[$counter]} "," ${companies[$i]} "," ${percents[$i]} "," $now>> temp.csv
}

cat temp.csv | sed 's/ , /,/g' | sed 's/%//g' > data.csv

rm temp.csv
