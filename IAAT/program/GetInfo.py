# -*- coding: utf-8 -*-
"""
Created on Sun May 15 19:22:12 2016

@author: gebruiker
"""
   
def execute(raw_text):    
   splitted=raw_text.split()
   name=[]
   name_sec=[]
   for word in splitted:
        if word.startswith('com(') or word.startswith('c(') or word.startswith('{com(') or word.startswith('{c('):
            index_next=splitted[splitted.index(word)+1]
            if word.startswith('{'):
                word=word[1:]
            name.append([word,index_next])
            
        if word.startswith('sec(') or word.startswith('{sec(') or word.startswith('{swd(') or word.startswith('swd('):
            index_next=splitted[splitted.index(word)+1]
            name_sec.append([word,index_next])
   if name: 
       name_s=' '.join((name[0][0],name[0][1]))
       if '}' in name_s:
           name_s=name_s[0:name_s.find('}')]
       if '{' in name_s:
           name_s=name_s[0:name_s.find('{')]
   else:
       name_s='none'
       name='none'
    #name_sec=[word for word in raw_text.split() if word.startswith('sec(')]
   if name_sec:    
       name_sec_s=' '.join((name_sec[0][0],name_sec[0][1])) 
   else:
       name_sec_s='none'
   if name and not name=='none':
       year = name[0][0][name[0][0].find("(")+1:name[0][0].find(")")]
   else:
       year=None
       name_s=None
       name_sec_s=None
   return ([name_s,name_sec_s],year)
    
#execute()