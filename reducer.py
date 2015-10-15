#!/usr/bin/env python
import sys
from operator import itemgetter, methodcaller

# initialize
current_word=None
current_date=0
current_count=0
word = None
dateview=None
total_count=0
reducelist=[]
initial_date=20150801
last_date=20150831

# sort datas according to article name and dates 
for line in sys.stdin:
	line=line.strip()
	l=line.split('\t')
	l[1]=int(l[1])
	reducelist.append(l)
reducelist=sorted(reducelist,key=itemgetter(0,1))

# count total views for sorted datas
for line in reducelist:
	word=line[0]
	date=line[1]
	count=line[2]

	# throw an exception for possible ValueError
	try:
		count=int(count)
	except ValueError:
		continue
	# after going through previous key, output its infomation
	if current_word==word:
		# count daily views by suming hourly views up
		if current_date==date:
			current_count+=count
		else:
			# record day views
			if current_date:
				if dateview:
					daycount=(':').join([str(current_date),str(current_count)])
					dateview=('\t').join([dateview,daycount])
				else:
					if current_date==initial_date:
						daycount=(':').join([str(current_date),str(current_count)])
						dateview=daycount
					else:
						daycount=(':').join([str(initial_date),'0'])
						dateview=daycount
						initial_date=initial_date+1
						while current_date!=initial_date:
							daycount=(':').join([str(initial_date),'0'])
							dateview=('\t').join([dateview,daycount])
							initial_date=initial_date+1
						daycount=(':').join([str(current_date),str(current_count)])
						dateview=('\t').join([dateview,daycount])
				# count monthly views by suming daily views up
				total_count+=current_count
				current_date+=1
			while current_date!=date:
				daycount=(':').join([str(current_date),'0'])
				dateview=('\t').join([dateview,daycount])
				current_date+=1
			current_date=date
			current_count=count
	else:
		# carefully cope with the first and the last data
		if current_date:
			if dateview:
				daycount=(':').join([str(current_date),str(current_count)])
				dateview=('\t').join([dateview,daycount])
				while current_date!=last_date:
					current_date+=1
					daycount=(':').join([str(current_date),'0'])
					dateview=('\t').join([dateview,daycount])
			else:
				if current_date==initial_date:
					daycount=(':').join([str(current_date),str(current_count)])
					dateview=daycount
				else:
					daycount=(':').join([str(initial_date),'0'])
					dateview=daycount
					initial_date=initial_date+1
					while current_date!=initial_date:
						daycount=(':').join([str(initial_date),'0'])
						dateview=('\t').join([dateview,daycount])
						initial_date=initial_date+1
					daycount=(':').join([str(current_date),str(current_count)])
					dateview=('\t').join([dateview,daycount])
			total_count+=current_count
			# output results
			if current_word and total_count>100000:
				print '%s\t%s\t%s' %(total_count,current_word,dateview)
		current_word=word
		current_date=date
		current_count=count
		# reset data for month views
		total_count=0
		dateview=None
		initial_date=20150801
