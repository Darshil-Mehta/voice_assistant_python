from tkinter import *
from main import *

root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.geometry("540x330")

header_font = ("Castellar", 15, "bold italic")
body_font = ("Castellar", 12)
feature_font = ("Castellar", 11)


def show_frame(frame):
    frame.tkraise()


def start_alpha():
    while True:
        time.sleep(1)
        speak("How can i help you?")
        user_command = record_audio()
        response(user_command)


frame_mainPage = Frame(root, bg="#2E81F4")
frame_aboutPage = Frame(root, bg="#B4EDD2")
frame_startPage = Frame(root, bg="#89023E")

for frame in (frame_startPage, frame_aboutPage, frame_mainPage):
    frame.grid(row=0, column=0, sticky="nsew")
show_frame(frame_startPage)

""" start page """
start_header_one = Label(frame_startPage,
                         text="Welcome!!!",
                         font=header_font,
                         pady=10,
                         bg="#89023E",
                         fg="white").grid(row=0, column=0, columnspan=5)
start_header_two = Label(frame_startPage,
                         text="This is your personal voice assistant!",
                         font=body_font,
                         pady=10,
                         bg="#89023E",
                         fg="white").grid(row=1, column=0, columnspan=5)
start_header_three = Label(frame_startPage,
                           text="Click on 'Use me' to get information regarding anything using voice command",
                           font=body_font,
                           pady=10,
                           bg="#89023E",
                           fg="white").grid(row=2, column=0, columnspan=5)
btn_mainPage = Button(frame_startPage,
                      text="Use me!",
                      bg="#EA638C",
                      fg="white",
                      pady=8,
                      command=lambda: show_frame(frame_mainPage)).grid(row=3, column=1, sticky="nsew")
btn_aboutPage = Button(frame_startPage,
                       text="About me!",
                       bg="#EA638C",
                       fg="white",
                       pady=8,
                       command=lambda: show_frame(frame_aboutPage)).grid(row=3, column=3, sticky="nsew")

""" about page """
start_header = Label(frame_aboutPage,
                     text="What things can i do for you?",
                     font=header_font,
                     pady=5,
                     bg="#B4EDD2").pack()
my_features = Label(frame_aboutPage,
                    text="Search anything on google",
                    font=feature_font,
                    bg="#B4EDD2",
                    pady=3).pack()
my_features = Label(frame_aboutPage,
                    text="Search anything on youtube",
                    font=feature_font,
                    bg="#B4EDD2",
                    pady=3).pack()
my_features = Label(frame_aboutPage,
                    text="Find location",
                    font=feature_font,
                    bg="#B4EDD2",
                    pady=3).pack()
my_features = Label(frame_aboutPage,
                    text="Find a route from a place to another (Google Maps)",
                    font=feature_font,
                    bg="#B4EDD2",
                    pady=3).pack()
my_features = Label(frame_aboutPage,
                    text="Get stock prices of some trending stocks",
                    font=feature_font,
                    bg="#B4EDD2",
                    pady=3).pack()
my_features = Label(frame_aboutPage,
                    text="Convert currency",
                    font=feature_font,
                    bg="#B4EDD2",
                    pady=3).pack()
my_features = Label(frame_aboutPage,
                    text="Get current time and date",
                    font=feature_font,
                    bg="#B4EDD2",
                    pady=3).pack()
my_features = Label(frame_aboutPage,
                    text="Find meaning of any word from dictionary",
                    font=feature_font,
                    bg="#B4EDD2",
                    pady=3).pack()
my_features = Label(frame_aboutPage,
                    text="Access your emails",
                    font=feature_font,
                    bg="#B4EDD2",
                    pady=3).pack()
btn_homePage = Button(frame_aboutPage,
                      text="<< Back",
                      bg="#87677B",
                      fg="white",
                      command=lambda: show_frame(frame_startPage)).pack()

""" main page """
start_header = Label(frame_mainPage,
                     font=header_font,
                     bg="#2E81F4",
                     fg="white",
                     pady=10,
                     text="Click below on start button to use me!").grid(row=0, column=0, columnspan=5, sticky="e")
btn_homePage = Button(frame_mainPage,
                      text="<< Back",
                      bg="#87677B",
                      fg="white",
                      command=lambda: show_frame(frame_startPage)).grid(row=1, column=1, sticky="nsew")
btn_start_voice = Button(frame_mainPage,
                         bg="#2376BA",
                         fg="white",
                         command=start_alpha,
                         text="START").grid(row=1, column=3, sticky="nsew")

root.mainloop()