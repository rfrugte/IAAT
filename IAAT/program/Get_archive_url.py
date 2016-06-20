# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:34:20 2016

@author: gebruiker
"""
import re
from urllib.request import urlopen

"""If present extracts the archived version from archive.org of the link provided and returs a link to the archived version"""
def execute(link):
    """Checks if any non ascii links present"""
    try:
        link.encode('ascii')
    except UnicodeEncodeError:
        n=None 
        """Checks if the provided link is archived and if present returns the url"""
    else:    
        url=''.join(["http://archive.org/wayback/available?url=",link])
        #url=''.join(["http://timetravel.mementoweb.org/memento/",link])
        res=urlopen(url).read().decode("utf-8")
        for i in res:
            if 'true' in res:
                archived_link=re.search('url":"(.*)","time',res).group(1)
            else:
                archived_link=''
        return archived_link    

#execute()
        
      