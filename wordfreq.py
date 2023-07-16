#!/usr/bin/python3

import sys
import string

f = open('test.txt')  

lineNum = 0

words = []
for line in f:
	lineNum += 1
	#print(line)
	words2 = line.split()  
	for word in words2:
		words.append(word)
f.close()

d = dict()
for word in words:
	t = word.translate(str.maketrans('','',string.punctuation)).upper()
	if(len(t) > 0):
		d[t] = d.get(t,0) + 1

l = list()
for key,value in d.items():
	l.append((value,key))
	
l = sorted(l, reverse=True)
for v,k in l:
	print(k,v)
