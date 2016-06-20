# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:47:11 2016

@author: gebruiker
"""
import os
import sys

def execute():
    '''Executes a VBA script which loops over all files in a given directory, extracts their footnotes and saves them in the map results'''
    #os.chdir(os.path.dirname(sys.argv[0]))
    os.system('start excel.exe GetFootnotes.xlsm')
    
#execute()