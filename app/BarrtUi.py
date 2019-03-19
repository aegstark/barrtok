from emoji import emojize
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from .dbops import Dbops


#initializations
db = Dbops()


class BarrtUi:
  def __init__(self):
    self.newzCatgs = db.retrNewsGenres()["categories"]
    self.wlcButtons = []
    for catg in self.newzCatgs:
      self.wlcButton = [InlineKeyboardButton(catg, callback_data=catg)]
      self.wlcButtons.append(self.wlcButton)

    self.wlcMsg = emojize("Hello there, I'm Barrtok :wave: :smile: \nPlease choose the categories you want", use_aliases=True)
    self.wlcKeyboard = InlineKeyboardMarkup(self.wlcButtons)