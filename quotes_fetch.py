import streamlit as st
import requests

# Replace 'YOUR_BOT_TOKEN' with your Telegram bot token
bot_token = '6010408512:AAHpLwF_PlsmHfoTAJkCIuKunopcVCB4yXw'
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

num_quotes = 3  # Number of quotes to fetch and display


def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        st.error(f"Failed to send message: {response.text}")


def quote():
    for _ in range(num_quotes):
        response = requests.get("https://quotes15.p.rapidapi.com/quotes/random/",
                                headers={"X-RapidAPI-Key": "2dc054a387msh10f1aa3417dd608p1cf866jsn38be8f35af2d",
                                         "X-RapidAPI-Host": "quotes15.p.rapidapi.com"})
        data = response.json()

        if "content" in data:
            quote_text = data["content"]
            send_message(chat_id="5809290032", text=quote_text)


def main():
if __name__ == "__main__":
    main()
