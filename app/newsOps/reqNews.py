import requests


class News:
  def __init__(self):
    self.newsUrl = "https://newsapi.org/v2/top-headlines?"

  def getNews(self, params):
    newsQuery = requests.get(self.newsUrl, params=params).json()
    return newsQuery


class NewsReq:
  def __init__(self):
    self.newsApiKey = "d0265273a0e54986a42cd2d721309914"
    self.worldNewsParams = {
      "apiKey": self.newsApiKey,
      "sources": "bbc-news"
    }
    self.businessNewsParams = {
      "apiKey": self.newsApiKey,
      "sources": "business-insider"
    }
    self.sportsNewsParams = {
      "apiKey": self.newsApiKey,
      "sources": "espn"
    }
    self.entNewsParams = {
      "apiKey": self.newsApiKey,
      "sources": "entertainment-weekly"
    }