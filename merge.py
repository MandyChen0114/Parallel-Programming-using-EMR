#!/usr/bin/env python

from operator import itemgetter, methodcaller

# merge output files
files=('','')
w=open('output','w')
resultlist=[]
for parts in files:
	f=open(parts,'r')
	for line in f:
		line=line.strip()
		l=line.split('\t')
		l[0]=int(l[0])
		resultlist.append(l)

# sort outputs by descending order
resultlist=sorted(resultlist,key=itemgetter(0),reverse=True)

# coutput results as seperate lines
for results in resultlist:
	result=('\t').join(results)
	w.write('%s\n' % (result))




#!/usr/bin/env python

from operator import itemgetter, methodcaller

# merge output files
f=open('datas','r')
w=open('output','w')
resultlist=[]
for line in f:
	line=line.strip()
	l=line.split('\t')
	l[0]=int(l[0])
	resultlist.append(l)

# sort outputs by descending order
resultlist=sorted(resultlist,key=itemgetter(0),reverse=True)

# coutput results as seperate lines
for results in resultlist:
	results[0]=str(results[0])
	result=('\t').join(results)
	w.write('%s\n' % (result))