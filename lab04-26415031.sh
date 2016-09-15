#!/bin/bash

beli= `curl -s http://www.bankmandiri.co.id/ | grep USD -A2 | cut -d">" -f2 | cut -d"<" -f1 | xargs | cut -d" " -f2`
jual= `curl -s http://www.bankmandiri.co.id/ | grep USD -A2 | cut -d">" -f2 | cut -d"<" -f1 | xargs | cut -d" " -f3`
echo "Harga jual: $jual"
echo "Harga beli: $beli"
