# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:53:12 2016

@author: gebruiker
"""
import os
import re
import rd
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import Get_archive_url as gau
from multiprocessing import Pool

from urllib.parse import urlparse
from threading import Thread
import http.client, sys
from multiprocessing import JoinableQueue
from multiprocessing import Pool

concurrent = 200

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = http.client.HTTPConnection(url.netloc)   
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        return res.status, ourl
    except:
        return "error", ourl

def doSomethingWithResult(status, url):
    print (status, url)

unique_links=list(['http://www.esa.int/esaLP/SEMJZ10DU8E_LPgmes_0.html', 'http://ec.europa.eu/enterprise/space/off_docs_en.html', 'http://ec.europa.eu/enterprise/space_research/pdf/gosis.pdf', 'http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:52008SC0112:EN:HTML', 'http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=COM:2008:0046:FIN:EN:PDF', 'http://eurlex.europa.eu/Notice.do?val=464212:cs&lang=en&list=464212:cs,&pos=1&page=1&nbl=1', 'http://ec.europa.eu/enterprise/calls/files/08_004/rpa_study.pdf', 'http://eur-lex.europa.eu/LexUriServ/site/en/com/2003/com2003_0017en01.pdf', 'http://ec.europa.eu/comm/space/whitepaper/whitepaper/whitepaper_en.html', 'http://ec.europa.eu/enterprise/space/doc_pdf/pep.pdf', 'http://ec.europa.eu/comm/space/news/article_2262.pdf', 'http://ec.europa.eu/enterprise/space/doc_pdf/impact_assessment_en.pdf', 'http://www.gmes.info/library/index.php?&direction=0&order=&directory=6.%20CrossCutting%20Studies%20Documents', 'http://www.gmes.info/library/index.php?&direction=0&order=&directory=6.%20CrossCutting%20Studies%20Documents', 'http://inspire.jrc.it/reports/inspire_extended_impact_assessment.pdf', 'http://inspire.jrc.it/reports/AANSDI_Italy_FinalApproved_v12en.pdf', 'http://www.ec-gis.org/ginie/doc/ginie_book.pdf', 'http://www.ec-gis.org/sdi/ws/costbenefit2006/reports/report_sdi_crossbenefit%20.pdf', 'http://www.ec-gis.org/sdi/ws/costbenefit2006/reference/ROI_Study.pdf', 'http://www.oecd.org/dataoecd/29/33/40200582.pdf', 'http://www.oecd.org/document/13/0,2340,en_2649_34815_35059341_1_1_1_1,00.html', 'http://www.ravi.nl/ruimte/index.htm', 'http://www.micus.de/pdf/micus_study_broadband.pdf', 'http://www.weather.gov/sp/Borders_report.pdf', 'http://epi.yale.edu/Home', 'http://www.esa.int/esaLP/SEMJZ10DU8E_LPgmes_0.html.'])


if __name__ == '__main__':
    q = JoinableQueue(concurrent * 2)
    for i in unique_links:
        t = Thread(target=doWork)
        t.daemon = True
        t.start()
    try:
        for url in unique_links:
            q.put(url.strip())
        q.join()
    except KeyboardInterrupt:
        sys.exit(1)



"""Checks a diretory for files,extracts all hyperlinks and validates them as valid(still reachable) or invalid(no longer reachable)"""
def get_links():
    """Changes the active directory"""
    rd.open_location('/HTM',False)
    """Creates a dictionary to store valid and invalid hyperlinks"""    
    dict_links={}
    """Loops through all files in the directory with extension htm"""    
    for filename in os.listdir(os.getcwd()):
        all_links=[]
        cleaned_links=[]
        if filename.endswith(".htm"):
            html=open(filename,'r')
            soup=BeautifulSoup(html)
            """Gets all links from a single file and puts them in a list"""
            for link in soup.findAll('a'):
                all_links.append(link.get('href'))
            for i in range(0,len(all_links)):
                if not all_links[i].startswith('#') and not all_links[i]=='http://www.pdfonline.com/pdf-to-word-converter/':
                    cleaned_links.append(all_links[i])
        """Makes a set of the list to remove any duplicates"""                    
        unique_links=set(cleaned_links)
        """Validates all links in the list(it checks if you can still reach the hyperlink)"""      
        good_hyperlink,failed_hyperlink,total,total_valid=validate_links(unique_links)
        """Updates the dictionary with the filename as the key and with valid hyperlinks and invalid hyperlinks as the values"""         
        dict_links.update({filename:(good_hyperlink,failed_hyperlink)})  
    return dict_links,total,total_valid

"""Part of get_links(). Here is the actual validation part """      
def validate_links(unique_links) :
    total=[]
    total_valid=[]
    failed_hyperlink=[]
    good_hyperlink=[]
    """Loops through all links in unique_links"""
    for url in unique_links:
        """Checks if there are any non ascii symbols in the link"""
        x=None
        x=re.sub('[\x00-\x7f]','',url)
        """Checks if the link is valid"""        
        try:
            if not x:
                rqst = urlopen(url)
                good_hyperlink.append(url)
                total.append(url)
                total_valid.append(url)
            else:
                failed_hyperlink.append(url)
                total.append(url)
        except urllib.error.HTTPError as e:
                failed_hyperlink.append(url)
                total.append(url)
        except urllib.error.URLError as e:
                failed_hyperlink.append(url)
                total.append(url)  
    return good_hyperlink, failed_hyperlink, total, total_valid  

"""Checks for all invalid links if there are older cached versions available"""
def check_invalid_links(values):
    """creates a dictionary with the filename as key and with valid hyperlinks, invalid hyperlinks and cashed hyperlinks as the values """
    """Loops through all invalid links and checks for cashed versions"""
    links=[]    
    for link in values:
        archived_link=gau.execute(link)
        if not archived_link=='' and not archived_link==None:
            links.append(archived_link)              
    return links   

def execute(links):
    pool=multiprocessing.Pool(processes=4)
    pool.map(validate_links,links)
         
def execute2():
    dict_links,total,total_valid=get_links()
    dict_links_extended=check_invalid_links(dict_links)
    return dict_links_extended

#execute()   
              
                