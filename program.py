import easyocr
import pyttsx3
import cv2 #allows for showing the image
from matplotlib import pyplot as plt 
import numpy as np

class Bubble:
    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y  
        self.words = []
        self.word_heights = max_y - min_y
        self.size = 1
    #Returns coordinates
    def __repr__(self):
        return ("[" + str(self.min_x) + ", " + str(self.min_y) + ", " + str(self.max_x) + ", " + str(self.max_y) + "]")
    #Returns coordinates
    def show_cords(self):
        return self.min_x, self.min_y, self.max_x, self.max_y
    #Returns min x value
    def getMax_x(self):
        return self.max_x
    #Returns max x value
    def getMin_x(self):
        return self.min_x
    #Sets the bubble's new max x value
    def new_max_x(self, value):
        self.max_x = value
    #Sets the bubble's new max y value
    def new_max_y(self, value):
        self.max_y = value
    #Gets the heights of all phrases
    def combined_height(self, y1, y2):
        word_height = y1 - y2
        self.word_heights += word_height
    #Adds a phrase to the bubble
    def add_phrase(self, y1, y2, word):
        self.words.append(word)
        self.size +=1
        self.combined_height(y1, y2)
    #Returns all text in bubble
    def show_bubble(self):
        holder = ""
        for i in self.words:
            holder += i
        return holder
    #Returns true if y cord is in the speech bubble
    def y_inrange(self, yval):
        if yval <= self.max_y and yval >= self.min_y:
            return True
        return False
    #Returns true if x cord is in the speech bubble
    def x_inrange(self, xval):
        if xval <= self.max_x and xval >= self.min_x:
            return True
        return False
    #Returns true if x cord is inside or reasonably spaced from speech bubble
    def x_spaced(self, xval):
        length = self.word_heights / self.size
        if xval <= length + self.max_x:
            return True
        return False
    #Returns true if y cord is inside or reasonably spaced from speech bubble
    def y_spaced(self, yval):
        length = self.word_heights / self.size
        if yval <= length + self.max_y:
            return True
        return False


#Finds the location of the speech bubble the phrase belongs in. 
#Returns -1 if the phrase isn't in a currently defined speech bubble
# bubbles = [startx, start_y, endx, end_y]: List of all exsiting speech bubbles
# phrase = [startx, start_y, endx, end_y]: Phrase or phrase being checked
def nearest_bubble(bubbles, phrase):
   # print("\nNEW")
    c = 0
    for cords in bubbles:
        if cords.x_spaced(phrase[0]) and cords.y_spaced(phrase[1]):
            return c
        c+=1
    return -1
 

image_path = "percy.jpg"
reader = easyocr.Reader(['en'], gpu = False) #en = english, there's no gpu (i checked :/)
result = reader.readtext(image_path)
       
#([X1,Y1],[xn,y1],[Xn,Yn],[x1,yn], text, confidence)
#print(result) #will print the text with array location and confidence values
#img = cv2.imread(image_path)
speech_bubbles = []
c = 0
for detection in result: #as long as there's something in the result- so there's text that's being read
    #grab x's and y's
    startx = detection[0][0][0]
    start_y = detection[0][0][1]
    endx = detection[0][1][0]
    end_y = detection[0][2][1]    
    phrase = [startx, start_y, endx, end_y]
    w = detection[1]
    #If there's no bubbles, create a new one
    if len(speech_bubbles) < 1:
        speech_bubbles.append(Bubble(startx, start_y, endx, end_y))
    else:
        c = nearest_bubble(speech_bubbles, phrase)
        #If the word isn't in the bubble, create a new bubble
        if c == -1:
            speech_bubbles.append(Bubble(startx, start_y, endx, end_y))
        else:
            #Expand the bubble to include new max values
            if not speech_bubbles[c].y_inrange(end_y):
                speech_bubbles[c].new_max_y(end_y)
            if not speech_bubbles[c].x_inrange(endx):
                speech_bubbles[c].new_max_x(endx)
    #Add the word to whatever speech bubble it's in
    speech_bubbles[c].add_phrase(end_y, start_y, w)

engine = pyttsx3.init()

for i in speech_bubbles:
    engine.say(i.show_bubble())
    print(i.show_bubble())
    engine.runAndWait()
