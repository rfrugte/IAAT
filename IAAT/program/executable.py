# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:48:12 2016

@author: gebruiker
"""
import ProcessFootnotes
import categorize
import mainextraction
import ValidateLinks
import GetDG
import create_excel
import comchecker
#import GetDGanalyze





process_footnotes = True
check_all = True     
get_info= True
get_archived=True
validate_links=True
#check_dg=False
analyze=False
def run(process_footnotes,check_all,get_info,validate_links,get_archived):
    if process_footnotes:   
        info_footnotes = ProcessFootnotes.execute()
    if check_all:
        info_links=mainextraction.execute(info_footnotes)
    working_list=GetDG.execute(info_links) 
    if get_info:    
        working_list = categorize.execute(info_links)
    if validate_links:    
        working_list=ValidateLinks.execute(working_list,get_archived) 
    create_excel.execute(working_list)
    #global working_list
    if analyze:
        data=comchecker.run(working_list)
        #data2=GetDGanalyze.execute(data)
#run(True,True,True,False,False)


    