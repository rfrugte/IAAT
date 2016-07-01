# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 16:17:10 2016

@author: gebruiker
"""
import ast
 

    
def execute(raw_text):
   if 'com (' in raw_text:
       raw_text=raw_text.replace('com (','com(')
       splitted=raw_text.split()
   if 'sec (' in raw_text:
       raw_text=raw_text.replace('sec (','sec(')
       splitted=raw_text.split()    
   splitted=raw_text.split()
   name=[]
   name_sec=[]
   for word in range(0,len(splitted)):
        if splitted[word].startswith('com(') or splitted[word].startswith('c(') or splitted[word].startswith('{com(') or splitted[word].startswith('{c(') or splitted[word].startswith('com ('):
            if not splitted[word]==splitted[-1]: 
                index_next=splitted[word+1]
                if splitted[word].startswith('{'):
                    splitted[word]=splitted[word][1:]
                name.append([splitted[word],index_next])
            else:    
                name.append([splitted[word]])
                
        elif 'com(' in splitted[word]:
            sen=''.join(('com(',splitted[word].split('com(',1)[1]))
            splitted2=sen.split()
            for word2 in range(0,len(splitted2)):
                if splitted2[word2].startswith('com(') or splitted2[word2].startswith('c(') or splitted2[word2].startswith('{com(') or splitted2[word2].startswith('{c(') or splitted2[word2].startswith('com ('):
                    if not splitted[word]==splitted[-1]: 
                        index_next=splitted[word+1]
                        if splitted2[word2].startswith('{'):
                            splitted2[word2]=splitted2[word2][1:]   
                        name.append([splitted2[word2],index_next]) 
                    else:
                        name.append([splitted2[word2]])
                        
        elif 'c(' in splitted[word] and not 'ec(' in splitted[word]:
            sen=''.join(('c(',splitted[word].split('c(',1)[1]))

            splitted3=sen.split()
            for word3 in range(0,len(splitted3)):
                if splitted3[word3].startswith('com(') or splitted3[word3].startswith('c(') or splitted3[word3].startswith('{com(') or splitted3[word3].startswith('{c(') or splitted3[word3].startswith('com ('):
                    if not splitted[word]==splitted[-1]: 

                        index_next=splitted[word+1]
                        if splitted3[word3].startswith('{'):
                            splitted3[word3]=splitted[word][1:]
                        name.append([splitted3[word3],index_next])
                    else:    
                        name.append([splitted3[word3]])                        
                        
        if splitted[word].startswith('sec(') or splitted[word].startswith('{sec(') or splitted[word].startswith('{swd(') or splitted[word].startswith('swd('):
            if not splitted[word]==splitted[-1]:            
                index_next=index_next=splitted[word+1]
                if splitted[word].startswith('{'):
                    splitted[word]=splitted[word][1:]
                name_sec.append([splitted[word],index_next])
            else:
                name_sec.append([splitted[word]])
                
                
        elif 'sec(' in splitted[word]:
            sen=''.join(('sec(',splitted[word].split('sec(',1)[1]))
            splitted4=sen.split()
            for word4 in range(0,len(splitted4)):
                if splitted4[word4].startswith('sec(') or splitted4[word4].startswith('{sec(') or splitted4[word4].startswith('{swd(') or splitted4[word4].startswith('swd('):
                    if not splitted[word]==splitted[-1]: 
                        index_next=splitted[word+1]
                        if splitted4[word4].startswith('{'):
                            splitted4[word4]=splitted4[word4][1:]   
                        name.append([splitted4[word4],index_next]) 
                    else:
                        name.append([splitted4[word4]])  
                        
        elif 'swd(' in splitted[word]:
            sen=''.join(('swd(',splitted[word].split('swd(',1)[1]))
            splitted4=sen.split()
            for word4 in range(0,len(splitted4)):
                if splitted4[word4].startswith('sec(') or splitted4[word4].startswith('{sec(') or splitted4[word4].startswith('{swd(') or splitted4[word4].startswith('swd('):
                    if not splitted[word]==splitted[-1]: 
                        index_next=splitted[word+1]
                        if splitted4[word4].startswith('{'):
                            splitted4[word4]=splitted4[word4][1:]   
                        name.append([splitted4[word4],index_next]) 
                    else:
                        name.append([splitted4[word4]])                  
   if name:
       return (name, name_sec)
   elif name_sec:
       return (name, name_sec)
 
def get(listy):    
    real=[]    
    listy=[l for l in listy if l is not None]    
    for k in range(0,len(listy)):
        for t in range(0,len(listy[k])):
            if not listy[k][t]==[]:
                if len(listy[k][t])>1:
                    for y in range(0,len(listy[k][t])):
                        
                        if listy[k][t][y][0].endswith(')') and len(listy[k][t][y])>1:            
                            name_s=' '.join((listy[k][t][y][0],listy[k][t][y][1]))
                            real.append(name_s)
                        else:
                            real.append(listy[k][t][y][0])    
                else: 
                    if len(listy[k][t][0])>1:
                        if listy[k][t][0][0].endswith(')'):            
                            name_s=' '.join((listy[k][t][0][0],listy[k][t][0][1]))
                            real.append(name_s)
                        else:
                            real.append(listy[k][t][0][0])
                    else:
                        real.append(listy[k][t][0][0])
    return real 

def clean(refs):
    clean_refs=[]
    for ref in refs:
        while not ref[-1].isdigit():
            ref= ref[:-1]
        if ') ' in ref:
            ref=ref.replace(') ',')')
            clean_refs.append(ref)
        else:
            clean_refs.append(ref)
    return clean_refs

def year(clean_refs):
    compl=[]
    for ia in clean_refs:        
        year = ia[ia.find("(")+1:ia.find(")")]
        compl.append((ia,year))
    return compl 
    
def run(footnoteso):
    for j in range(0,len(footnoteso)):
        footnotes=[]
        for r in footnoteso[j][7]:
            footnotes.append(r)
            listy=[]
            for i in footnotes:
                listy.append(execute(i.lower())) 
            refs=get(listy)
            clean_refs=clean(refs)
            compl=year(clean_refs)
        footnoteso[j].append(compl)
    return footnoteso            

