# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:25:14 2016

@author: gebruiker
"""
import CheckLinks as cl
import urlchecker as uc
def execute(working_list,archived):
    for i in range(0,len(working_list)):
        good_hyperlink,failed_hyperlink,archived_hyperlink,total,total_valid,total_archived=None,None,None,0,0,0
        
        if working_list[i][5]:
            good_hyperlink,failed_hyperlink,archived_hyperlink=uc.execute(working_list[i][5],archived)
        if not good_hyperlink==None or not failed_hyperlink==None:
            working_list[i].append(len(good_hyperlink)+len(failed_hyperlink))
        else:
            working_list[i].append(total)
        if failed_hyperlink:
            working_list[i].append(len(good_hyperlink))
        else:
            working_list[i].append(total_valid)
        if archived_hyperlink:
            working_list[i].append(len(archived_hyperlink))
        else:
            working_list[i].append(total_archived)
        
        

        working_list[i].append(good_hyperlink)
        working_list[i].append(failed_hyperlink)
        working_list[i].append(archived_hyperlink)
    return working_list    
    
#def execute2(working_list):
#    for i in range(0,len(working_list)):
#        if working_list[i][5]: 
#            good_hyperlink,failed_hyperlink,total,total_valid=None,None,0,0
#            cl(working_list[i][5])
#        if working_list[i][5]:
#            good_hyperlink,failed_hyperlink,total,total_valid=cl.validate_links(working_list[i][5])
#        if failed_hyperlink:
#            archived_hyperlink=cl.check_invalid_links(failed_hyperlink)
#        else:
#            archived_hyperlink=None
#        working_list[i].append(total)
#        working_list[i].append(total_valid)
#        working_list[i].append(good_hyperlink)
#        working_list[i].append(failed_hyperlink)
#        working_list[i].append(archived_hyperlink)
#    return working_list       