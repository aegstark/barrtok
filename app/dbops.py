#imports
import pymongo
from pymongo import MongoClient


#Initializations
extDBUrl = "mongodb://regalia:regalia18@barrtoktest-shard-00-00-p1aif.mongodb.net:27017,barrtoktest-shard-00-01-p1aif.mongodb.net:27017,barrtoktest-shard-00-02-p1aif.mongodb.net:27017/test?ssl=true&replicaSet=barrtoktest-shard-0&authSource=admin&retryWrites=true"
barrtokCli = MongoClient(extDBUrl)
barrtdb = barrtokCli['barrtdb']
barrtNewzCatgs = barrtdb['barrtNewzCatgs']
barrtUsers = barrtdb['barrtUsers']
worldNewzSubs = barrtdb['worldNewzSubs']
businessNewzSubs = barrtdb['businessNewzSubs']
sportsNewzSubs = barrtdb['sportsNewzSubs']
entNewzSubs = barrtdb['entNewzSubs']
worldNewzLogg = barrtdb['worldNewzLogg']
businessNewzLogg = barrtdb['businessNewzLogg']
sportsNewzLogg = barrtdb['sportsNewzLogg']
entNewzLogg = barrtdb['entNewzLogg']




#def superUserAddNewsCatgs(catgs):
  #print(catgs)
  #barrtNewzCatgs.insert_one(catgs)
  #categories = barrtNewzCatgs.find_one()
  #print(categories)

#categs = {"categories": ["World", "Business", "Sports", "Entertainment"]}
#superUserAddNewsCatgs(categs)



class Dbops:
  def retrNewsGenres(self):
    newzGenres = barrtNewzCatgs.find_one()
    return newzGenres

  def retrUser(self, userId):
    user = barrtUsers.find_one({"user_id": userId})
    return user

  def retrWorldUsers(self):
    users = worldNewzSubs.find()
    return users

  def retrBussUsers(self):
    users = businessNewzSubs.find()
    return users

  def retrSportsUsers(self):
    users = sportsNewzSubs.find()
    return users

  def retrEntUsers(self):
    users = entNewzSubs.find()
    return users

  def registrar(self, userInfo):
    barrtUsers.insert_one(userInfo)

  def checkGenreSub(self, subbId, genreColl):
    subber = genreColl.find_one({"subbName": subbId})
    if subber:
      subbStat = "subbed"
    else:
      subbStat = "notsubbed"
    return subbStat


  def newzGenreAdder(self, genreAddInfo):
    userid = genreAddInfo[0]
    userName = genreAddInfo[2]
    userrGenre = barrtUsers.find_one({"user_id": userid})["preferedGenre"]
    prefferedGenre = genreAddInfo[1]
    if prefferedGenre == "World":
      genreSubbedStatus = self.checkGenreSub(userName, worldNewzSubs)
      if genreSubbedStatus == "notsubbed":
        worldSubberInfo = {
          "subbName": genreAddInfo[2],
          "subb_id": genreAddInfo[0]
        }
        worldNewzSubs.insert_one(worldSubberInfo)
        userrGenre.append(genreAddInfo[1])
        barrtUsers.update_one({'user_id': genreAddInfo[0]}, {"$set": {"preferedGenre": userrGenre}}, upsert=False)
      else:
        genreSubbedStatus = "subscribed"

    elif prefferedGenre == "Business":
      genreSubbedStatus = self.checkGenreSub(userName, businessNewzSubs)
      if genreSubbedStatus == "notsubbed":
        buzSubberInfo = {
          "subbName": genreAddInfo[2],
          "subb_id": genreAddInfo[0]
        }
        businessNewzSubs.insert_one(buzSubberInfo)
        userrGenre.append(genreAddInfo[1])
        barrtUsers.update_one({'user_id': genreAddInfo[0]}, {"$set": {"preferedGenre": userrGenre}}, upsert=False)
      else:
        genreSubbedStatus = "subscribed"

    elif prefferedGenre == "Sports":
      genreSubbedStatus = self.checkGenreSub(userName, sportsNewzSubs)
      if genreSubbedStatus == "notsubbed":
        sportsSubberInfo = {
          "subbName": genreAddInfo[2],
          "subb_id": genreAddInfo[0]
        }
        sportsNewzSubs.insert_one(sportsSubberInfo)
        userrGenre.append(genreAddInfo[1])
        barrtUsers.update_one({'user_id': genreAddInfo[0]}, {"$set": {"preferedGenre": userrGenre}}, upsert=False)
      else:
        genreSubbedStatus = "subscribed"

    elif prefferedGenre == "Entertainment":
      genreSubbedStatus = self.checkGenreSub(userName, entNewzSubs)
      if genreSubbedStatus == "notsubbed":
        entSubberInfo = {
          "subbName": genreAddInfo[2],
          "subb_id": genreAddInfo[0]
        }
        entNewzSubs.insert_one(entSubberInfo)
        userrGenre.append(genreAddInfo[1])
        barrtUsers.update_one({'user_id': genreAddInfo[0]}, {"$set": {"preferedGenre": userrGenre}}, upsert=False)
      else:
        genreSubbedStatus = "subscribed"

    return genreSubbedStatus


  def newsDbCreator(self,newsType, newsData):
    if newsType == "world":
      worldNewzLogg.insert_one(newsData)
    elif newsType == "business":
      businessNewzLogg.insert_one(newsData)
    elif newsType == "sports":
      sportsNewzLogg.insert_one(newsData)
    elif newsType == "entertainment":
      entNewzLogg.insert_one(newsData)

  def newsDbDeleter(self, newsType):
    if newsType == "world":
      worldNewzLogg.delete_many({})
    elif newsType == "business":
      businessNewzLogg.delete_many({})
    elif newsType == "sports":
      sportsNewzLogg.delete_many({})
    elif newsType == "entertainment":
      entNewzLogg.delete_many({})


  def fetchWorldNewsItems(self):
    newsItems = []
    for newItem in worldNewzLogg.find():
      newsItems.append(newItem)
    return newsItems

  def fetchBussNewsItems(self):
    newsItems = businessNewzLogg.find()
    return newsItems

  def fetchSportsNewsItems(self):
    newsItems = sportsNewzLogg.find()
    return newsItems

  def fetchEntNewsItems(self):
    newsItems = entNewzLogg.find()
    return newsItems