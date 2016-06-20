# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:30:24 2016

@author: Jordi
"""

import rd
#import codecs
import os
import GetInfo as gi
#from bs4 import BeautifulSoup
#from collections import defaultdict

def open_location():
    '''Changes the working directory and loops through all files with extension "htm"  '''
    #os.chdir("..")
    rd.open_location('/HTM',False)
    #os.chdir(os.getcwd() + "/HTM")
        
def get_raw_text(filename):
    '''Import the files and gets the raw text in lowercase, this makes it easier to search'''
    return rd.get_raw_text(filename)

def get_references(raw_text):
    '''Takes all lines after the last occurrence of the searched query ''' 
    position=[]
    search_querys=['bibliography\n','references\n', 'bibliography','references \n']
    for query in search_querys:
        position.append(raw_text.rfind(query))
    position =sorted(position)
    references = raw_text[position[-1]:]
    listed_references_cluttered=references.splitlines()
    return listed_references_cluttered


       
    
def remove_clutter(listed_references_cluttered):
    listed_references=[]
    '''Deletes the first instance in the list. It does this because the first item is not a reference but the search query'''
    del listed_references_cluttered[0]
    '''Removes the clutter from the reference list.(empty strings, pagenumbers,language tag) and puts them in a dict '''
    for item in listed_references_cluttered:
        if item and not item.isdigit()==True and not item=="en" and not item =="\xa0" :
            listed_references.append(item)      
    listed_references=remove_extra(listed_references)        
    if listed_references and listed_references[-1]=="convert pdf to word" :
        del listed_references[-1]            
    '''write the references to text file in working directory'''        
    #rd.list_to_txtfile(listed_references)
    '''print the references in the console '''
    #rd.print_list_with_enter(listed_references)
    return listed_references 

def remove_extra(listed_references):
    '''Removes extra text after the references'''
    for string in listed_references:
        #if string and ( string.startswith('annex') or string[0].isdigit()):
        if string and ( string.startswith('annex')):
            listed_references=listed_references[0:listed_references.index(string)]
            break
        if string and string[0].isdigit():
            del listed_references[listed_references.index(string)]
    return listed_references   

def main_loop():
    open_location()
    #dict_references={}
    filename_list=[]
    pagenumber_list=[]
    listed_references_list=[]
    ia_info=[]
    raw_text_list=[]
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".htm"):
            raw_text =get_raw_text(filename)
            raw_text_list.append([filename,raw_text])
            listed_references_cluttered=get_references(raw_text)
            if listed_references_cluttered:
                listed_references=remove_clutter(listed_references_cluttered)
            else:
                listed_references='None'
            pagenumber=rd.get_pagenumber(raw_text)
            info=gi.execute(raw_text)
            #dict_references.update({filename:(pagenumber,len(listed_references),listed_references)})
            filename_list.append(filename)
            pagenumber_list.append(pagenumber)
            listed_references_list.append(listed_references)
            ia_info.append(info)
        else:
            continue
    
    return (filename_list,pagenumber_list,listed_references_list,ia_info),raw_text_list   
    
def execute():
    xdf=main_loop()
    #return main_loop()   
#    global xdf  
'''This begins the retrievel of the references in the "reference" section'''
#execute()
          



             