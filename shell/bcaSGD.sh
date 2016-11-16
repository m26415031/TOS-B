#!/bin/bash

jual=`curl -s http://www.klikbca.com/ | grep SGD -A2 | cut -d">" -f2 | cut -d"<" -f1 | xargs | cut -d" " -f2`
beli=`curl -s http://www.klikbca.com/ | grep SGD -A2 | cut -d">" -f2 | cut -d"<" -f1 | xargs | cut -d" " -f3`
echo `date` "|" $jual "|" $beli>>~/TOS-B/bcaSGD.txt
