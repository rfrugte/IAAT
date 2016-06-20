# -*- coding: utf-8 -*-
"""
Created on Mon May 16 22:03:53 2016

@author: gebruiker
"""
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.grid_search import GridSearchCV
import numpy as np
import test
import random
from random import shuffle
import matplotlib.pyplot as plt


#print(sum(check2)/10)
#import rd

#lines = open('test2.txt', 'r', encoding ='utf-8').read().split('\n\n')


#f=sum(check)/1980
#check2=[]
#l=open('trainingsset09062016.txt','r')
#text=l.read()
#lijst_met_voetnoten= ast.literal_eval(text)
#df=lijst_met_voetnoten+lijst_met_voetnoten
#for g in range(0,1):
#    check=[]
#    for j in range(20,800): 
#        datar=[]
#        footr=[]
#        data=[]
#        foot=[]
#        x=random.sample(lijst_met_voetnoten,j)
#        for l in lijst_met_voetnoten:
#            if not l in x:
#                data.append(l[0])
#                foot.append(l[1])
#        for i in x:
#            datar.append(i[0])
#            footr.append(i[1])
#        
#        #data=footnotess[0::2]
#        #data2=footnotess[1::2]
#        
#        #result=cate[0::2]    
#        #results=cate[1::2]
#        count_vect = CountVectorizer()
#        
#        text_clf=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf',SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3,n_iter=5, random_state=42)),])
#        _ = text_clf.fit(datar,footr)
#        predicted=text_clf.predict(data[50:150])
#        check.append(np.mean(predicted==foot[50:150]))
##    for s in range(0,len(check2)):
##        
##        check2[s]=(check2[s]+check[s])/2 
##    print('x')    
#plt.plot(check)
#plt.show







l=open('trainingsset09062016.txt','r')
text=l.read()
lijst_met_voetnoten= ast.literal_eval(text)
shuffle(lijst_met_voetnoten)

for c in range(0,100):
    r=[lijst_met_voetnoten[i:i+110] for i in range(0,len(lijst_met_voetnoten),110)]
    check=[]
    for i in range(0,10):
        datar=[]
        footr=[]
        data=[]
        foot=[]
        training=[]
        test=r[i]
        for j in r:
            if not j==test:
                for k in j:
                    training.append(k)
        for a in training:
           datar.append(a[0])
           footr.append(a[1])             
    
        for b in test:
            data.append(b[0])
            foot.append(b[1])
            
    
        count_vect = CountVectorizer()
        
        text_clf=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf',SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3,n_iter=5, random_state=42)),])
        _ = text_clf.fit(datar,footr)
        predicted=text_clf.predict(data)
        check.append(np.mean(predicted==foot))

    for d in range(0,len(check2)):
        check2[d]=(check2[d]+check[d])/2 

plt.plot(check2)
plt.show
        
        
#print(metrics.classification_report(results,predicted))
#for i in check:
#    notes=check[i][7]
#    predicted= text_clf.predict(notes)
#    p=list(check[i])
#    x=predicted.tolist()
#    #r=check[i]+x
#    p.append(x)
#    p=tuple(p)
#    check2.update({i:(p)})
#global check2    

#print(np.mean(predicted==results))

#print(metrics.classification_report(results,predicted))

#parameters={'vect__ngram_range':[(1,1),(1,2)],'tfidf__use_idf':(True,False),'clf__alpha':(1e-2,1e-3),}
#gs_clf = GridSearchCV(text_clf,parameters,n_jobs=-1)
#gs_clf =gs_clf.fit(data[:3],result[:3])
#best_parameters,score,_=max(gs_clf.grid_scores_,key=lambda x: x[1])
#for param_name in sorted(parameters.keys()):
#    print("%s: %r" % (param_name, best_parameters[param_name]))
