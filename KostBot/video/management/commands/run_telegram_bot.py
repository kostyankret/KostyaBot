from django.core.management.base import BaseCommand
from video.models import Video
import telebot

bot = telebot.TeleBot("6987220975:AAHkjSUEP-AFtC8WC56-wfrSqbAN7OrOy4I")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Команды: /add, /videos, /help, Привет")

@bot.message_handler(commands=['videos'])
def videos(message):
    videos = Video.objects.all()
    for video in videos:
        bot.send_message(message.chat.id, f"Название: {video.name}, URL: {video.url}")

@bot.message_handler(commands=['add'])
def add(message):
    bot.send_message(message.from_user.id, "Напишите название")
    bot.register_next_step_handler(message, title_handler)

def title_handler(message):
    global title
    title = message.text

    bot.send_message(message.chat.id, "Напишите URL")
    bot.register_next_step_handler(message, url_handler)

def url_handler(message):
    global url
    url = message.text
    bot.send_message(message.chat.id, f"Видео добавлено")
    new_video = Video.objects.create(name=title, url=url)

def new_video():
    video = Video(name=name, url=url)
    video.save()

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "/add /videos")

    else:
        bot.send_message(message.from_user.id, "Не понял? /help.")

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")