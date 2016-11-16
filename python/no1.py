#!/usr/bin/python

what=raw_input('Input a string: ')

def count_characters(param):
	this=list(param)
	res=dict()
	from collections import Counter
	res=Counter(this)
	print res
	
count_characters(what)		
