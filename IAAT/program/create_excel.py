# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:45:07 2016

@author: gebruiker
"""
import pandas as pd
from pandas import DataFrame
import os

def execute(working_list):
    names=[]
    pages=[]
    references=[]
    footnotes=[]
    relevant_footnotes=[]
    policy_law=[]
    profdata=[]
    journal=[]
    none=[]
    com=[]
    sec=[]
    year=[]
    mande=[]
    len_mande=[]
    valid_links=[]
    invalid_links=[]
    archived_links=[]
    DG=[]
    for i in range(0,len(working_list)):
        names.append(working_list[i][0])
        pages.append(working_list[i][3])
        references.append(len(working_list[i][1]))
        footnotes.append(working_list[i][6])
        DG.append(working_list[i][8])
        relevant_footnotes.append(len(working_list[i][7])-working_list[i][9].count('None'))
        policy_law.append(working_list[i][9].count('PolicyLaw'))
        profdata.append(working_list[i][9].count('Profdata'))
        journal.append(working_list[i][9].count('Journal'))
        none.append(working_list[i][9].count('None'))
        if (len(working_list[i][4][0])>1):
            com.append(working_list[i][4][0][0])
            sec.append(working_list[i][4][0][1])
        else:
            com.append(working_list[i][4][0])
            sec.append(working_list[i][4][0])            
        year.append(working_list[i][4][1])
        if len(working_list[i])>12:
            valid_links.append(working_list[i][11])
            invalid_links.append(working_list[i][10]-working_list[i][11])
            archived_links.append(working_list[i][12])
        if not working_list[i][2]==None:
            mande.append('yes')
            len_mande.append(working_list[i][2][1])
        else:
            mande.append('no')
            len_mande.append(0)
    #names=list(check)
    if len(working_list[i])<=12:
        df= DataFrame({'Name':names, 'DG':DG, 'Year':year, 'Proposal':com, 'IA report':sec, 'References':references, 'Footnotes':footnotes, 'Relevant Footnotes':relevant_footnotes, 'Policy/Law':policy_law, 'Profdata':profdata, 'Journal':journal, 'None':none, 'M&E':mande, 'M&E Words':len_mande})
        os.chdir('..')        
        writer= pd.ExcelWriter('Tool_output_without_links.xlsx', engine='xlsxwriter') 
        df.to_excel(writer,sheet_name='info',columns=['Name','DG','Year','Proposal','IA report','References','Footnotes','Relevant Footnotes','Policy/Law','Profdata','Journal','M&E','M&E Words'])        
        workbook=writer.book
        worksheet=writer.sheets['info']
        worksheet.set_column('B:C',60)
        worksheet.set_column('D:O',20)
        writer.save()
        file = "Tool_output_without_links.xlsx"
        os.startfile(file)
    else:
        df= DataFrame({'Name':names, 'DG':DG, 'Year':year, 'Proposal':com, 'IA report':sec, 'References':references, 'Footnotes':footnotes, 'Relevant Footnotes':relevant_footnotes, 'Policy/Law':policy_law, 'Profdata':profdata, 'Journal':journal, 'None':none, 'M&E':mande, 'M&E Words':len_mande, 'Valid Hyperlinks':valid_links, 'Invalid Hyperlinks':invalid_links, 'Archived Hyperlinks':archived_links })
        os.chdir('..')
        writer= pd.ExcelWriter('Tool_output_with_links.xlsx', engine='xlsxwriter') 
        df.to_excel(writer,sheet_name='info',columns=['Name','DG','Year','Proposal','IA report','References','Footnotes','Relevant Footnotes','Policy/Law','Profdata','Journal','M&E','M&E Words','Valid Hyperlinks','Invalid Hyperlinks','Archived Hyperlinks'])
        #df.to_excel('C:/Users/gebruiker/Desktop/Demo/test.xlsx',sheet_name='info',columns=['Name','Year','Proposal','IA report','References','Footnotes','Relevant Footnotes','Policy/Law','Profdata','M&E','M&E Words','Valid Hyperlinks','Invalid Hyperlinks','Archived Hyperlinks'])
        workbook=writer.book
        worksheet=writer.sheets['info']
        worksheet.set_column('B:C',60)
        worksheet.set_column('D:Q',20)
        writer.save()
        file = "Tool_output_with_links.xlsx"
        os.startfile(file)
    return df

#execute(working_list)