# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:03:57 2016

@author: gebruiker
"""
import os
import rd
import re

import GetReferences as gr
import docx2txt
import linktest as lt
import GetInfo as gi
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage


def get_part_of_text(headings_list,list_of_indicators,text): 
    for i in reversed(range(len(headings_list))):
        for indicator in list_of_indicators: 
            if indicator in headings_list[i][1].lower():
                
                try:
                    if len(headings_list[i][1])>15:
                        returned_text=text.split(headings_list[i][1].lstrip('0123456789.-').strip(),1)[1]
                        returned_text=returned_text.split("Annex ",1)[0]
                        returned_text=returned_text.split("ANNEX ",1)[0]
                        returned_text=returned_text.split("annex ",1)[0]
                        returned_text=returned_text.split("APPENDIX ",1)[0]
                    else:    
                        returned_text=text.split(headings_list[i][1].lstrip('0123456789.-').strip(),1)[1]
                        returned_text=returned_text.split("Annex ",1)[0]
                        returned_text=returned_text.split("ANNEX ",1)[0]
                        returned_text=returned_text.split("annex ",1)[0]
                        returned_text=returned_text.split("APPENDIX ",1)[0] 
                    if not i+1==len(headings_list):
                        for j in range(i+1,len(headings_list)):
                            for indicator_ in list_of_indicators:
                                if indicator_ in headings_list[j][1].lower():
                                    if not j+1==len(headings_list):
                                        returned_text_complete=returned_text.rsplit(headings_list[j+1][1].lstrip('0123456789.-').strip(),1)[0]
                                    else:
                                        returned_text_complete=returned_text 
                                else:        
                                    returned_text_complete=returned_text.rsplit(headings_list[j][1].lstrip('0123456789.-').strip(),1)[0]
                    else:
                        returned_text_complete=returned_text 
                    return returned_text_complete   
                except:
                    return get_references2([text,'check'])
                  
    return get_references2([text,'check'])


def get_references2(raw_text):
    pre_info=[]
    if not isinstance(raw_text, str):
        raw_text=raw_text[0].lower()
    listed_references_cluttered=gr.get_references(raw_text)
    if listed_references_cluttered:
        listed_references=gr.remove_clutter(listed_references_cluttered)
        clean_references=[]
        for item in listed_references:
            if not item.isdigit()==True and not item=="en" and not item =="\xa0" and not item==' ' and not item=='' and not '\ten' in item:
                clean_references.append(item)    
        pre_info.append(clean_references)
    else:
        pre_info.append("no list")
    return pre_info
       
def get_references(headings_list,raw_text):
    list_of_reference_indicators=["bibliography","references","reference"]
    reference_text_complete=get_part_of_text(headings_list,list_of_reference_indicators,raw_text)
    if not isinstance(reference_text_complete, str):
        return reference_text_complete[0]
    if reference_text_complete=='ll':
        return 'll'
        
    raw_references=reference_text_complete.split('\n')
    reference_list=[]
    for item in raw_references:
        if not item.isdigit()==True and not item=="en" and not item =="\xa0" and not item==' ' and not item=='' and not '\tEN' in item:
            reference_list.append(item)
        elif '□' in item:
            return None
    return reference_list        

def get_monitoring_and_evaluation(headings_list,raw_text):
    list_of_MandE_indicators=['monitoring and evaluation','monitoring']                       
    MandE_text_complete=get_part_of_text(headings_list,list_of_MandE_indicators,raw_text)
    if not isinstance(MandE_text_complete,str):
        return None
    count=len(re.findall(r'\w+', MandE_text_complete))
    return ('Yes',count)    
    
def get_headings(filename):
    os.chdir('..')
    rd.open_location("/PDF",True)
    filename_=filename[:-14]

    for compare_filename in os.listdir(os.getcwd()):

        if filename_ == compare_filename[:-4]:
            in_file=open(compare_filename, 'rb')
            
            parse_file=PDFParser(in_file)
            file=PDFDocument(parse_file)
            pages=0
            for page in PDFPage.get_pages(in_file):
                pages+=1   
            headings_list=[]
            try:
                for (level,title,dest,a,structelem) in file.get_outlines():
                    headings_list.append((level,title))
                rd.open_location("/program",True)    
                return headings_list,pages
            except:
                rd.open_location("/program",True)
                return None,pages

def combine(raw_text,filename,info_footnotes):

    filename=filename[:-14]
    for i in range(0,len(info_footnotes[0])):
        if filename == info_footnotes[0][i][:-18]:
            for x in info_footnotes[2][i]:
                raw_text+=" %s"% (x)
            break    
    links=lt.execute(raw_text)
    return [links,info_footnotes[1][i],info_footnotes[2][i]]

def has_TOC(headings_list,raw_text_lower):
    if headings_list:
        for heading in headings_list:
            if 'table of content' in str(heading).lower() or 'contents' in str(heading).lower():
                return 'yes'
            else:
                if 'table of content' in raw_text_lower or 'contents' in raw_text_lower:
                    return 'yes'
                else:
                    return 'no'               
    else:
        if 'table of content' in raw_text_lower or 'contents' in raw_text_lower:
            return 'yes'
        else:
            return 'no'          
    
def find_m(raw_text_lower):
    if 'monitoring and evaluation' in raw_text_lower or 'evaluation and monitoring' in raw_text_lower:
        return('yes',1)
    else:
        return('no',0)
    

    
def execute(info_footnotes):
    info=[]
    rd.open_location("/DOCX",True)
    for filename in os.listdir(os.getcwd()):

        if filename.endswith(".docx"):
            headings_list,pages=get_headings(filename)
            rd.open_location("/DOCX",False)
            raw_text=docx2txt.process(filename)
            raw_text_lower=raw_text.lower()
            TOC=has_TOC(headings_list,raw_text_lower)
            iainfo=gi.execute(raw_text_lower)
            links=combine(raw_text,filename,info_footnotes)
           
            if headings_list==None:
               back=get_references2(raw_text_lower)
               me=find_m(raw_text_lower)
               if back[0]=="no list":
                   info.append([filename,back[0],me,pages,iainfo,links[0],links[1],links[2],TOC])
               else:
                   info.append([filename,back[0],me,pages,iainfo,links[0],links[1],links[2],TOC])
            else:    
                references=get_references(headings_list,raw_text)
                monitoring_and_evaluation=get_monitoring_and_evaluation(headings_list,raw_text)
                info.append([filename,references,monitoring_and_evaluation,pages,iainfo,links[0],links[1],links[2],TOC])            
                
    return info        