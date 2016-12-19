#!/usr/bin/bash

index=`cat sendalert.txt | cut -d"," -f1`
src=`cat sendalert.txt | cut -d"," -f2`
mail=`cat sendalert.txt | cut -d"," -f3`

ems=()
while IFS= read -r line
do
	ems+=("$line") 
done < data.csv

em=`echo ${ems[$index]}`

bash alert.sh $em $src $mail
