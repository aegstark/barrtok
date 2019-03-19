import time
import schedule
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from app.Controllers import Controllers
from app.newsOps.newsops import LoggNews
from app.newsCaster import NewsCaster


#Initilaizations and Data
token = "752155752:AAHNxMiq7vkdVRH7sFcqzUKTpqjdqx-DxUQ"
barrtok = telegram.Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher
ctrl = Controllers()
mrnGetime = "10:16"
mrnCastime = "10:17"
aftGetime = "11:50"
aftCastime = "12:00"
eveGetime = "18:10"
eveCastime = "18:20"


def getBarrtok():
  print(barrtok.getMe().first_name)


def main():
  getBarrtok()

  newsLogger = LoggNews()
  nc = NewsCaster() 

  dispatcher.add_handler(CommandHandler("start", ctrl.ctrlStart))
  dispatcher.add_handler(CallbackQueryHandler(ctrl.ctrlNewzGenre))

  #Morning News
  schedule.every().day.at(mrnGetime).do(newsLogger.getWorldNews)
  schedule.every().day.at(mrnCastime).do(nc.castWorldNews)
  schedule.every().day.at(mrnGetime).do(newsLogger.getBusNews)
  schedule.every().day.at(mrnCastime).do(nc.castBusinessNews)
  schedule.every().day.at(mrnGetime).do(newsLogger.getSportsNews)
  schedule.every().day.at(mrnCastime).do(nc.castSportsNews)
  schedule.every().day.at(mrnGetime).do(newsLogger.getEntNews)
  schedule.every().day.at(mrnCastime).do(nc.castEntNews)

  #Afternoon News
  schedule.every().day.at(aftGetime).do(newsLogger.getWorldNews)
  schedule.every().day.at(aftCastime).do(nc.castWorldNews)
  schedule.every().day.at(aftGetime).do(newsLogger.getBusNews)
  schedule.every().day.at(aftCastime).do(nc.castBusinessNews)
  schedule.every().day.at(aftGetime).do(newsLogger.getSportsNews)
  schedule.every().day.at(aftCastime).do(nc.castSportsNews)
  schedule.every().day.at(aftGetime).do(newsLogger.getEntNews)
  schedule.every().day.at(aftCastime).do(nc.castEntNews)

  #Evening News
  schedule.every().day.at(eveGetime).do(newsLogger.getWorldNews)
  schedule.every().day.at(eveCastime).do(nc.castWorldNews)
  schedule.every().day.at(eveGetime).do(newsLogger.getBusNews)
  schedule.every().day.at(eveCastime).do(nc.castBusinessNews)
  schedule.every().day.at(eveGetime).do(newsLogger.getSportsNews)
  schedule.every().day.at(eveCastime).do(nc.castSportsNews)
  schedule.every().day.at(eveGetime).do(newsLogger.getEntNews)
  schedule.every().day.at(eveCastime).do(nc.castEntNews)

  updater.start_polling()

  while True:
      schedule.run_pending()
      time.sleep(1)


  

if __name__ == "__main__":
  main()