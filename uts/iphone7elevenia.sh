#!/bin/bash

harga=`curl -s http://www.elevenia.co.id/prd-apple-iphone-7-plus-black-128gb-garansi-6242166 | grep "price notranslate" | cut -d">" -f2 | cut -d"<" -f1 | cut -d" " -f2`

echo `date` "|" $harga>>~/iphone7elevenia.txt

pr=`curl -s http://www.elevenia.co.id/prd-apple-iphone-7-plus-black-128gb-garansi-6242166 | grep "price notranslate" | cut -d">" -f2 | cut -d"<" -f1 | cut -d" " -f2 | cut -d"." -f1`

if [$pr<15] then 
echo `date` "|" $harga | mail -s "Harga iPhone 7 Plus" m26415031@john.petra.ac.id
fi
