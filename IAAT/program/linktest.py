# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 18:16:56 2016

@author: gebruiker
"""

def clean_links(links):
    clean_links=[]
    for link in links:
        if 'http.' in link:
            link=link.replace('http.','http:')
        if 'http' in link: 
            clean_links.append(link[link.index('http'):])
        else:
            clean_links.append(link)
    return clean_links
    
def get_links(raw_text):
    links=[]
    words=raw_text.split()
    
    for x in words:
        if 'http' in x:
            links.append(x)
        elif 'www.' in x:
            links.append(x)
    clean_link=clean_links(links)        
    return clean_link
    
def execute(raw_text):
    return set(get_links(raw_text))