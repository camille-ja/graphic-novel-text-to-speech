import PIL.Image
import easyocr
import pyttsx3
import random

import cv2
import PIL
from PIL import Image
from PIL import ImageDraw


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
        return self.y1
    def get_max_y(self):
        return self.y2
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
        self.word_heights = max_y - min_y
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
    #Gets the heights of all phrases
    def combined_height(self, y1, y2):
        word_height = y2 - y1
        self.word_heights += word_height
   #finds the coordinates for/adds words to the line
    def build_line(self, phrase):
        #each strip should have the same (or rlly close) min and max y values
        #line[minx, miny, maxx, maxy] (y's shouldn't change)
        #if line is empty, add strip to line an
        if(len(self.line) == 0):
            self.line.append(Line(phrase.get_min_x(),phrase.get_min_y(),phrase.get_max_x(),phrase.get_max_y()))
        else: 
            expandedLine = False
            for i in self.line:
            #can edit for room for error- maybe a difference depending on size of the words? 2 is arbitrary for now
                #if the phrase fits on the line, expand the lenght of the line
                if(phrase.get_min_y() >= (i.get_min_y() - 2) and phrase.get_min_y() <= (i.get_min_y() + 2)
                and phrase.get_max_y() >= (i.get_max_y() - 2) and phrase.get_max_y() <= (i.get_max_y() + 2)):
                    i.set_max_x(phrase.get_max_x())
                    expandedLine = True
            if(not expandedLine):
                self.line.append(Line(phrase.get_min_x(),phrase.get_min_y(),phrase.get_max_x(),phrase.get_max_y()))
            #if the min and max y could fit in the line, change the max x of the line
            #else create a new line
    #prints the line and cords 
    def get_line(self):
        forShow = ""
        for i in self.line:
            forShow += i.getLine()
            forShow += " STRIP "
        return forShow
    #Adds a phrase to the bubble
    def add_phrase(self, x1,y1, x2, y2, word):
        w = Phrase(word, x1,y1, x2, y2)
        self.words.append(w)
        self.size +=1
        self.combined_height(y1, y2)
        self.build_line(w)
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
    def x_inrange(self, x1, x2):
        #print(str(self.max_x) + ", " + str(self.min_x) + ", " + str(x1) + ", " + str(x2))
        if x2 <= self.max_x and x1 >= self.min_x:
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
    c = 0
    for cords in bubbles:
        if cords.x_spaced(phrase[0]) and cords.y_spaced(phrase[1]):
            return c
        c+=1
    return -1



 
#im = screenreader.get_image()
class Reading():
    def read(run):
        print("read")
        
        #editing image
        img = cv2.imread("temp.jpg",0)
        blur = cv2.GaussianBlur(img,(5,5),0)
        pil = Image.fromarray(blur)
        pil.save("look.jpg")
        
        image_path = "temp.jpg"
        im = PIL.Image.open("temp.jpg") #temp bc im trying to draw the boudning box 
        im
        reader = easyocr.Reader(['en'], gpu = False) #en = english, there's no gpu (i checked :/)
        result = reader.readtext(im) #no changes
        #conttrast thereshold sets minum contrast and adjusts it, adding margins increase bound box in all directions, width: if something outside a box is close to something within one it'll merge the two
        #result = reader.readtext(im, contrast_ths=0.05, adjust_contrast=0.9, width_ths= 1.5, add_margin=.25, decoder= 'beamsearch')
        #doing a ycenter_ths of like 5 will give the indivudal speech bubbles
        result
        ''' draw = ImageDraw.Draw(im)
        for results in result:
            p0, p1, p2, p3 = results[0]
            draw.line([*p0,*p1,*p2,*p3,*p0], fill = 'yellow', width = 2)
        im.show()'''
        
       # print(result)
            
        #([X1,Y1],[xn,y1],[Xn,Yn],[x1,yn], text, confidence)
        #print(result) #will print the text with array location and confidence values
        speech_bubbles = []
        c = 0
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
            #If there's no bubbles, create a new one
            if len(speech_bubbles) < 1:
                speech_bubbles.append(Bubble(start_x, start_y, end_x, end_y))
            else:
                c = nearest_bubble(speech_bubbles, phrase)
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
            speech_bubbles[c].add_phrase(start_x, start_y, end_x, end_y, w)
        Editing.edit(speech_bubbles, reader, im, True)

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
    def get_let(self):
        return self.char
    #adds new char and gives it a point
    def add_char(self, char):
        self.points.append(1)
        self.char.append(char)
    #returns the letter w the most points corrosponding to it
    def best_let(self):
        return self.char[self.points.index(max(self.points))]



class Editing():

    def edit(speech_bubbles, reader, im, run):
        vals = [[0.0, 0.1],[0.4, 0.1],[0.8, 0.1],
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
                  [0.0, 1],[0.4, 1],[0.8, 1]] #[contrast threshold, inc/dec, margin,inc/dec,con]
        for i in speech_bubbles: #goes bubble by bubble (so through entire page)
            print("BUBBLE")
            for j in i.line: #goes line by line
                
                
                #This is all cropping the bubble line by line
                #-----------------------------------------------#
                im1 = im.crop((j.get_min_x() - 5, j.get_min_y() - 2, j.get_max_x() + 5, j.get_max_y() + 2))
                im1 = im1.save("cropped.jpg")                 
                #im2 = PIL.Image.open(im1)
                #im1.show()
                im1 = PIL.Image.open("cropped.jpg") #temp bc im trying to draw the boudning box 
                im1.thumbnail((300,300))
                im1.save("cropped.jpg")
                '''im1 = im1.point( lambda p: 255 if p > 125 else 0 )
                im1 = im1.convert('1')
                im1.save("cropped1.jpg")'''
                
                #--------------------------------------------#
                
                #This is adjusting variables per bubble
                words = [] #holds alll of the phrases w versions of adjustments (this is for one line)

                for p in vals: #for each adjustement
                    result = reader.readtext("cropped.jpg", contrast_ths=p[0], adjust_contrast=.9, width_ths= 1.5, add_margin= p[1], decoder= 'beamsearch') #conttrast thereshold sets minum contrast and adjusts it, adding margins increase bound box in all directions,                # width: if something outside a box is close to something within one it'll merge the two
                    words.append(result[0][1]) #adding adjustment to the word
                letters = [] #will hold the letters, points, and indexs for all chars in phrase
                first_time = True

                for i in words: #per line, goes through every possible variation one at a time
                    x = 0
                    while x < len(i): #this will go through each char of one variation
                        if first_time or len(letters) <= x: #add all chars to the phrase the first time around 
                            letters.append(LetterPoints(i[x], 1))
                        else:
                            if i[x] in letters[x].get_let(): #if the char is in phrase at this specific index
                                letters[x].add_point(letters[x].get_let().index(i[x])) #add a point to the index that corosponds to the char
                            else: #if there is no char in this phrase yet
                                letters[x].add_char(i[x]) #add the char and give it a point
                        x+=1
                    first_time = False

                holder = ""
                for i in letters:
                    holder+=i.best_let()
                print(holder)  
                    

    
        
        print("done")
            
       

Reading.read(True)