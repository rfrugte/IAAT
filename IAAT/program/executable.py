# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:48:12 2016

@author: gebruiker
"""
#import GetReferences
#import GetFootnotes
#import GetHeadings
import ProcessFootnotes
#import dictionary
import categorize
import newtest
import ValidateLinks
import GetDG
#import CheckLinks
#import CheckMonitoring
#import CompleteDict
import create_excel
import comchecker
import GetDGanalyze
#import categorize
import cProfile
import time


#get_references = False
#get_footnotes = False   #Warning uses office
                        #Warning only works with office 2013+
                        #Warning slow ~20s per pdf for i3 4gb   


process_footnotes = True
check_all = True     
get_info= True
get_archived=True
validate_links=True
check_dg=True
analyze=False
def run(process_footnotes,check_all,get_info,validate_links,get_archived):
#def run():    

  
    if process_footnotes:   
        info_footnotes = ProcessFootnotes.execute()

    if check_all:
        info_links=newtest.execute(info_footnotes)
        
    working_list=GetDG.execute(info_links) 
    #print(working_list[-1])
    if get_info:    
        working_list = categorize.execute(info_links)
        #data =create_excel.execute(check3)
    if validate_links:    
        working_list=ValidateLinks.execute(working_list,get_archived)
        #ValidateLinks.execute(working_list)
    create_excel.execute(working_list) 
    if analyze:
        data=comchecker.run(working_list)
        #data2=GetDGanalyze.execute(data)
        global data
start_time= time.time()    
run(True,True,True,True,True)

print("%s"% (time.time()-start_time))
#cProfile.run("run(True,True,True,False,False)")
    