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
#r=open('C:/Users/gebruiker/Desktop/testref.txt').read()
#x=r.split('\n')


def get_part_of_text(headings_list,list_of_indicators,text):
    for i in reversed(range(len(headings_list))):
        for indicator in list_of_indicators:        
            if indicator in headings_list[i][1].lower():
                #print(headings_list)
                try:
                    if len(headings_list[i][1])>15:
                        returned_text=text.split(headings_list[i][1][7:-2],1)[1]
                        returned_text=returned_text.split("Annex ",1)[0]
                        returned_text=returned_text.split("ANNEX ",1)[0]
                        returned_text=returned_text.split("annex ",1)[0]
                        returned_text=returned_text.split("APPENDIX ",1)[0]
                    else:    
                        returned_text=text.split(headings_list[i][1][4:],1)[1]
                        returned_text=returned_text.split("Annex ",1)[0]
                        returned_text=returned_text.split("ANNEX ",1)[0]
                        returned_text=returned_text.split("annex ",1)[0]
                        returned_text=returned_text.split("APPENDIX ",1)[0]
                    if not i+1==len(headings_list):
                        for j in range(i+1,len(headings_list)):
                            for indicator_ in list_of_indicators:
                                if indicator_ in headings_list[j][1].lower():
                                    if not j+1==len(headings_list):
                                        returned_text_complete=returned_text.split(headings_list[j+1][1][4:],1)[0]
                                    else:
                                        returned_text_complete=returned_text 
                                else:        
                                    returned_text_complete=returned_text.split(headings_list[j][1][4:],1)[0]
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
        #print(listed_references_cluttered)
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




    
def execute(info_footnotes):
    info=[]
    rd.open_location("/DOCX",True)
    for filename in os.listdir(os.getcwd()):

        if filename.endswith(".docx"):
            headings_list,pages=get_headings(filename)
            rd.open_location("/DOCX",False)
            raw_text=docx2txt.process(filename)
            raw_text_lower=raw_text.lower()
            #page_number=rd.get_pagenumber(raw_text)
            #links=lt.execute(raw_text)
            iainfo=gi.execute(raw_text_lower)
            links=combine(raw_text,filename,info_footnotes)
            if headings_list==None:
               back=get_references2(raw_text_lower)
               if back[0]=="no list":
                   info.append([filename,back,None,pages,iainfo,links[0],links[1],links[2]])
               else:
                   info.append([filename,back[0],None,pages,iainfo,links[0],links[1],links[2]])
            else:    
                references=get_references(headings_list,raw_text)
                monitoring_and_evaluation=get_monitoring_and_evaluation(headings_list,raw_text)
                info.append([filename,references,monitoring_and_evaluation,pages,iainfo,links[0],links[1],links[2]])            
                
    return info      
#text=docx2txt.process('C:/Users/gebruiker/Desktop/Demo/DOCX/CELEX%3A52008SC2086%3AEN%3ATXT.pdf_file.docx')
#anwb=text.split("References",1)[1]
#anwa=anwb.split("Annex",1)[0]
#nwe=anwa.split('\n')
#    
#execute() 
#pdd=[info]  
    
    
    
#def combine(raw_text,filename,info_footnotes):
#    links2=[]
#    links=lt.execute(raw_text)
#    filename=filename[:-14]
#    print('dfdf')
#    for i in range(0,len(info_footnotes[0])):
#        if filename in info_footnotes[0][i] and info_footnotes[3][i]:
#            links2.append(links)
#            links2.append(info_footnotes[3][i])
#            break
#    return links2
#    
#def execute(info_footnotes):
#    info=[]
#    rd.open_location("/DOCX")
#    print('wtf')
#    for filename in os.listdir(os.getcwd()):
#        print('kanker')
#        if filename.endswith(".docx"):
#            headings_list=get_headings(filename)
#            rd.open_location("/DOCX")
#            raw_text=docx2txt.process(filename)
#            
#            raw_text_lower=raw_text.lower()
#            links=combine(raw_text,filename,info_footnotes)
#            if headings_list==None:
#               back=get_references2(raw_text_lower)
#               info.append([filename,back])
#            else:    
#                references=get_references(headings_list,raw_text)
#                monitoring_and_evaluation=get_monitoring_and_evaluation(headings_list,raw_text)
#                info.append([filename,references,monitoring_and_evaluation,links])            
#    return info      