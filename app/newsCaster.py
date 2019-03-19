from .dbops import Dbops
import telegram
from telegram.ext import Updater, Dispatcher

#Initilaizations
token = "752155752:AAHNxMiq7vkdVRH7sFcqzUKTpqjdqx-DxUQ"
barrtok = telegram.Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher
db = Dbops()

class NewsCaster:
  def castWorldNews(self):
    newz = db.fetchWorldNewsItems()
    subscribers = db.retrWorldUsers()
    for subscriber in subscribers:
      subbid = subscriber["subb_id"]
      for newIt in newz:
        newItem = newIt["auth"] + "\n" + newIt["title"] + "\n" + newIt["description"] + "\n" + str(newIt["news"]) + \
                  str(newIt["newsurl"])
        barrtok.send_message(subbid, newItem)
    db.newsDbDeleter("world")

  def castBusinessNews(self):
    newz = db.fetchBussNewsItems()
    subscribers = db.retrBussUsers()
    for subscriber in subscribers:
      subbid = subscriber["subb_id"]
      for newIt in newz:
        newItem = newIt["auth"] + "\n" + newIt["title"] + "\n" + newIt["description"] + "\n" + str(newIt["news"]) + \
                  str(newIt["newsurl"])
        barrtok.send_message(subbid, newItem)
    db.newsDbDeleter("business")

  def castSportsNews(self):
    newz = db.fetchSportsNewsItems()
    subscribers = db.retrSportsUsers()
    for subscriber in subscribers:
      subbid = subscriber["subb_id"]
      for newIt in newz:
        newItem = newIt["auth"] + "\n" + newIt["title"] + "\n" + newIt["description"] + "\n" + str(newIt["news"]) + \
                  str(newIt["newsurl"])
        barrtok.send_message(subbid, newItem)
    db.newsDbDeleter("sports")

  def castEntNews(self):
    newz = db.fetchEntNewsItems()
    subscribers = db.retrEntUsers()
    for subscriber in subscribers:
      subbid = subscriber["subb_id"]
      for newIt in newz:
        newItem = newIt["auth"] + "\n" + newIt["title"] + "\n" + newIt["description"] + "\n" + str(newIt["news"]) + \
                  str(newIt["newsurl"])
        barrtok.send_message(subbid, newItem)
    db.newsDbDeleter("entertainment")