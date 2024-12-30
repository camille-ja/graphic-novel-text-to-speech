import PIL.Image
import easyocr
import pyttsx3
import random
import math
import os


import cv2
import PIL
from PIL import Image
from PIL import ImageDraw
import json
with open('words_dictionary.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def get_min_y(self):
        return self.y1
    def get_max_y(self):
        return self.y2
    def set_max_x(self, x):
        self.x2 = x
    def set_min_y(self, y):
        self.y1 = y
    def set_max_y(self, y):
        self.y2 = y
    def get_min_x(self):
        return self.x1
    def get_min_y(self):
        return self.y1
    def get_max_x(self):
        return self.x2
    def get_max_y(self):
        return self.y2
    def getLine(self):
        return (str(self.x1) + ", " + str(self.y1) + ", " + str(self.x2) + ", " + str(self.y2))

#inside the bubble there's a phrase that hold's it's x and y coord
#maybe make a phrase strip class? but it'd have to be unattached from the bubble
#kinda like the bubble: you have individual strips
#if y cords a similar x cords reasonably line up (maybe they have to be in the same bubble?)
# yeah like every bubble is broken up into phrases
#so every bubble contains a strip- put the code in the bubble class
class Phrase:
    def __init__(self, text, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.text = text
    def get_y_cords(self):
        return ": miny" +  str(self.y1) + ", maxy:" +  str(self.y2) + ": "
    def get_min_y(self):
        return math.floor(self.y1)
    def get_max_y(self):
        return math.floor(self.y2)
    def get_min_x(self):
        return self.x1
    def get_max_x(self):
        return self.x2
    def get_phrase(self):
        return self.text

class Bubble:
    def __init__(self, min_x, min_y, max_x, max_y):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y  
        self.words = []
        self.bubble_heights = max_y - min_y
        self.word_height = max_y - min_y
        self.size = 1
        self.line = []
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
    #Returns min y value
    def getMin_y(self):
        return self.min_y
    #Returns max y value
    def getMax_y(self):
        return self.max_y
    #Sets the bubble's new x values
    def new_x_val(self, x1, x2):
        if(self.max_x < x2):
            self.max_x = x2
        if(self.min_x > x1):
            self.min_x = x1
    #Sets the bubble's new max y value
    def new_max_y(self, value):
        self.max_y = value
   #finds the coordinates for/adds words to the line 
    def build_line(self, phrase, min_x):
        #each strip should have the same (or rlly close) min and max y values
        #line[minx, miny, maxx, maxy] (y's shouldn't change)
        #if line is empty, add strip to line
        if(len(self.line) == 0):
            self.line.append(Line(phrase.get_min_x(),phrase.get_min_y(),phrase.get_max_x(),phrase.get_max_y()))
            #print(phrase.get_phrase())
        else: 
            expandedLine = False
            for i in self.line:
            #can edit for room for error- maybe a difference depending on size of the words? 2 is arbitrary for now
                #if the phrase fits on the line, expand the length of the line
                if(phrase.get_min_y() >= (i.get_min_y() - 2) and phrase.get_min_y() <= (i.get_min_y() + 2)
                and phrase.get_max_y() >= (i.get_max_y() - 2) and phrase.get_max_y() <= (i.get_max_y() + 2)):
                    i.set_max_x(phrase.get_max_x())
                    expandedLine = True
            if(not expandedLine):      #else create a new line
                self.line.append(Line(min_x,phrase.get_min_y(),phrase.get_max_x(),phrase.get_max_y()))
    #prints the line and cords 
    def get_line(self):
        forShow = ""
        for i in self.line:
            forShow += i.getLine()
            forShow += "<- STRIP "
        return forShow
    #returns the y value of each phrase in the bubble
    def phrase_cords(self):
        holder = ""
        for i in self.words:
            holder += i.get_phrase() +  " " + i.get_y_cords()
        return holder
    #Returns all text in bubble
    def show_bubble(self):
        holder = ""
        for i in self.words:
            holder += i.get_phrase()
        return holder
    #Returns true if y cord is in the speech bubble
    def y_inrange(self, yval):
        if yval <= self.max_y and yval >= self.min_y:
            return True
        return False
    #Returns true if x cord is in the speech bubble
    def x_inrange(self, x1, x2): #starx,endx
        if x2 <= self.max_x and x1 >= self.min_x:
            return True
        return False
    #the size of the bubble is increased by the height of the newest phrase
    def combined_height(self, y1, y2):
        word_height = y2 - y1
        self.bubble_heights += word_height #bubble is increase by the height of the phrase that's been added
    #Adds a phrase to the bubble
    def add_phrase(self, x1,y1, x2, y2, word, min):
        w = Phrase(word, x1,y1, x2, y2)
        self.words.append(w)
        self.size +=1
        self.combined_height(y1, y2)
        self.build_line(w, min)
    #Returns true if x cord is inside or reasonably spaced from speech bubble
    def x_spaced(self, xval, min_y, max_y):
        smaller_height = max_y - min_y
        if self.word_height < smaller_height: #this is to account for big text in a bubble followed by small text or vis versa
            smaller_height = self.word_height
        if xval <= smaller_height + self.max_x: #if min x of checked value is less than max x of bubble + length of a word, it's in bubble
            return True
        return False
    #Returns true if y cord is inside or reasonably spaced from speech bubble
    def y_spaced(self, yval):
        length = self.bubble_heights / self.size
        if yval <= self.word_height + self.max_y: #if the word starts before the max y of the bubble (plus room for an additional word, it's resonably spaced)
            return True
        return False

#Finds the location of the speech bubble the phrase belongs in. 
#Returns -1 if the phrase isn't in a currently defined speech bubble
# bubbles = [startx, start_y, endx, end_y]: List of all exsiting speech bubbles
# phrase = [startx, start_y, endx, end_y]: Phrase or phrase being checked
def nearest_bubble(bubbles, phrase, w):
    c = 0
    for cords in bubbles:
        if cords.x_spaced(phrase[0], phrase[1], phrase[2]) and cords.y_spaced(phrase[1]):
            return c
        c+=1
    return -1

 
#im = screenreader.get_image()
class Reading():
    def read(run):
        reader = easyocr.Reader(['en'], gpu = False) #en = english, there's no gpu (i checked :/)
        print("read")
        to_read = []

        #editing image
        #img = cv2.imread("temp.jpg",0)
        folder_path = 'C:/Users/cjam2/graphic novel text to speech/panels/panels'
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)
            im = PIL.Image.open(image_path)
            result = reader.readtext(im) #no changes
            #print(result)
            speech_bubbles = []
            c = 0
            prev_x = 0
            prev_y = 0
            for detection in result: #as long as there's something in the result- so there's text that's being read
                #grab x's and y's
                #startx/y = x1, endx/y = x2 (l-r, top-bottom)
                start_x = detection[0][0][0]
                start_y = detection[0][0][1]
                end_x = detection[0][1][0]
                end_y = detection[0][2][1]    
                phrase = [start_x, start_y, end_x, end_y]
                #w = word/phrase
                w = detection[1]
                if start_x >= prev_x or start_y >= prev_y: #if the phrase is to the right or under the prev phrase, add it
                    #If there's no bubbles, create a new one
                    if len(speech_bubbles) < 1:
                        speech_bubbles.append(Bubble(start_x, start_y, end_x, end_y))
                    else:    
                        c = nearest_bubble(speech_bubbles, phrase, w)
                        #If the word isn't in the bubble, create a new bubble
                        if c == -1:
                            speech_bubbles.append(Bubble(start_x, start_y, end_x, end_y))
                        else:
                            #Expand the bubble to include new max values
                            if not speech_bubbles[c].y_inrange(end_y):
                                speech_bubbles[c].new_max_y(end_y)
                            if not speech_bubbles[c].x_inrange(start_x, end_x):
                                speech_bubbles[c].new_x_val(start_x, end_x)
                        #Add the word to whatever speech bubble it's in
                    prev_x = start_x
                    prev_y = start_y
                    speech_bubbles[c].add_phrase(start_x, start_y, end_x, end_y, w, speech_bubbles[c].getMin_x())                    
            print("done read, edit time!")
            to_read.append(Editing.edit(speech_bubbles, reader, im, True))
            to_read.append(" ")
        for s in to_read:
            print(s)
            
        

class LetterPoints():
    def __init__(self, char, points):
        self.char = []
        self.char.append(char)
        self.points = []
        self.points.append(points)
    def add_point(self, index):
        self.points[index] +=1
    def get_points(self):
        return self.points
    def get_word(self):
        return self.char
    #adds new word and gives it a point
    def add_word(self, char):
        self.points.append(1)
        self.char.append(char)
    #returns the letter w the most points corrosponding to it
    def best_word(self):
        return self.char[self.points.index(max(self.points))]

#adds a word to phrase
#words is the array that holds all the words scanned so far
#temp_string is the word we're adding with a space at the end
#y is the specific index (so the specific word) we're looking at
def add_to_phrase(words, temp_string, y, delete):
    if words[y] == "XX": #if a real word hasn't been added to words[], add it here
        words[y] = LetterPoints(temp_string,1)
    elif temp_string in words[y].get_word(): #if the word is already found at the index, add a point to the word
        words[y].add_point(words[y].get_word().index(temp_string)) #add a point to the index that corosponds to the word
    else: #if temp_string is a new word at the index, add temp_string and give the word 1 point (im like so sure this isn't nesicary)
        #print(words[y].get_word())
        words[y].add_word(temp_string)
        '''print("ADDING",temp_string)
        print(y, delete) #delete is min words
        u = 0
        while u < len(words):
            if words[u] == "XX":
                print("XX")
            else:
                print(words[u].get_word())
            u+=1'''
        
def word_correction(words, junk_words, temp_string, separated_char, y, max_word_index):
    print("f")


class Editing():
    def edit(speech_bubbles, reader, im, run):
        vals = [ [0,0], [0.0, 0.1],[0.4, 0.1],[0.8, 0.1],
                  [0.0, 0.5],[0.4, 0.5],[0.8, 0.5],
                  [0.0, 1],[0.4, 1],[0.8, 1],

                  [0.0, 0.1],[0.4, 0.1],[0.8, 0.1],
                  [0.0, 0.5],[0.4, 0.5],[0.8, 0.5],
                  [0.0, 1],[0.4, 1],[0.8, 1],
                  
                  [0.0, 0.1],[0.4, 0.1],[0.8, 0.1],
                  [0.0, 0.5],[0.4, 0.5],[0.8, 0.5],
                  [0.0, 1],[0.4, 1],[0.8, 1],
                  
                  [0.0, 0.1],[0.4, 0.1],[0.8, 0.1],
                  [0.0, 0.5],[0.4, 0.5],[0.8, 0.5],
                  [0.0, 1],[0.4, 1],[0.8, 1]] #[contrast threshold, margin]
        holder = ""
        for i in speech_bubbles: #goes bubble by bubble (so through entire page)
            '''print(i.show_bubble())
            print("BUBBLE")
            print("NUM LINES: ",len(i.line))'''

            for j in i.line: #goes line by line
                
                
                #This is all cropping the bubble line by line
                #-----------------------------------------------#
                im1 = im.crop((j.get_min_x() - 5, j.get_min_y() - 2, j.get_max_x() + 5, j.get_max_y() + 2))
                im1 = im1.save("cropped.jpg")                 
                im1 = PIL.Image.open("cropped.jpg") #temp bc im trying to draw the boudning box 
                im1.thumbnail((300,300))
                im1.save("cropped.jpg")
                #--------------------------------------------#
                
                #This is adjusting variables per bubble
                phrases = [] #holds alll of the phrases w versions of adjustments (this is for one line)

                for p in vals: #for each adjustement
                    result = reader.readtext("cropped.jpg", contrast_ths=p[0], adjust_contrast=.9, width_ths= 1.5, add_margin= p[1], decoder= 'beamsearch') #conttrast thereshold sets minum contrast and adjusts it, adding margins increase bound box in all directions,                # width: if something outside a box is close to something within one it'll merge the two
                    if len(result) != 0:
                        phrases.append(result[0][1]) #adding adjustment to the word
                words = [] #will hold the letters, points, and indexs for all chars in phrase
                first_time = True
                temp = [] #will hold chars to one word 
                junk_words = [] #same length as words[]- indexs with YY have valid words
                max_word_index = -1
                single_lets = ['a', 'i'] #letters that can reasonbly be by themselves
                for z in phrases:
                    print(z)
                #what if none of the words are there?
                #what if [/other common errors?

                for i in phrases: #per line, goes through every possible variation one at a time
                    x = 0 #the index of i
                    y = 0 #the index of words[] and junk_words[]
                    #print("NEW:", i)
                    #print("----------NEW LOOP-------------")
                    i += " " #so the last word gets picked up
                    while x < len(i): #this will go through each char of one variation
                        if i[x].isalnum(): #if the char is a letter or number, add it to the list
                            temp.append(i[x]) 
                        #    print(i[x])
                        else: #a space was found, so check if the word exists
                            #print(temp)
                            if not not temp: #if the prev to x wasn't a space 
                                if (len(temp) > 1 or temp[0] in single_lets):# and x + 1 < len(i) -1: #if there's just a single character at the end that isn't i, or a it's probably a mistake
                                    temp_string = "".join(temp)
                                    temp_string = temp_string.lower()
                                    t = "," + temp_string + "," #to make things match the json file
                                    #print(t, x < len(i))
                                    temp_string += " " #adding a space to separate the words
                                    #-------deciding what to do with the scanned word----------------------#      
                                    if t in data: #if the word is in the list of words
                                        if first_time or y > max_word_index: #if we're adding a word at an index not prev accessed
                                            words.append(LetterPoints(temp_string, 1))
                                            junk_words.append("YY")
                                            max_word_index+=1
                                            #print(first_time)
                                        else: #word is in list and is being added to an index that's filled with words or XX
                                            #print("Y ",y,"words: ",len(words), max_word_index)
                                            
                                            add_to_phrase(words, temp_string, y, max_word_index)
                                    else: #did not scan a word
                                        if first_time: #word isn't in list but it's the first time we're adding to the list
                                            words.append("XX") #filler bc there's no word 
                                            junk_words.append("YY")
                                            max_word_index+=1
                                        else: 
                                            if y > max_word_index:
                                                words.append("XX")
                                                junk_words.append("YY")
                                                max_word_index+=1
                                            else: #word isn't in list and this isn't the first time we're adding to list (so something should be in words[y])- we're adding what's scanned to junk
                                                #print(max_word_index, y, temp_string)
                                                #for w in words:
                                                #    if w == "XX":
                                                #        print(w)
                                                #    else:
                                                        #print(w.get_word())
                                                if junk_words[y] == "YY":
                                                    junk_words[y] = (LetterPoints(temp_string,1)) #replacing the filler with the scanned word (not in list)
                                                if temp_string in junk_words[y].get_word(): #if the word is alr in junk string, give it a point
                                                    junk_words[y].add_point(junk_words[y].get_word().index(temp_string)) 
                                                else: #there's already a junk word, but it doesn't match anything in junk_words
                                                    junk_words[y].add_word(temp_string)
                                    y+=1
                                    temp = [] #will hold chars to one word 
                            #else:
                                #print("END MISTAKE", len(temp), x, len(i), )
                                #for w in temp:
                                #    print(w)
                        #print(y, ":", i, ":" ,i[x], x, len(i))
                        x+=1
                    first_time = False
                    temp = []



                c = 0
                while c < len(words):
                    if words[c] == "XX": #there's a junk word that should be used instead
                        w = junk_words[c].best_word()
                        if w != "YY":
                            #print(junk_words[c].best_word())
                            holder+= junk_words[c].best_word()
                    else:
                        holder += words[c].best_word()
                    c+=1
                print(holder)  
                holder += " "
                    

    
        
        print("done")
        return holder
            
       

Reading.read(True)