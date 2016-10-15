#!/usr/bin/python
import csv
import numpy as np

def deal_data():
	f1=open('/home/star/project/music/data/11.csv')
	for line1 in f1:
		artist_id=line1.split('\t')[0].strip()
		count=line1.split('\t')[1].strip()
		date=line1.split('\t')[2].strip()
		f=open('/home/star/project/music/data/everyData/'+artist_id+'.txt','a')
		f.write(date+','+count)
		f.write('\n')
		f.close()

if __name__=="__main__":
	deal_data()
	

	
