# -*- coding: utf-8 -*-
"""
Created on Mon May 30 22:21:35 2016

@author: gebruiker
"""
import ast
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline


def Get_training_data():
    new=os.path.dirname(os.path.abspath(__file__))
    os.chdir(new)
    r=open('trainingsset09062016.txt' ,'r')
    text=r.read()
    training_list= ast.literal_eval(text)
    return training_list

def train_sgdc(training_list):
    footnotes=[]
    cate=[]
    for i in training_list:
        footnotes.append(i[0])
        cate.append(i[1])
    #count_vect = CountVectorizer()    
    text_clf=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf',SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3,n_iter=5, random_state=42)),])
    _ = text_clf.fit(footnotes,cate)
    return text_clf    
    
def categorize_footnotes(working_list,text_clf):
    check2={}
    for i in range(0,len(working_list)):
        notes=working_list[i][-2]
        predicted= text_clf.predict(notes)
        predicted_footnotes=predicted.tolist()
        working_list[i].append(predicted_footnotes)
    return working_list

def execute(working_list):
    training_data=Get_training_data()
    text_clf=train_sgdc(training_data)
    working_list=categorize_footnotes(working_list,text_clf)
    return working_list

#execute()    
