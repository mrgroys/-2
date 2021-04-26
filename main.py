from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler

k = 0


def start(update, context):
    global k
    update.message.reply_text(
        "Привет! Если хочешь, то можешь пройти небольшой тест из 8 вопросов на знание аккордов для гитары.\n"
        "Ты можешь прервать тест, послав команду /stop.\n"
        "1)Какой это аккорд?")
    context.bot.send_photo(update.message.chat_id, photo=open('1c.jpg', 'rb'))
    k = 0
    return 1


def one(update, context):
    global k
    ot1 = update.message.text
    if ot1 == '/stop':
        k = 0
        return ConversationHandler.END
    if ot1 == 'Em' or ot1 == 'em':
        k += 1
    update.message.reply_text('2)Какой это аккорд?')
    context.bot.send_photo(update.message.chat_id, photo=open('2c.jpg', 'rb'))
    return 2


def two(update, context):
    global k
    ot1 = update.message.text
    if ot1 == '/stop':
        k = 0
        return ConversationHandler.END
    if ot1 == 'am' or ot1 == 'Am':
        k += 1
    update.message.reply_text('3)Какой это аккорд?')
    context.bot.send_photo(update.message.chat_id, photo=open('3c.jpg', 'rb'))
    return 3


def three(update, context):
    global k
    ot1 = update.message.text
    if ot1 == '/stop':
        k = 0
        return ConversationHandler.END
    if ot1 == 'Dm' or ot1 == 'dm':
        k += 1
    update.message.reply_text('4)Какой это аккорд?')
    context.bot.send_photo(update.message.chat_id, photo=open('4c.jpg', 'rb'))
    return 4


def four(update, context):
    global k
    ot1 = update.message.text
    if ot1 == '/stop':
        k = 0
        return ConversationHandler.END
    if ot1 == 'C' or ot1 == 'c':
        k += 1
    update.message.reply_text('5)Какой это аккорд?')
    context.bot.send_photo(update.message.chat_id, photo=open('5c.jpg', 'rb'))
    return 5


def five(update, context):
    global k
    ot1 = update.message.text
    if ot1 == '/stop':
        k = 0
        return ConversationHandler.END
    if ot1 == 'E' or ot1 == 'e':
        k += 1
    update.message.reply_text('6)Какой это аккорд?')
    context.bot.send_photo(update.message.chat_id, photo=open('6c.jpg', 'rb'))
    return 6


def six(update, context):
    global k
    ot1 = update.message.text
    if ot1 == '/stop':
        k = 0
        return ConversationHandler.END
    if ot1 == 'A' or ot1 == 'a':
        k += 1
    update.message.reply_text('7)Какой это аккорд?')
    context.bot.send_photo(update.message.chat_id, photo=open('7c.jpg', 'rb'))
    return 7


def seven(update, context):
    global k
    ot1 = update.message.text
    if ot1 == '/stop':
        k = 0
        return ConversationHandler.END
    if ot1 == 'D' or ot1 == 'd':
        k += 1
    update.message.reply_text('8)Какой это аккорд?')
    context.bot.send_photo(update.message.chat_id, photo=open('8c.jpg', 'rb'))
    return 8


def eight(update, context):
    global k
    ot1 = update.message.text
    if ot1 == '/stop':
        k = 0
        return ConversationHandler.END
    if ot1 == 'G' or ot1 == 'g':
        k += 1
    update.message.reply_text(f'Ваш результат: {k}/8.')
    return ConversationHandler.END


def stop(update, context):
    global k
    k = 0
    return ConversationHandler.END


def main():
    updater = Updater('1720954108:AAFP9bn3No-s9kMzSWpT-YIDvA0Oww95Cig', use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(Filters.text, one)],
            2: [MessageHandler(Filters.text, two)],
            3: [MessageHandler(Filters.text, three)],
            4: [MessageHandler(Filters.text, four)],
            5: [MessageHandler(Filters.text, five)],
            6: [MessageHandler(Filters.text, six)],
            7: [MessageHandler(Filters.text, seven)],
            8: [MessageHandler(Filters.text, eight)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
