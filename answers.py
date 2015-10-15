#!/usr/bin/env python
# answer_1 count lines
with open('output') as f:
	for i,l in enumerate(f):
		pass
print i+1



#!/usr/bin/env python
# answer_2 find the most popular article
with open('output') as f:
	# the first one is the most popular one because results have been sorted
	for line in f:
		l=line.split('\t')
		print '%s\t%s' %(l[1],l[0])
		break


#!/usr/bin/env python
# answer_3 find the least popular article
with open('output') as f:
	# the last one is the most popular one because results have been sorted
	# find the last one by passing all previous ones
	for j,l in enumerate(f):
		if j==1493:
			result=l.split('\t')
			print '%s\t%s' %(result[1],result[0])

#!/usr/bin/env python
# answer_4 find the most popular artice of August 2015 with ZERO views on 20150801
with open('output') as f:
	for line in f:
		l=line.split('\t')
		# the data for 20150801 is after the second tab
		Aug01=l[2]
		Aug01data=Aug01.split(':')
		# the views for Aug.01 is after the sign ':'
		Aug01view=int(Aug01data[1])
		# find the first one by passing all previous ones
		if Aug01view!=0:
			continue
		print '%s' %(l[1])
		break

#!/usr/bin/env python
# answer_5  count days when FIRST is more popular than SECOND
with open('q5') as files:
	goals=[]
	for line in files:
		line=line.split('\n')
		goals.append(line[0])
with open('output') as f:
	lists=[]
	for line in f:
		l=line.split('\t')
		if l[1]==goals[0] or l[1]==goals[1]:
			lists.append(l)
	word1=lists[0]
	word2=lists[1]
	count=0
	i=2
	# compare day by day
	while i<32:
		daily1=word1[i].split(':')
		daily2=word2[i].split(':')
		view1=int(daily1[1])
		view2=int(daily2[1])
		if view1>view2:
			count+=1
		i+=1
	print count
		





#!/usr/bin/env python
# answer_6 rank movies given
from operator import itemgetter, methodcaller
movielist=[]
sortedlist=[]
with open('q6') as f:
	for line in f:
		line=line.split('\n')
		movielist.append(line[0])
with open('output') as files:
	for line in files:
		l=line.split('\t')
		# search if the title equals to any of moive titles
		if l[1]==movielist[0] or l[1]==movielist[1] or l[1]==movielist[2] or l[1]==movielist[3] or l[1]==movielist[4]:
			moviename=l[1]
			maxview=0;
			i=2;
			while i<32:
				daily=l[i].split(':')
				dailyview=int(daily[1])
				if dailyview>maxview:
					maxview=dailyview
				i+=1
			movie=('\t').join([moviename,str(maxview)])
			movie=movie.split('\t')
			movie[1]=int(movie[1])
			sortedlist.append(movie)
# rank movies
sortedlist=sorted(sortedlist,key=itemgetter(1),reverse=True)
# join and output rank 
rank=None
for movierank in sortedlist:
	if rank:
		rank=(',').join([rank,movierank[0]])
	else:
		rank=movierank[0]
print rank


#!/usr/bin/env python
# answer_7 rank OS
from operator import itemgetter, methodcaller
oslist=[]
sortedlist=[]
with open('q7') as f:
	for line in f:
		line=line.split('\n')
		oslist.append(line[0])
with open('output') as files:
	for line in files:
		l=line.split('\t')
		# search if the title equals to any of moive titles
		if l[1]==oslist[0] or l[1]==oslist[1] or l[1]==oslist[2] or l[1]==oslist[3]:
			os=('\t').join([l[1],str(l[0])])
			os=os.split('\t')
			os[1]=int(os[1])
			sortedlist.append(os)
# rank os
sortedlist=sorted(sortedlist,key=itemgetter(1),reverse=True)
# join and output rank 
rank=None
for osrank in sortedlist:
	if rank:
		rank=(',').join([rank,osrank[0]])
	else:
		rank=osrank[0]
print rank

#!/usr/bin/env python
# answer_8 When did the article "NASDAQ-100" have the most number of page views
with open('output') as files:
	goal='NASDAQ-100'
	for line in files:
		l=line.split('\t')
		# search the article
		if l[1]==goal:
			# search the most-views day
			maxview=0
			i=2;
			while i<32:
				daily=l[i].split(':')
				dailyview=int(daily[1])
				if dailyview>maxview:
					maxview=dailyview
					date=daily[0]
				i+=1
			print date

#!/usr/bin/env python
# answer_9 Find out the number of articles with longest number of strictly decreasing sequence of views
with open('output') as files:
	count=1
	longest=0
	for line in files:
		l=line.split('\t')
		# check if it's strictly decreasing sequence
		i=2
		num=1
		previous=None
		while i<32:
			daily=l[i].split(':')
			dailyview=int(daily[1])
			if previous:
				if previous>dailyview:
					num+=1
				# if break, count days from 0
				else:
					num=1
				previous=dailyview
			else:
				previous=dailyview
			i+=1
		# check if longest
		if num>longest:
			longest=num
			count=1
		elif num==longest:
			count+=1
	print 81
















			