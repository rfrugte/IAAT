# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:28:33 2016

@author: gebruiker
"""

from tkinter import *

allfootnotes=[]
law_footnote = []
journal_footnote=[]
data_footnote =[]
none_footnote =[]
und_footnote =[]

     
def split_footnotes(footnotes):

    for i in footnotes:
        l = i
        get_policy_law(l)
    
def start(working_list): 
    n=0
    for i in range(0,len(working_list)):
    #for i in range(0,1):
       x=working_list[i][7]
       for j in x:
           allfootnotes.append([j])
    for k in range(0,len(allfootnotes)):
        l=inter(allfootnotes[k],k,str(n))
        n+=1
    global allfootnotes 
    
def inter(footnote,k,n):

    master = Tk()
    global master
    
    
    w=Label(master,text=(footnote,n),wraplength=500,justify=CENTER)
   
    #y=Label(master,text=('Impact Assessment:  '+ name))      
    b=Button(master , text='Policy/Legal', command=lambda:policy(footnote,k))
    c=Button(master , text='Data/Reports', command=lambda:data(footnote,k))
    d=Button(master , text='Journal', command=lambda:journal(footnote,k))
    f=Button(master , text='Other', command=lambda:other(footnote,k))
    e=Button(master , text='Stop', command=lambda:destroys)
    #x.pack()
    w.pack()
    b.pack()
    c.pack()
    d.pack()
    f.pack()
    e.pack()
    master.mainloop()
     

def policy(footnote,k):
    law_footnote.append(footnote)
    allfootnotes[k].append('PolicyLaw')
    destroys()
    
def journal(footnote,k):
    journal_footnote.append(footnote)
    allfootnotes[k].append('Journal')
    destroys()
    
def other(footnote,k):
    none_footnote.append(footnote)
    allfootnotes[k].append('None')
    destroys()
    
def data(footnote,k):
    data_footnote.append(footnote)
    allfootnotes[k].append('Profdata')
    destroys()
    
def destroys():
    master.destroy()

def start2(check):  
       #name=check.keys()[i]
    name=list(check.keys())[7]
    footnotes=list(check.values())[7][7]
    split_footnotes(footnotes)
    for x in und_footnote:
        inter(x,name)
       
start(working_list)   