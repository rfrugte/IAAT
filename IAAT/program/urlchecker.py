# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:09:37 2016

@author: gebruiker
"""
import multiprocessing
import os
import cProfile
import re
import Get_archive_url as gau
import urllib
import concurrent.futures
from urllib.request import urlopen


def validate_links(url) :
    failed_hyperlink=[]
    good_hyperlink=[]
    """Checks if there are any non ascii symbols in the link"""
    x=None
    x=re.sub('[\x00-\x7f]','',url)
    """Checks if the link is valid"""        
    try:
        if not x:
            rqst = urlopen(url)
            good_hyperlink.append(url)
        else:
            failed_hyperlink.append(url)
    except urllib.error.HTTPError as e:
            failed_hyperlink.append(url)
    except urllib.error.URLError as e:
            failed_hyperlink.append(url)
    except ValueError:
            failed_hyperlink.append(url) 
#    except: 
#            failed_hyperlink.append(url)
    return good_hyperlink,failed_hyperlink

def check_invalid_links(values):
    """creates a dictionary with the filename as key and with valid hyperlinks, invalid hyperlinks and cashed hyperlinks as the values """
    """Loops through all invalid links and checks for cashed versions"""

    links=[]    
    for link in values:
        archived_link=gau.execute(link)
        if not archived_link=='' and not archived_link==None:
            links.append(archived_link)              
    return links  

    
#k=list(['http://www.esa.int/esaLP/SEMJZ10DU8E_LPgmes_0.html', 'http://ec.europa.eu/enterprise/space/off_docs_en.html', 'http://ec.europa.eu/enterprise/space_research/pdf/gosis.pdf', 'http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:52008SC0112:EN:HTML', 'http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=COM:2008:0046:FIN:EN:PDF', 'http://eurlex.europa.eu/Notice.do?val=464212:cs&lang=en&list=464212:cs,&pos=1&page=1&nbl=1', 'http://ec.europa.eu/enterprise/calls/files/08_004/rpa_study.pdf', 'http://eur-lex.europa.eu/LexUriServ/site/en/com/2003/com2003_0017en01.pdf', 'http://ec.europa.eu/comm/space/whitepaper/whitepaper/whitepaper_en.html', 'http://ec.europa.eu/enterprise/space/doc_pdf/pep.pdf', 'http://ec.europa.eu/comm/space/news/article_2262.pdf', 'http://ec.europa.eu/enterprise/space/doc_pdf/impact_assessment_en.pdf', 'http://www.gmes.info/library/index.php?&direction=0&order=&directory=6.%20CrossCutting%20Studies%20Documents', 'http://www.gmes.info/library/index.php?&direction=0&order=&directory=6.%20CrossCutting%20Studies%20Documents', 'http://inspire.jrc.it/reports/inspire_extended_impact_assessment.pdf', 'http://inspire.jrc.it/reports/AANSDI_Italy_FinalApproved_v12en.pdf', 'http://www.ec-gis.org/ginie/doc/ginie_book.pdf', 'http://www.ec-gis.org/sdi/ws/costbenefit2006/reports/report_sdi_crossbenefit%20.pdf', 'http://www.ec-gis.org/sdi/ws/costbenefit2006/reference/ROI_Study.pdf', 'http://www.oecd.org/dataoecd/29/33/40200582.pdf', 'http://www.oecd.org/document/13/0,2340,en_2649_34815_35059341_1_1_1_1,00.html', 'http://www.ravi.nl/ruimte/index.htm', 'http://www.micus.de/pdf/micus_study_broadband.pdf', 'http://www.weather.gov/sp/Borders_report.pdf', 'http://epi.yale.edu/Home', 'http://www.esa.int/esaLP/SEMJZ10DU8E_LPgmes_0.html.'])

def sort(links):
    valid_hyperlink=[]
    invalid_hyperlink=[]
    for i in links:
        if i[0]:
            valid_hyperlink.append(i[0][0])
        else:
            invalid_hyperlink.append(i[1][0])   
    return valid_hyperlink, invalid_hyperlink 


#def new(invalid_hyperlink):
#    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool2:
#        results = pool2.map(check_invalid_links, invalid_hyperlink)
#    archived_links=list(results)  
#    return archived_links
    
def execute(k,archived):
    valid_hyperlink=[]
    invalid_hyperlink=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as pool:
        results = pool.map(validate_links, k)  
        
    links=list(results)
    valid_hyperlink, invalid_hyperlink=sort(links)
    #concurrent.futures.Executor.shutdown(1)
    #print(' i')
    if archived:
        archived_links=check_invalid_links(invalid_hyperlink)
    else:
        archived_links=['not checked']
    #archived_links=new(invalid_hyperlink)   
    
    return valid_hyperlink, invalid_hyperlink, archived_links

#f=execute(k)
