from telegram import Update
from telegram.ext import CommandHandler, MessageHandler,Filters, ConversationHandler, CallbackContext, Updater

class Organizador():

    def __init__(self, name):
        self.name = name
        self.nomes = []

    def leitorNome(self, update: Update, context: CallbackContext):
        
        chat_id = update.message.chat_id
        context.user_data["chat_id"] = chat_id
        context.user_data["nomes"] = []

        update.message.reply_text("Seja bem-vindo ao Organizador!\nEstou aqui para ajudar você a organizar as pastas em ordem alfabética.")
        update.message.reply_text("Por favor, digite os nomes separados por espaços ou vírgulas:")

        return "collecting_names"
    
    def collecting_names(self, update, context):

        text = update.message.text
        chat_id = update.message.chat_id

        if not text:
            update.massage.reply_text("Por favor, Digite pelo menos um nome.")
            return "collecting_names"
        
        nomes = [nome.strip() for nome in text.split(",")]
        context.user_data["nomes"] = nomes
        update.message.reply_text(f"Recebi os nomes: {', '.join(nomes)}")

        return "organizing_names"
    
    def organizing_names(self, update: Update, context: CallbackContext):

        if "nomes" not in con

        nomes = context.user_data["nomes"]
        nomes.sort()
        update.message.reply_text("Nomes organizados em ordem alfabética: ")
        update.message.reply_text("\n".join(nomes))
        
        return ConversationHandler.END
    
    def clearCache():



        return "clearCache"
    
def main():

    bot_token = ""  # Substitua pelo token do seu bot

    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    organizador = Organizador("Minha organização")

    dispatcher.add_handler(CommandHandler("start", organizador.leitorNome, pass_user_data=True))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, organizador.collecting_names, pass_user_data=True))
    dispatcher.add_handler(CommandHandler("nomesorganizados", organizador.nomesOrganizados, pass_user_data=True))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
