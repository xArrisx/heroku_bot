import telebot
from config import token
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    buttons = types.InlineKeyboardMarkup()
    btn_github = types.InlineKeyboardButton(text='github', url='https://github.com/xArrisx/teleBot')
    btn_youtube = types.InlineKeyboardButton(text='youtube', url='https://www.youtube.com/watch?v=YdCzZvDgBjQ&t=2918s')
    buttons.add(btn_github, btn_youtube)
    bot.send_message(message.chat.id, 'как дкла красава__?', reply_markup=buttons)



if __name__ == '__main__':
    bot.polling(none_stop=True)