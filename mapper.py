#!/usr/bin/env python

import os,sys
for line in sys.stdin:
	# delete white spaces in lines
	line=line.strip()
	# filter data as Project 1.1
	l=line.split()
	# filter malformat data missing article names
	if len(l)!=4:
		continue
	for j,col in enumerate(l):
		if (j==0):
			if(col!='en'):
				break
		if (j==1):
			prefix=['Media:','Special:','Talk:','User:','User_talk:','Project:','Project_talk:','File:','File_talk:','MediaWiki:','MediaWiki_talk:','Template:','Template_talk:','Help:','Help_talk:','Category:','Category_talk:','Portal:','Wikipedia:','Wikipedia_talk:']
			suffix=['.jpg','.gif','.png','.JPG','.GIF','.PNG','.txt','.ico']
			title=['404_error/','Main_Page','Hypertext_Transfer_Protocol','Search']
			if col.startswith(tuple(prefix)) or col.startswith(tuple(title)):
				break
			elif col[0].islower():
				break
			elif col.endswith(tuple(suffix)):
				break
			else:
				word=l[1]
				count=int(l[2])
				# get date information from filenames
				fname=os.environ["mapreduce_map_input_file"]
				fdate=fname.split('-')
				date=fdate[2]
				# output filtered data and set article's name as key for mapper
				print '%s\t%s\t%d' % (word,date,count)






