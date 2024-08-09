import easyocr
import pyttsx3

print("Start")

engine = pyttsx3.init()



def read(img):
    reader = easyocr.Reader(['en'], gpu = False) 
    results = reader.readtext(img) #creates a list with words, location of word, and confidence values
    for detection in results: #as long as there's something in the results list- so there's text that's being read
        text = detection[1] #grabbing text
        print(text)
        #engine.say(text)
        engine.runAndWait()

read("percy.jpg")
