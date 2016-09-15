#!/bin/bash

/sbin/ifconfig | grep "inet addr" | cut -d" " -f12 | cut -d":" -f2 | xargs |echo "`date` " `awk -F " " '{print "=>",$2,$1;}'`

