# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:36:58 2019

@author: Akhil
"""

#import preprocess
import csv
file1=open("loan.csv","rt")
file2=open("loan_reduced.csv","w")
writer = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\r')
reader=csv.reader(file1,delimiter=",")
counter=0;
for row in reader:
    #temp=preprocess.process(row[5])
    writer.writerow([row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[20],row[21],row[22],row[23]])
    counter=counter+1;
    if (counter==6000):
        break;