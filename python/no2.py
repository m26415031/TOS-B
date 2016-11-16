#!/usr/bin/python

what=raw_input('Input a sentence: ')

def most_letters(param):
	delim=' '
	tmp=param.split(delim)
	cpw={i:len(i) for i in tmp}
	max=cpw[tmp[0]]
	for i in range(0, len(tmp)):
		if cpw[tmp[i]]>max:
			max=cpw[tmp[i]]
	for i in range(0, len(tmp)):
		if cpw[tmp[i]]==max:
			print tmp[i]

most_letters(what)
