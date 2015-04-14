#created by Ajay M S


import urllib
from bs4 import BeautifulSoup
import urlparse
import requests
import re
import numpy as np
from Document import Doc
def getData(newsurls):
    print "getting data"
    docId=0
    docDump=[]
    docContentList=[]

    for urls in newsurls:
        r=requests.get(urls)
        htmlcontent=BeautifulSoup(r.content)
        g_data=htmlcontent.find_all("div",{"class":"maincontent news col-lg-9 col-md-9 col-sm-9"})
        for items in g_data:
            title= items.find("h1").text
            content = items.find_all("p",{"class":"FORMAT-BODY","class":"FORMAT-WRITER"})
            l=[]
            l.append(title)
            for cont in content:
                l.append(cont.text) 
            singlecontent=' '.join(l)
            doc= Doc(docId,title,urls,singlecontent)
            docDump.append(doc)
            docContentList.append(singlecontent)
            docId=docId+1
    print "finsished scraping"
    return docDump,docContentList
