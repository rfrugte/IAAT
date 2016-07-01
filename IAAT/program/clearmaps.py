# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 11:11:42 2016

@author: gebruiker
"""

import os
def execute():
    docx=os.path.dirname(os.path.realpath(__file__))+'\DOCX'
    results=os.path.dirname(os.path.realpath(__file__))+'\Results'
    clear_map(docx) 
    clear_map(results)   
    
    
def clear_map(Map):    
    for the_file in os.listdir(Map):
        file_path=os.path.join(Map, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)