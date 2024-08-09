import easyocr
import pyttsx3

print("Start")

image_path = "percy.jpg"
engine = pyttsx3.init()
reader = easyocr.Reader(['en'], gpu = False) #en = english, there's no gpu (i checked :/)
results = reader.readtext(image_path) #creates a list with words, location of word, and confidence values

for detection in results: #as long as there's something in the results list- so there's text that's being read
    text = detection[1] #grabbing text
    print(text)
    engine.say(text)
    engine.runAndWait()