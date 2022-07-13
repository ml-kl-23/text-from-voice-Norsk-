# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 10:13:43 2022

!pip3 install SpeechRecognition

@author: manish
"""
import speech_recognition as sr 

r = sr.Recognizer()

    
with sr.Microphone() as source:
    # read the audio data from the default microphone
    print(" PLEASE START TALKIN IN THE MICROPHONE ... ")
    
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    
    # convert speech to text
    #text = r.recognize_google(audio_data)
    
    ## FOR NORWEGIAN 
    
    text = r.recognize_google(audio_data, language="no-NO")
    print(text)
    #return text

