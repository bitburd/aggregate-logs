#!/usr/bin/python
#
# Open a Ubuntu apache log file using python and get the time from a fictional data line
# Author: Jason Graham
# The script will eventually aggregate and acumulate data in form of grouped columns 
# Useage: aggregate.py /var/log/httpd/error_log
#
 
import sys

#open log file handle
filename = sys.argv[1]
fileh = open(filename, "r", 0)
fileh.close()

#open a line and estimate the num of columns

#gets a column from a fictional log data line
def get_column(num):
    data1 = ["Tue","7","2018","10:20:00","192.168.1.3:84801","localhost:80","[http]","-","500","internal","server","error"]
    
    #get data column
    coldata = data1[num]
    
    print "column ",num," is: ",coldata
    return coldata

#Time column 4 is '3'
get_column(3)
