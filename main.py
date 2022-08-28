## Importing on python packages
import pandas as pd
import json
import xlrd
import bs4
import requests
import sqlalchemy
import pydub
from google.cloud import bigquery
import os # Package is used to degugging 

##Changing directory 
retval = os.getcwd()
print ("Current working directory %s" % retval)
##os.chdir('\GitHub\hha-data-ingestion')
#fkdatadir = os.path.join('D:/GitHub/', 'hha-data-ingestion/data/fakepatientdata.xlsx')

## Section 1 - Converting excel file into dataframe
# The excel file was generated by myself and does not represent any real world counterpart
fkdata = xlrd.open_workbook('/Users/xxxda/Documents/GitHub/hha-data-ingestion/data/fakepatientdata.xls', on_demand=True)
print(fkdata.sheet_names())

tab1 = pd.read_excel('/Users/xxxda/Documents/GitHub/hha-data-ingestion/data/fakepatientdata.xls', sheet_name="Sheet1")
tab2 = pd.read_excel('/Users/xxxda/Documents/GitHub/hha-data-ingestion/data/fakepatientdata.xls', sheet_name="Sheet2")

print(tab1)
print(tab2)

###Code below is for main desktop
#xls = xlrd.open_workbook('data/fakepatientdata.xlsx', on_demand=True)
#xls = xlrd.open_workbook('D:/GitHub/', 'hha-data-ingestion/data/fakepatientdata.xlsx', on_demand=True)
#xls.sheet_names() 
#fkdatadir.sheet_names()

##Section 2 - Use the requests package to open a json API via CMS

print("Finished Running")