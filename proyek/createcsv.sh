#!/usr/bin/bash
curl -s http://www.seputarforex.com/saham/sektor/tabel_naik_turun_harga.php | grep "/saham/grafik/harga" -A13 | grep "<strong>" | cut -d">" -f2 | cut -d"<" -f1 > kodeemiten.txt
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
sp=() 
while IFS= read -r line
do 
	sp+=("$line") 
done < persensektor.txt
now="$(date +'%Y%m%d')"
id="A"
for((i=0;i<9;i++))
{
	id="A"
	num=$((i + 1))
	id=$id$num
	echo $id "," ${sectors[$i]} "," ${sp[$i]} "," $now>> temp.csv
}
cat temp.csv | sed 's/ , /,/g' > persensektor.csv
#sed '1 i\ID,SEKTOR,PERUBAHAN,TANGGAL\' persensektor.csv > temp.csv
#rm persensektor.csv
#mv temp.csv persensektor.csv
rm temp.csv

counter=0
id="E"
for((i=0;i<90;i++))
{
	if(($i % 10 == 0))&&(($i != 0))
	then
	{
		counter=$((counter + 1))
	}
	fi
	id="E"
	num=$((i + 1))
	id=$id$num
	echo ${companies[$i]} "," ${sectors[$counter]} >> temp.csv
}
cat temp.csv | sed 's/ , /,/g' | sed 's/%//g' > emitents.csv
sed '1 i\KODE\' sektor.txt > sectors.csv
#sed '1 i\KODE,SEKTOR\' temp.csv > emitents.csv
#rm emitents.csv
#mv temp.csv emitents.csv
rm temp.csv
bash noquotesector.sh
#sed '1 i\ID,EMITEN,PERUBAHAN,TANGGAL\' temp.csv > data.csv
#rm data.csv
#mv temp.csv data.csv
#rm temp.csv

