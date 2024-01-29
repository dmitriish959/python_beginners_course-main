import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Замените 'YOUR_TOKEN' на ваш токен от BotFather
TOKEN = 'YOUR_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот для поиска товаров на Ozon. Введите /search <товар>, чтобы найти товар на Ozon.')

def search(update: Update, context: CallbackContext) -> None:
    query = ' '.join(context.args)
    response = requests.get(f'https://api.ozon.ru/search/v2?keyword={query}')
    if response.status_code == 200:
        products = response.json()['result']['items']
        for product in products:
            update.message.reply_text(f"{product['name']}: {product['price']} рублей")
    else:
        update.message.reply_text('Произошла ошибка при поиске товара.')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('search', search))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()