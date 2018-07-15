# -*- coding: utf-8 -*-

import json
#from sodapy import Socrata
import pandas as pd
import os
#Getting data from configuration file

def Sheets(filename):
    path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Excel/%s' % filename)
    ExcelFile=pd.read_excel(path,sheetname=None,index=False)
    sheets=list(ExcelFile)
    for i in range(0,len(sheets)):
        sheets[i]=(sheets[i],sheets[i])
    sheets=tuple(sheets)
    return sheets

def Columns(filename, sheet):
    path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Excel/%s' % filename)
    #print(sheet)
    #print(filename)
    ExcelFile=pd.read_excel(path,sheetname=sheet,index=False)
    #print(ExcelFile)
    columns=list(ExcelFile)
    for i in range(0,len(columns)):
        columns[i]=(columns[i],columns[i])        
    return columns, ExcelFile

def FinalExcel(filename,sheet,columns):
    path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Excel/%s' % filename)
    ExcelFile=pd.read_excel(path,sheetname=sheet,index=False)
    ExcelFile=ExcelFile[columns]
    return ExcelFile


