import logging

from telegram impotr Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# ForceReply ?


#вкл логирование

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = loging.getLogger(__name__)


def start(engine: Update, context: CallbackContext) -> None:
    # Получаю имя пользователя указанное при регистрации
    user = engine.effective_user
    # Приветствие
    engine.message.reply_markdown_v2(
        fr'Привет, {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def halp_command(engine: Update, ontext: CallbackContext) -> None:
    engine.message.reply_text('Я сам себе помочь не могу, а ты еще тут клацаешь!')

def eche(engine: Update, context: CallbackContext) -> None:
    # Зеркалим запрос
    engine.message.reply_text(engine.message.text)

def main() -> None:
    from .gitignore import token
    car = Updater(token)
    dispatcher = car.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo ))
    engine.start_polling()
    engine.idle()

if __name__ == '__name__':
    main()