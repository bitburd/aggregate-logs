#!/usr/bin/python
#
# Using python open apache error log and get the time from a line
# Author: Jason Graham
# The script will also aggregate and acumulate data in form of grouped errors
# Useage: aggregate-logs.py /var/log/httpd/error_log
#
 
import sys
import datetime
import pandas as pd
from db import *

#aggregate candidates
error_df = [['data','item','date','time']]
erroritem = ['[authz_core:error]','[core:error]','[203]','[204]','[205]','[301]','[302]','[400]','[401]','[404]','[408]','[412]','[414]','[500]','[502]','[504]']

#aggregation dataframe
df = pd.DataFrame(error_df)

#get date
currdate = datetime.datetime.now()
datestr = currdate.strftime('%m-%d-%Y') 
currtime = datetime.datetime.now()
timestr = currtime.strftime('%H:%M:%S')

#error line count
ec = 0

#open log file handle
filename = sys.argv[1]
fileh = open(filename, "r", 0)

#open a line and estimate the num of columns
def find_columns(dataline):
    colnum = 0
    for col in dataline:
        colnum = colnum + 1
    return colnum

#get file lines that contain error data by error item code 
def get_error_lines(line,item):
    global ec
    totcols = 0
    columns = find_columns(line)
    #find if log line column has a predefined error:
    c = 0
    while c < columns:
        try: 
	    if item in line:
                erritem = item
                if ec:
                     errorlines[ec] = line
                     ec = ec + 1
            else:
                erritem = "notfound"
        finally:
            c += 1
        return erritem

# add error and itemtype data to aggregation dataframe
def add_to_dataframe(data,item,date,time):
    dfadd = df.append(pd.DataFrame([[data,item,date,time]], columns=['data','item','date','time']), ignore_index=True)
    return dfadd


# group dataframes to error item
def group_dataframe(index):
    global df


# for each error item, add them to the dataframe
for itm in erroritem:
     for line in fileh:
         erritem = get_error_lines(line,itm)
         if erritem != 'notfound':
             df = add_to_dataframe(line,itm,datestr,timestr)

# group the dataframes by error item
group_dataframe('item')

#add dataframe items to a db 
create_connection()
for row in df.iterrows():
   index, data = row
   data1 = data['data']
   item1 = data['item']
 
   insert_data(data1, item1, datestr, timestr)
close_connection()

