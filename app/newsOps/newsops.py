#imports
from app.newsOps.reqNews import News
from app.newsOps.reqNews import NewsReq
from app.dbops import Dbops

#initializations
nop = News()
nreq = NewsReq()
db = Dbops()

#worldNews = nop.getNews(nreq.worldNewsParams)["articles"]
#busNews = nop.getNews(nreq.businessNewsParams)["articles"]
#sportsNews = nop.getNews(nreq.sportsNewsParams)["articles"]
#entNews = nop.getNews(nreq.entNewsParams)["articles"]


#methods
def newsAuthor(news):
  author = news["author"]
  return author

def newsTitle(news):
  title = news["title"]
  return title

def newsDesc(news):
  desc = news["description"]
  return desc

def newsUrl(news):
  newsurl = news["url"]
  return newsurl

def newsImage(news):
  newsimg = news["urlToImage"]
  return newsimg

def publishDate(news):
  pdate = news["url"]
  return pdate

def newsActual(news):
  newscontent = news["content"]
  return newscontent

def getCurrentNews(newsType):
  newsArticles = []
  for article in newsType:
    author = newsAuthor(article)
    title = newsTitle(article)
    newsdescription = newsDesc(article)
    newsurl = newsUrl(article)
    imageurl = newsImage(article)
    publishdate = publishDate(article)
    newscontent = newsActual(article)
    newsData = {
      "auth": author,
      "title": title,
      "description": newsdescription,
      "newsurl": newsurl,
      "imageurl": imageurl,
      "publishdate": publishdate,
      "news": newscontent
    }
    newsArticles.append(newsData)
  return newsArticles


class LoggNews:
  def __init__(self):
    self.newsTypes = ["world", "business", "sports", "entertainment"]

  def getWorldNews(self):
    worldNews = nop.getNews(nreq.worldNewsParams)["articles"]
    newsInfo = getCurrentNews(worldNews)
    for article in newsInfo:
      db.newsDbCreator(self.newsTypes[0], article)

  def getBusNews(self):
    busNews = nop.getNews(nreq.businessNewsParams)["articles"]
    newsInfo = getCurrentNews(busNews)
    for article in newsInfo:
      db.newsDbCreator(self.newsTypes[1], article)

  def getSportsNews(self):
    sportsNews = nop.getNews(nreq.sportsNewsParams)["articles"]
    newsInfo = getCurrentNews(sportsNews)
    for article in newsInfo:
      db.newsDbCreator(self.newsTypes[2], article)

  def getEntNews(self):
    entNews = nop.getNews(nreq.entNewsParams)["articles"]
    newsInfo = getCurrentNews(entNews)
    for article in newsInfo:
      db.newsDbCreator(self.newsTypes[3], article)