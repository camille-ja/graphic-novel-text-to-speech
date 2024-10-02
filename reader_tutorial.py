import easyocr
import pyttsx3

def read(img):
    reader = easyocr.Reader(['en'], gpu = False) 
    results = reader.readtext(img) #creates a list with words, location of word, and confidence values
    for detection in results: #as long as there's something in the results list- so there's text that's being read
        text = detection[1] #grabbing text
        print(text)
        #engine.say(text)
        engine.runAndWait()

print("Start")
engine = pyttsx3.init()


#model finds order of text blocks
num_blocks = 1
#splits image by text? so loop 
while num_blocks > 0:
    #split/focus on one part of image
    img = "percy.jpg"
    read(img)
    num_blocks -=1