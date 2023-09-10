import requests
import telebot
import streamlit as st

url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    "X-RapidAPI-Key": "2dc054a387msh10f1aa3417dd608p1cf866jsn38be8f35af2d",
    "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
}

num_quotes = 3  # Number of quotes to fetch and display

# Replace 'YOUR_BOT_TOKEN' with your Telegram bot token
bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_message = "Welcome! I'm a chatbot that can generate random quotes.\n\nSend /quote to get a quote."
    bot.send_message(chat_id=message.chat.id, text=welcome_message)

@bot.message_handler(commands=['quote'])
def quote(message):
    for _ in range(num_quotes):
        response = requests.get(url, headers=headers)
        data = response.json()

        if "content" in data:
            quote = data["content"]
            bot.send_message(chat_id=message.chat.id, text=quote)

if __name__ == "__main__":
    st.write("The bot is running.")  # Added message to indicate the bot is running
    bot.polling()
