import pyttsx3
import datetime
import webbrowser
import setuptools
import pyaudio
import wikipedia
import pywhatkit
from PIL import Image,ImageTk,ImageSequence 
import time
import pygame 
from pygame import mixer
mixer.init()

import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import time




root = tk.Tk()
root.geometry("1000x600")

def play_gif():
    root.lift()
    root.attributes('-topmost',True)
    img = Image.open('7kmF.gif')
    lbl = tk.Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load('computer-startup-music-97699.mp3')
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,600))
        img_tk = ImageTk.PhotoImage(img) # Keep a reference to the PhotoImage
        lbl.config(image=img_tk)
        lbl.image = img_tk # Keep a reference to the PhotoImage
        root.update()
        time.sleep(0.04)
    root.destroy()

play_gif()
root.mainloop()

engine = pyttsx3.init('sapi5')

# ask user to change voice or not 

voices_id = int(input('Select 0-1 ') or 0)

# change the voice function

def change_voice():
    if voices_id==1:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[voices_id].id)   
            engine.setProperty('rate',230)
    else:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voices_id].id)
        engine.setProperty('rate',230)
# ask from user 'give me a name'

name = input('Give me a name ')

# define a function for audio

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

#it will take command in text form

def take_command():
    while True:
        command = input('Enter a command: ')
        if command.lower() == 'quit':
            speak('Goodbye!')
            break
        elif command == 'goodbye':
            speak('Enjoy')
            break
        elif command == 'what is your name':
            speak(f'my name is {name or "EVIE"}')
        else:
            if command.lower() == 'quit':
                speak('command not recognized')
                break




# it will greet me from time to time

def GreetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning!')
    elif hour>=12 and hour<=15:
        speak('Good AfterNoon!')
    elif hour>=15 and hour<=19:
        speak('Good Evening!')
    else:
        speak('Good Night!')
    speak(f'This is {name or'EVIE'}. Hey!how may I help you?')

def play_music():
    music_url = "https://www.spotify.com" 
    webbrowser.open(music_url)

def write_email():
    email_url = "https://mail.google.com"  
    webbrowser.open(email_url)

def open_youtube():
    youtube_url = "https://www.youtube.com"
    webbrowser.open(youtube_url)


def save_commands_to_file(command):
    with open('commands.txt', 'a') as file:
        file.write(command + '\n')

def save_commands_to_file(command):
    try:
        with open('commands.txt', 'a') as file:
            file.write(command + '\n')
            file.flush()
            file.close()
    except Exception as e:
        print(f"Error writing to file: {e}")
# this is the main function where all the funtion called 

def main():
    change_voice()
    print()
    GreetMe()
    while True:
        command = input('Enter a command: ')
        if command.lower() == 'quit':
            speak('Goodbye!')
            save_commands_to_file(command)
            break
        elif command == 'goodbye':
            speak('Enjoy')
            save_commands_to_file(command)
            break
        elif command == 'what is your name':
            speak(f'my name is {name or "EVIE"}')
            save_commands_to_file(command)
        elif command == 'play music':
            speak('here you go')
            play_music()
            save_commands_to_file(command)
        elif command == 'write email':
            speak('here you go')
            write_email()
            save_commands_to_file(command)

        elif command == 'open youtube':
            speak('here you go')
            open_youtube()
            save_commands_to_file(command)

        else:
            speak('command not recognized')
            break
            save_commands_to_file(command)

    take_command()
    play_gif()
    print()
    play_music()  
    write_email() 
    open_youtube()

if __name__ == "__main__":
     main()


