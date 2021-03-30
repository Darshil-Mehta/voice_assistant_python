import speech_recognition as sr
import webbrowser
from datetime import datetime
import yfinance as yf
r = sr.Recognizer()


def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source, phrase_time_limit=4)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('I did not get that')
        except sr.RequestError:
            print('Sorry, the service is down')
        return voice_data.lower()


def response(user_command):
    if 'how are you' in user_command:
        print('I am fine, thanks for asking!')
    elif 'what is your name' in user_command:
        print("Hello I am Alpha")
    elif 'search google' in user_command:
        search_google = record_audio("What do you want to search for on google?")
        url = 'https://google.com/search?q=' + search_google
        webbrowser.get().open(url)
        print("Here is what i found for " + search_google)
    elif 'search youtube' in user_command:
        search_youtube = record_audio("What do you want to search for on youtube?")
        url = 'https://www.youtube.com/results?search_query=' + search_youtube
        webbrowser.get().open(url)
        print("Here is what i found for " + search_youtube)
    elif 'open mail' in user_command:
        url = 'https://mail.google.com/mail/u/0/#inbox'
        webbrowser.get().open(url)
    elif 'find location' in user_command:
        location = record_audio("What location do you want to find on maps?")
        url = 'https://www.google.co.in/maps/place/' + location
        webbrowser.get().open(url)
        print("Here is your required location " + location)
    elif 'find direction' in user_command:
        current_location = record_audio("Where are you currently?")
        final_destination = record_audio("Where do you want to go?")
        url = 'https://www.google.co.in/maps/dir/' + current_location + '/' + final_destination
        webbrowser.get().open(url)
        print("Here is how you can reach " + final_destination + " from " + current_location)
    elif 'what is the time' in user_command:
        current_time = datetime.now().time()
        print("Currently the time is " + str(current_time))
    elif 'what is the date' in user_command:
        current_date = datetime.now().date()
        print("Today is " + str(current_date))
    elif 'get stock details' in user_command:
        search_term = record_audio("Which stock do u want to search for?")
        stocks = {
            "apple": "AAPL",
            "microsoft": "MSFT",
            "facebook": "FB",
            "tesla": "TSLA",
            "amazon": "AMZN",
            "zoom video communications": "ZM",
            "netflix": "NFLX",
            "bitcoin": "BTC-USD",
            "ethereum": "ETH-USD",
            "nifty fifty": "^NSEI",
            "tata motors": "TATAMOTORS.NS",
            "tata power": "TATAPOWER.NS",
            "tata steel": "TATASTEEL.NS",
            "reliance": "RELIANCE.NS",
            "tata consultancy service": "TCS.NS",
            "icici bank": "ICICIBANK.NS",
            "hdfc bank": "HDFCBANK.NS",
            "hdfc": "HDFC.NS",
            "state bank of india": "SBIN.NS",
            "hcl technologies": "HCLTECH.NS",
            "infosys": "INFY.NS",
            "hindustani unilever": "HINDUNILVR.NS",
            "l and t": "LT.NS"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]
            currency = stock.info["currency"]
            print("Market Price of " + search_term + " is " + str(price) + " " + currency)
        except:
            print("No data available for the stock you are searching for!")
    elif 'convert currency' in user_command:
        currency_type = ['indian rupee', 'japanese yen', 'us dollar', 'euros', 'canadian dollar', 'australian dollar', 'pakistani rupee']
        currency_one = record_audio("Say currency type which you have")
        currency_one_value = float(record_audio("How much amount of " + currency_one + " do you have?"))
        currency_two = record_audio("Say currency type which you want to convert to")
        if (currency_one != currency_two) and (currency_one and currency_two in currency_type):
            value = None
            currency_two_value = None
            if currency_one == "indian rupee":
                value = currency_one_value
            if currency_one == "japanese yen":
                value = currency_one_value * 0.66
            if currency_one == 'us dollar':
                value = currency_one_value * 72.45
            if currency_one == 'euros':
                value = currency_one_value * 85.44
            if currency_one == 'canadian dollar':
                value = currency_one_value * 57.48
            if currency_one == 'australian dollar':
                value = currency_one_value * 55.32
            if currency_one == 'pakistani rupee':
                value = currency_one_value * 0.47
            if currency_two == "indian rupee":
                currency_two_value = value
            if currency_two == "japanese yen":
                currency_two_value = value * 1.51
            if currency_two == "us dollar":
                currency_two_value = value * 0.0138026
            if currency_two == "euros":
                currency_two_value = value * 0.0117041
            if currency_two == "canadian dollar":
                currency_two_value = value * 0.0173974
            if currency_two == "australian dollar":
                currency_two_value = value * 0.0180766
            if currency_two == "pakistani rupee":
                currency_two_value = value * 2.1276595
        else:
            print("No data found for the mentioned currencies")
        currency_two_values = "{:.2f}".format(currency_two_value)
        print(str(currency_one_value) + " " + currency_one + " is equal to " + str(currency_two_values) + " " + currency_two)
    elif 'find word meaning' in user_command:
        word = record_audio("Which word meaning do you want?")
        url = "https://www.dictionary.com/browse/" + word
        webbrowser.get().open(url)
        print("Here is what " + word + " means!")
    elif 'exit' in user_command:
        print('going offline')
        exit()
    else:
        print("I did not get what you want me to do. Please repeat again!")


while(True):
    print("How can i help you?")
    user_command = record_audio()
    print(user_command)
    response(user_command)