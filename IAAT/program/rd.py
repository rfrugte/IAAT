# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:56:12 2016

@author: gebruiker
"""

from bs4 import BeautifulSoup
import codecs
import os

def open_location2(map_name):
    '''Changes the working directory and loops through all files with extension "docx"  '''
    
    os.chdir("..")
    os.chdir(os.getcwd() + map_name)

def open_location(map_name,back):
    '''Changes the working directory and loops through all files with extension "docx"  '''
    if back:    
        os.chdir("..")
    os.chdir(os.getcwd() + map_name)

def list_to_txtfile(to_write):
    '''Writes a list to a text file.'''
    with open("testfile.txt", "w",encoding="utf-8") as text_file:
        for item in to_write:
            text_file.write(item + "\n\n")
 
def print_list_with_enter(to_print):
    '''Print list separated by enters'''
    for item in to_print:
        print(item + "\n\n")  
        
def contains_number(to_search):
    return sum(char.isdigit() for char in to_search)    

def get_pagenumber(to_search):
    #return re.sub('.*?([0-9]*)$', r'\1', to_search)
    #return re.match('.+([0-9])[^0-9]*$',to_search).group(1)
    array =[int(i) for i in to_search.split() if i.isdigit() ]
    print(array)
    return array.pop()

def get_raw_text(filename):
    '''Import the files and gets the raw text in lowercase, this makes it easier to search'''   
    htm_file = codecs.open(filename, "r","utf-8")
    soup = BeautifulSoup(htm_file, 'html.parser')
    for script in soup(["script","style"]):
        script.extract()
    raw_text= soup.get_text().lower()
    return raw_text        