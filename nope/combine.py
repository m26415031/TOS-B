#!/usr/bin/python

with open('data.txt') as f:
    lis=[map(int,x.split()) for x in f if x.strip()]
