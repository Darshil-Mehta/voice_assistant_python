import speech_recognition as sr # voice command -> text
import webbrowser
from datetime import datetime
import yfinance as yf
import playsound
import os
import random
from gtts import gTTS # google text to speech
import time
r = sr.Recognizer()


def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
            print("response = " + ask)
        audio = r.listen(source, phrase_time_limit=4)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down')
        return voice_data.lower()


def speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    randomNum = random.randint(1, 10000000)
    audio_file = 'audio-' + str(randomNum) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print("response = " + audio_string)
    os.remove(audio_file)


def response(user_command):
    if 'how are you' in user_command:
        speak('I am fine, thanks for asking!')
    elif 'what is your name' in user_command:
        speak("Hello I am Alpha")
    elif 'search google' in user_command:
        search_google = record_audio("What do you want to search for on google?")
        url = 'https://google.com/search?q=' + search_google
        webbrowser.get().open(url)
        speak("Here is what i found for " + search_google)
    elif 'search youtube' in user_command:
        search_youtube = record_audio("What do you want to search for on youtube?")
        url = 'https://www.youtube.com/results?search_query=' + search_youtube
        webbrowser.get().open(url)
        speak("Here is what i found for " + search_youtube)
    elif 'open mail' in user_command:
        url = 'https://mail.google.com/mail/u/0/#inbox'
        webbrowser.get().open(url)
        speak("Your inbox is now opened")
    elif 'find location' in user_command:
        location = record_audio("What location do you want to find on maps?")
        url = 'https://www.google.co.in/maps/place/' + location
        webbrowser.get().open(url)
        speak("Here is your required location " + location)
    elif 'find direction' in user_command:
        current_location = record_audio("Where are you currently?")
        final_destination = record_audio("Where do you want to go?")
        url = 'https://www.google.co.in/maps/dir/' + current_location + '/' + final_destination
        webbrowser.get().open(url)
        speak("Here is how you can reach " + final_destination + " from " + current_location)
    elif 'what is the time right now' in user_command:
        current_time_h = datetime.now().time().hour
        current_time_m = datetime.now().time().minute
        current_time = str(current_time_h) + " hours and " + str(current_time_m) + " minutes"
        speak("Currently the time is " + current_time)
    elif 'what is the date today' in user_command:
        current_date = datetime.now().date()
        speak("Today is " + str(current_date))
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
            speak("Market Price of " + search_term + " is " + str(price) + " " + currency)
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
            speak("No data found for the mentioned currencies")
        currency_two_values = "{:.2f}".format(currency_two_value)
        speak(str(currency_one_value) + " " + currency_one + " is equal to " + str(currency_two_values) + " " + currency_two)
    elif 'dictionary' in user_command:
        word = record_audio("Which word meaning do you want?")
        url = "https://www.dictionary.com/browse/" + word
        webbrowser.get().open(url)
        speak("Here is what " + word + " means!")
    elif 'wait alpha' in user_command:
        speak("Going offline for 5 minutes!")
        time.sleep(300)
    elif 'exit alpha' in user_command:
        speak('going offline')
        exit()
    else:
        speak("I did not get what you want me to do. Please repeat again!")