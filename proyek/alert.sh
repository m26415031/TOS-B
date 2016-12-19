#!/bin/bash

em=$1
psrc="$2"
#xpsrc=$((psrc*100))
mail=$3

now="$(date +'%Y%m%d')"
pr=`tail -n 90 data.csv | grep $em | cut -d"," -f3 | cut -d"," -f1`
#xpr=$((pr*100))

if [ "$pr" == "$psrc" ]
then
{
	echo "Perubahan harga saham" $em "hari ini (`date`):" $pr "persen" | mail -s "Alert Saham $em" $mail
}
fi
