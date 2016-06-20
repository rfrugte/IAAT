# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 20:25:55 2016

@author: gebruiker
"""

from urllib.request import urlopen
def execute(info):
    for i in range(0,len(info)):
        gg=[]
        ia_info=info[i][-1]
        for j in range(0,len(ia_info)):
            if not len(ia_info[j])>1:
                gg.append('none')
            else:    
                year=ia_info[j][1]
                com=ia_info[j][0]
                if not len(year)==4:
                    gg.append('none')
                else:    
                    if not com:
                        gg.append('none')
                    else:    
                        com=com.replace(' ','')
                        try:
                            x=urlopen(''.join(('http://ec.europa.eu/smart-regulation/impact/ia_carried_out/cia_',year,'_en.htm'))).read()
                            x=x.decode(encoding='UTF-8') 
                            com=com.upper()
                    
                            if com in x:
                                text=x.split(com,1)[0]
                                index=text.rfind('<!--')
                                text_slice=text[index:]
                                DGs=text_slice[text_slice.find('<!--')+4:text_slice.find('-->')].strip()
                                DG=sort(DGs)
                                gg.append(DG)
                            else: 
                                gg.append('none')    
                        except:
                            gg.append('none')
        info[i].append(gg)                            
    return info    

 
def sort(DGs):
    text=DGs.lower()
    if text.startswith('agri'):
        return 'Agriculture and Rural Development (AGRI)'
    elif text.startswith('bud'):  
        return 'Budget (BUDG)'
    elif text.startswith('cli'): 
        return 'Climate Action (CLIMA)'
    elif text.startswith('comp'): 
        return 'Competition (COMP)'
    elif text.startswith('eco') or text.startswith('ecf'): 
        return 'Economic and Financial Affairs (ECFIN)'
    elif text.startswith('edu') or text.startswith('eac'):   
        return 'Education and Culture (EAC)'
    elif text.startswith('emp'): 
        return 'Employment, Social Affairs and Inclusion (EMPL)' 
    elif text.startswith('ene'): 
        return 'Energy (ENER)'
    elif text.startswith('env'): 
        return 'Environment (ENV)'  
    elif text.startswith('eur') or text.startswith('est'):   
        return 'Eurostat (ESTAT)'    
    elif text.startswith('fin') or text.startswith('fis'):   
        return 'Financial Stability, Financial Services and Capital Markets Union (FISMA)'
    elif text.startswith('hea') or text.startswith('san'):   
        return 'Health and Food Safety (SANTE)'    
    elif text.startswith('inf') or text.startswith('dig'):   
        return 'Informatics (DIGIT)' 
    elif text.startswith('interp') or text.startswith('sci'):
        return 'Interpretation (SCIC)'    
    elif text.startswith('joi') or text.startswith('jrc'):   
        return 'Joint Research Centre (JRC)'    
    elif text.startswith('jus'): 
        return 'Justice and Consumers (JUST)'
    elif text.startswith('mar'): 
        return 'Maritime Affairs and Fisheries (MARE)'    
    elif text.startswith('mig') or text.startswith('hom'):   
        return 'Migration and Home Affairs (HOME)'
    elif text.startswith('mob') or text.startswith('mov') or text.startswith('transp'):   
        return 'Mobility and Transport (MOVE)' 
    elif text.startswith('nei') or text.startswith('nea'):   
        return 'Neighbourhood and Enlargement Negotiations (NEAR)'
    elif text.startswith('reg'): 
        return 'Regional and urban Policy (REGIO)' 
    elif text.startswith('res') or text.startswith('rtd'):   
        return 'Research and Innovation (RTD)' 
    elif text.startswith('sec') or text.startswith('sg'):   
        return 'Secretariat-General (SG)'  
    elif text.startswith('ser') or text.startswith('fpi'):   
        return 'Service for Foreign Policy Instruments (FPI)'
    elif text.startswith('tax'): 
        return 'Taxation and Customs Union (TAXUD)'
    elif text.startswith('trad'): 
        return 'Trade (TRADE)'
    elif text.startswith('transl') or text.startswith('dgt'):   
        return 'Translation (DGT)'
    elif text.startswith('comm') or text.startswith('cne'):
        if 'cne' in text or 'net' in text:
            return 'Communications Networks, Content and Technology (CNECT)'
        else:    
            return 'Communication (COMM)'    
    elif text.startswith('hum') or text.startswith('ech') or text.startswith('hr'):
        if 'aid' in text or 'ech' in text:
            return 'Humanitarian Aid and Civil Protection (ECHO)'
        else:    
            return 'Human Resources and Security (HR)'    
    elif text.startswith('int') or text.startswith('gro') or text.startswith('dev'):
        if 'mark' in text or 'gro' in text:
            return 'Internal Market, Industry, Entrepreneurship and SMEs (GROW)'
        else:    
            return 'International Cooperation and Development (DEVCO)'    
    else:
        return text