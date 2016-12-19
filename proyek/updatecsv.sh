#!/usr/bin/bash
curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php | grep "/saham/grafik/harga" -A13 | grep "<strong>" | cut -d">" -f2 | cut -d"<" -f1 > kodeemiten.txt
curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php | grep "/saham/grafik/harga" -A13 | grep "%<" | cut -d ">" -f3 | cut -d "<" -f1 > persenselisih.txt
curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php | grep "/saham/grafik/indeks_bei/harga" -A13 | grep "<strong>" | cut -d">" -f3 | cut -d"<" -f1 > sektor.txt
curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php | grep "/saham/grafik/indeks_bei/harga" -A8 | grep "font-size" | cut -d">" -f3 | cut -d"<" -f1 | cut -d"%" -f1 > persensektor.txt
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
sp=() 
while IFS= read -r line
do 
	sp+=("$line") 
done < persensektor.txt
now="$(date +'%Y%m%d')"
id="A"
max=`tail -n 1 persensektor.csv | cut -d"," -f1 | cut -d"A" -f2`
for((i=0;i<9;i++))
{
	id="A"
	max=$((max + 1))
	id=$id$max
	echo $id "," ${sectors[$i]} "," ${sp[$i]} "," $now>> temp.csv
}
cat temp.csv | sed 's/ , /,/g' >> persensektor.csv
rm temp.csv
counter=0
now="$(date +'%Y%m%d')"
id="P"
max=`tail -n 1 data.csv | cut -d"," -f1 | cut -d"P" -f2`
for((i=0;i<90;i++))
{
	if(($i % 10 == 0))&&(($i != 0))
	then
	{
		counter=$((counter + 1))
	}
	fi
	id="P"
	max=$((max + 1))
	id=$id$max
	echo $id "," ${companies[$i]} "," ${percents[$i]} "," $now>> temp.csv
}
cat temp.csv | sed 's/ , /,/g' | sed 's/%//g' >> data.csv
rm temp.csv


