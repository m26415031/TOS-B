#!/usr/bin/python

what=raw_input('Input a string: ')

def unique_elements(param):
	this=list(param)
	tmp=dict()
	res=[]
	from collections import Counter
	tmp=Counter(this)
	for i in range(0,len(this)):
		if tmp[this[i]]==1:
			res.append(this[i])
	print res
	
unique_elements(what)
