#created by Ajay M S

class Doc:
    def __init__(self, idno, title, url, content):
      self.title = title
      self.content = content
      self.idno=idno  
      self.url=url
    def getId(self):
        return self.idno    
    def getTitle(self):
        return self.title
    def getContent(self):
        return self.content
    def getUrl(self):
        return self.url
