import requests
import streamlit as st

url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    "X-RapidAPI-Key": "2dc054a387msh10f1aa3417dd608p1cf866jsn38be8f35af2d",
    "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
}

num_quotes = 3  # Number of quotes to fetch and display


def fetch_quotes():
    quotes = []
    for _ in range(num_quotes):
        response = requests.get(url, headers=headers)
        data = response.json()
        if "content" in data:
            quote = data["content"]
            quotes.append(quote)
    return quotes


def main():
    st.title("Random Quote Bot")
    st.write("Welcome! I'm a chatbot that can generate random quotes.")

    quotes = fetch_quotes()

    if st.button("Generate Quote"):
        for quote in quotes:
            st.write(quote)


if __name__ == "__main__":
    main()
