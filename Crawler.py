#created by Ajay M S

import urllib
from bs4 import BeautifulSoup
import urlparse

def crawl(url,newsurl):
    print "start crawling"
    
    urls=[url]
    visited = [url]
    newsurls=[]
    while len(urls)>0:
        try:
            htmltext=urllib.urlopen(urls[0]).read()
        except:
            print "exception ",urls[0]
        soup=BeautifulSoup(htmltext)
        urls.pop(0)
        for tag in soup.findAll('a',href=True):
            tag['href']=urlparse.urljoin(url,tag['href'])
            if url in tag['href'] and tag['href'] not in visited:
                urls.append(tag['href'])
                visited.append(tag['href'])
                if newsurl in tag['href']:
                    newsurls.append(tag['href'])
    
    print "finsished crawling"
    return newsurls
