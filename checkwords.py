#just a temp file where I tested the edit metehod

import json
with open('words_dictionary.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)

#words = ['He TRICKED QAD Into__uK_BARFING', 'He TRICKED QAD Into__uK_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING']
#words = [
'''KzoNoS NAS KInG OF The',
'KzoNS NAS KING OF The',
'KzoNS NAS KING OF The',
'KzowS NAS KInG OF The',
'Kzons WAS KInG OF The',
'Kzons WAS KInG OF The',
'KzowS NAS KInG OF The',
'Kzons WAS KInG OF The',
'Kzons WAS KInG OF The',
'KzoNoS NAS KInG OF The',
'KzoNS NAS KING OF The',
'KzoNS NAS KING OF The',
'KzowS NAS KInG OF The',
'Kzons WAS KInG OF The',
'Kzons WAS KInG OF The',
'KzowS NAS KInG OF The',
'Kzons WAS KInG OF The',
'Kzons WAS KInG OF The',
'KzoNoS NAS KInG OF The',
'KzoNS NAS KING OF The',
'KzoNS NAS KING OF The',
'KzowS NAS KInG OF The',
'Kzons WAS KInG OF The',
'Kzons WAS KInG OF The',
'KzowS NAS KInG OF The',
'Kzons WAS KInG OF The',
'Kzons WAS KInG OF The',
'KzoNoS NAS KInG OF The',
'KzoNS NAS KING OF The',
'KzoNS NAS KING OF The',
'KzowS NAS KInG OF The',
'Kzons WAS KInG OF The',
'Kzons WAS KInG OF The',
'KzowS NAS KInG OF The',
'Kzons WAS KInG OF The',
'Kzons WAS KInG OF The']
words = ['Gods; [ Mean . Er',
'Gods; [ Mean. Er',
'Gods; [ Mean. Er',
'~Gods; [ Mean_ Er .',
'\'GODS; [ Mean_ Er .\'',
'\'GODS; [ Mean_ Er .\'',
'~Gods; [ Mean_ Er_.T',
'\'GODS; [ Mean_ Er_.1',
'\'GODS; [ Mean_ Er_.1',
'Gods; [ Mean . Er',
'Gods; [ Mean. Er',
'Gods; [ Mean. Er',
'~Gods; [ Mean_ Er .',
'\'GODS; [ Mean_ Er .\'',
'\'GODS; [ Mean_ Er .\'',
'~Gods; [ Mean_ Er_.T\'',
'GODS; [ Mean_ Er_.1',
'GODS; [ Mean_ Er_.1',
'Gods; [ Mean . Er',
'Gods; [ Mean. Er',
'Gods; [ Mean. Er',
'~Gods; [ Mean_ Er    .', 
'\'GODS; [ Mean_ Er .\'',
'\'GODS; [ Mean_ Er .\'',
'~Gods; [ Mean_ Er_.T',
'\'GODS; [ Mean_ Er_.1',
'\'GODS; [ Mean_ Er_.1',
'Gods; [ Mean . Er',
'Gods; [ Mean. Er',
'Gods; [ Mean. Er',
'~Gods; [ Mean_ Er .',
'\'GODS; [ Mean_ Er .\'',
'\'GODS; [ Mean_ Er .\'',
'~Gods; [ Mean_ Er_.T',
'\'GODS; [ Mean_ Er_.1',
'GODS; [ Mean_ Er_.1']
words = ['? Ce DIDNT [ust HIS',
'P Ke DIDNT Wust HIS',
'P Ke DIDNT Wust HIS',
'He DIDNT Irust HIS k',
') Ke DIDNT WRuSt HIS k',
') Ke DIDNT WRuSt HIS k',
'P He DIDNT Irust HIS KII',
') Ke DIDNT Irust HIS KIC',
') Ke DIDNT Irust HIS KIC',
'? Ce DIDNT [ust HIS',
'P Ke DIDNT Wust HIS',
'P Ke DIDNT Wust HIS',
'He DIDNT Irust HIS k',
') Ke DIDNT WRuSt HIS k',
') Ke DIDNT WRuSt HIS k',
'P He DIDNT Irust HIS KII',
') Ke DIDNT Irust HIS KIC',
') Ke DIDNT Irust HIS KIC',
'? Ce DIDNT [ust HIS',
'P Ke DIDNT Wust HIS',
'P Ke DIDNT Wust HIS',
'He DIDNT Irust HIS k',
') Ke DIDNT WRuSt HIS k',
') Ke DIDNT WRuSt HIS k',
'P He DIDNT Irust HIS KII',
') Ke DIDNT Irust HIS KIC',
') Ke DIDNT Irust HIS KIC',
'? Ce DIDNT [ust HIS',
'P Ke DIDNT Wust HIS',
'P Ke DIDNT Wust HIS',
'He DIDNT Irust HIS k',
') Ke DIDNT WRuSt HIS k',
') Ke DIDNT WRuSt HIS k',
'P He DIDNT Irust HIS KII',
') Ke DIDNT Irust HIS KIC',
') Ke DIDNT Irust HIS KIC']'''
phrases = ['Qhjet Down',
'Qhiet Down',
'Qhiet Down',
'Qhiet Down',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'Qhiet Down',
'Qhiet Down',
'Qhiet Down',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'Qhiet Down',
'Qhiet Down',
'Qhiet Down',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',
'Qhiet Down',
'Qhiet Down',
'Qhiet Down',
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;', 
'\'Quzet Down;',
'\'Quzet Down;',
'\'Quzet Down;',]
'''phrases = ['TICKED DAD IntO__.HM.BARFING',
'TICKED DAD INto_uM: BARFING',
'TICKED DAD INto_M:BARFING',
'TICKED DAD INto_M:BARFING',
'TICKED DAD Into__uM: BARFInG',
'TICKED DAD INto__uM:BARFING',
'TICKED DAD INto__uM:BARFING',
'He TPICKED DAD Into__uMBARFInG',
'He TRICKED DAD Into__UM:BARFING',
'He TRICKED DAD Into__UM:BARFING',
'TICKED DAD INto_uM: BARFING',
'TICKED DAD INto_M:BARFING',
'TICKED DAD INto_M:BARFING',
'TICKED DAD Into__uM: BARFInG',
'TICKED DAD INto__uM:BARFING',
'TICKED DAD INto__uM:BARFING',
'He TPICKED DAD Into__uMBARFInG',
'He TRICKED DAD Into__UM:BARFING',
'He TRICKED DAD Into__UM:BARFING',
'TICKED DAD INto_uM: BARFING',
'TICKED DAD INto_M:BARFING',
'TICKED DAD INto_M:BARFING',
'TICKED DAD Into__uM: BARFInG',
'TICKED DAD INto__uM:BARFING',
'TICKED DAD INto__uM:BARFING',
'He TPICKED DAD Into__uMBARFInG',
'He TRICKED DAD Into__UM:BARFING',
'He TRICKED DAD Into__UM:BARFING',
'TICKED DAD INto_uM: BARFING',
'TICKED DAD INto_M:BARFING',
'TICKED DAD INto_M:BARFING',
'TICKED DAD Into__uM: BARFInG',
'TICKED DAD INto__uM:BARFING',
'TICKED DAD INto__uM:BARFING',
'He TPICKED DAD Into__uMBARFInG',
'He TRICKED DAD Into__UM:BARFING',
'He TRICKED DAD Into__UM:BARFING']'''


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

avg = 0
maximum = 0
for i in phrases:
    length = len(i)
    avg += length
    if maximum < length:
        maximum = length
avg = avg // len(phrases)

real_phrase = []

words = []
to_read = []
junk_words = []
first_time = True
temp = [] #will hold chars to one word 
min_words = 0
max_word_index = -1
single_lets = ['a','i']


for i in phrases: #per line, goes through every possible variation one at a time
    x = 0 #the index of i
    y = 0 #the index of words[] and junk_words[]
    #print("NEW:", i)
    print("----------NEW LOOP-------------")
    print(i)
    i += " " #so the last word gets picked up
    while x < len(i): #this will go through each char of one variation
        if i[x].isalnum(): #if the char is a letter or number, add it to the list
            temp.append(i[x]) 
            #    print(i[x])
        else: #a space was found, so check if the word exists
            print(i[x])
            if not not temp: #if the prev to x wasn't a space 
                if (len(temp) > 1 or temp[0] in single_lets):# and x + 1 < len(i) -1: #if there's just a single character at the end that isn't i, or a it's probably a mistake
                    print("adding", i[x], len(temp), temp[0])
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
                            print("inc bc word")
                            max_word_index+=1
                            #print(first_time)
                        else: #word is in list and is being added to an index that's filled with words or XX
                            #print("Y ",y,"words: ",len(words), max_word_index) 
                            for w in words:
                                    if w == "XX":
                                        print(w)
                                    else:
                                        print(w.get_word())      
                            print(len(words), max_word_index, y)
                            add_to_phrase(words, temp_string, y, max_word_index)
                    else: #did not scan a word
                        if first_time: #word isn't in list but it's the first time we're adding to the list
                            words.append("XX") #filler bc there's no word 
                            junk_words.append("YY")
                            print("inc no word first time")
                            max_word_index+=1
                        else: 
                            if y > max_word_index:
                                print("inc no word, longer than words[]")
                                words.append("XX")
                                junk_words.append("YY")
                                max_word_index+=1
                            else: #word isn't in list and this isn't the first time we're adding to list (so something should be in words[y])- we're adding what's scanned to junk
                                #print(max_word_index, y, temp_string)
                                if junk_words[y] == "YY":
                                    junk_words[y] = (LetterPoints(temp_string,1)) #replacing the filler with the scanned word (not in list)
                                if temp_string in junk_words[y].get_word(): #if the word is alr in junk string, give it a point
                                    junk_words[y].add_point(junk_words[y].get_word().index(temp_string)) 
                                else: #there's already a junk word, but it doesn't match anything in junk_words
                                        junk_words[y].add_word(temp_string)                                    
                    print("inc y", y, max_word_index, temp_string)
                    y+=1
                    temp = [] #will hold chars to one word 
                    #else:
                        #print("END MISTAKE", len(temp), x, len(i), )
                        #for w in temp:
            
            else:
                print("didn't change")                #    print(w)
        #print(y, ":", i, ":" ,i[x], x, len(i))
        x+=1
    first_time = False
    temp = []

holder = ""
c = 0

#i need to make sure the last word in the phrase is like an actual word
#also if two versions of phrase are next to each other and similar combine them but sometimes they can be similar?
for l in words:
    print(l)
#words.remove("XX" )
while c < len(words):
    #print(c)
    #print(words[c])
    if words[c] == "XX":
        print("yay")
        if c != len(words) - 1: #if the last word is junk
            print(junk_words[c].best_word())
            holder += junk_words[c].best_word()
    else:
         holder += words[c].best_word()
    c+=1 
   
print("FINAL")
print(holder)  



# Access the data'''
if ",k," in data:
    print("yes") 
   




