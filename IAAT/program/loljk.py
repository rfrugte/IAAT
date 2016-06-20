# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 01:06:45 2016

@author: gebruiker
"""

import networkx as nx
import matplotlib.pyplot as plt
ll=[]
for i in data:
    if not i[10]==[] and not i[4][0][0]==[] and not i[4][0][0]==None :
        for t in range(0,len(i[10])):
            i[4][0][0]=i[4][0][0].replace(' ','')
            i[4][0][0]=i[4][0][0].replace('final','')
            ll.append((i[4][0][0],i[10][t][0]))
strd=''
for i in ll:
    x=i[0]
    y=i[1]    
    strd=strd+('"%s"->"%s",'%(x,y))            
strd=strd[:-1]
fl='GraphPlot[{%s},VertexLabeling->True]'%(strd)        
        
    
def draw_graph(graph):

    # extract nodes from graph
    nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

    # create networkx graph
    G=nx.Graph()

    # add nodes
    for node in nodes:
        G.add_node(node)

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # draw graph
    pos = nx.shell_layout(G)
    nx.draw(G, pos)

    # show graph
    plt.show()

# draw example
graph = ll
draw_graph(graph)