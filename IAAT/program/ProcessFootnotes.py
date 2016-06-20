# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:43:27 2016

@author: gebruiker
"""

import rd
#import codecs
import os
import xlrd

def open_location():
    '''Changes the working directory and loops through all files with extension "xlsx"  '''
    if not '\program' in os.getcwd():    
        rd.open_location('/program',False)    
    rd.open_location('/Results',False)    
    #os.chdir("..")
    #os.chdir(os.getcwd() + "/Results")     
    
def read_lines(filename):
    '''Converts the rows in a xlsx file into a list '''
    listed_footnotes =[]
    footnotes = xlrd.open_workbook(filename)
    sheet_name= footnotes.sheet_by_index(0)
    number_of_rows = sheet_name.nrows
    for i in range(0,number_of_rows):
        if isinstance(sheet_name.row_values(i)[0],str):
            listed_footnotes.append(sheet_name.row_values(i)[0].strip())
    return listed_footnotes    
        

def first_classification(listed_footnotes):
    likely_relevant=[]
    likely_not_relevant=[]
    links=[]
    number_of_footnotes=len(listed_footnotes)
    for footnote in listed_footnotes:
        if "http" in footnote or rd.contains_number(footnote)>=3:
            likely_relevant.append(footnote)
        else:
            likely_not_relevant.append(footnote)
    return (likely_relevant ,number_of_footnotes)     
            

def main_loop():
    open_location()
    number_of_footnotes_list=[]
    footnotes_list=[]
    filenames=[]
    footnotes=[]
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".xlsx"):
            listed_footnotes=read_lines(filename)
            footnote_info=first_classification(listed_footnotes)
            number_of_footnotes_list.append(footnote_info[1])
            footnotes_list.append(footnote_info[0])
            filenames.append(filename)

            
        else:
            continue
    return(filenames,number_of_footnotes_list,footnotes_list)
    
def execute():
    return main_loop()
    
#execute()   