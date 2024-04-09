import pyttsx3
import wikipedia
voice = pyttsx3.init()
In = input("Type something: ")
result = wikipedia.summary(In, sentences = 3)
print(result)
voice.say(result)
voice.runAndWait()