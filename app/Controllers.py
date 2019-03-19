from .BarrtUi import BarrtUi
from .dbops import Dbops

#initializations
ui = BarrtUi()
db = Dbops()

class Controllers:

  def ctrlStart(self, barrtok, update):
    subscriber = db.retrUser(update.message.chat_id)
    if subscriber:
      barrtok.send_message(update.message.chat_id, ui.wlcMsg, reply_markup=ui.wlcKeyboard)
      

    else:
      barrtok.send_message(update.message.chat_id, ui.wlcMsg, reply_markup=ui.wlcKeyboard)
      userInfo = {
        "user_id": update.message.chat_id,
        "userName": update.message.chat.username,
        "preferedGenre": []
      }
      db.registrar(userInfo)


  def ctrlNewzGenre(self, barrtok, update):
    newsGenres = db.retrNewsGenres()
    if update.callback_query.data in newsGenres['categories']:
      prefGen = update.callback_query.data
      addGenreInfo = [update.callback_query.message.chat_id, prefGen, update.callback_query.message.chat.username]
      subbedans = db.newzGenreAdder(addGenreInfo)

      if subbedans == "subscribed":
        barrtok.send_message(update.callback_query.message.chat_id, "Genre already subscribed to")
      else:
        barrtok.send_message(update.callback_query.message.chat_id, "Genre selected")

    else:
      barrtok.send_message(update.callback_query.message.chat_id, "How on earth did you do that?")
