import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #gets you the details of the current voice
engine.setProperty('voice', voice[1].id)  # 0-male voice , 1-female voice

def speak(audio):   
    engine.say(audio)    
    engine.runAndWait() #Without this command, speech will not be audible to us.

if __name__=="__main__" :    
    speak('Hello Sir, I am Wally, your Artificial intelligence assistant. Please tell me how may I help you')