#created by Ajay M S

from Crawler import *
from Scrape import *
from MyCluster import *
import pandas as pd
from HtmlDisplay import *
def main():
    url = "http://www.purdue.edu/newsroom/"
    newsurl = "http://www.purdue.edu/newsroom/releases"
    
    newsurls=crawl(url,newsurl)

    docDump,docContentList= getData(newsurls)
    noOfClusters=5
    newsClusters=cluster(docDump,docContentList,noOfClusters)
    displayMainPage(newsClusters)
if __name__ == '__main__':
    main()
