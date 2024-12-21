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
'GODS; [ Mean_ Er_.1']'''
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
') Ke DIDNT Irust HIS KIC']


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
    def get_phrase(self):
        return self.char
    #adds new char and gives it a point
    def add_char(self, char):
        self.points.append(1)
        self.char.append(char)
    def best_phrase(self):
        return self.char[self.points.index(max(self.points))]



def add_to_phrase(phrase, temp_string, y):
    if phrase[y] == "XX":
        phrase[y] = LetterPoints(temp_string,1)
    elif temp_string in phrase[y].get_phrase(): #if the word is in phrase at this specific index or there was no phrase at this index
        phrase[y].add_point(phrase[y].get_phrase().index(temp_string)) #add a point to the index that corosponds to the char
    else: #if there is no char in this phrase yet
        phrase[y].add_char(temp_string)

avg = 0
maximum = 0
for i in words:
    length = len(i)
    avg += length
    if maximum < length:
        maximum = length
avg = avg // len(words)

real_phrase = []

phrase = []
to_read = []
junk_words = []
first_time = True
temp = [] #will hold chars to one word 
min_words = 0

for i in words: #goes through each version of the phrase (i is a specific phrase)
    x = 0 #x is the number of indexs we've traveled in i
    y = 0 #y is the number of words in phrase[]
    while x < len(i): 
        if i[x] != " " and i[x] != "_" and i[x] != "-" and i[x] != "*" and i[x] != "&" and i[x] != "?" and i[x] != ";" and i[x] != ":": #if there's no space, there's a word so add it to temp
            temp.append(i[x])
        else: #a space was found, so check if the word exists
            #min_words+=1 #a new word is here, regardless of if it scanned well
            if not not temp: #if the prev to x wasn't a space
                temp_string = "".join(temp)    
                t = "," + temp_string.lower() + ","            
                if t.lower() in data: #if the word is in the list of words
                    temp_string += " "
                    if first_time or y > min_words:
                        phrase.append(LetterPoints(temp_string, 1))
                        junk_words.append("YY")
                        min_words+=1
                    else:
                        add_to_phrase(phrase, temp_string, y)
                else: #words it not a word
                    if first_time:
                        phrase.append("XX")#(LetterPoints("XX ", 0)) #filler bc there's no word
                        junk_words.append("YY")
                    else: #add to junk_words (we're just gonna read this out loud)
                        #print(temp_string)

                        temp_string += " "
                        if junk_words[y] == "YY":
                            junk_words[y] = (LetterPoints(temp_string,1))
                        if temp_string in junk_words[y].get_phrase(): #if the word is already in the junk, increase the point
                            junk_words[y].add_point(junk_words[y].get_phrase().index(temp_string))
                        else: #if jw isn't empty but the word isn't there, add the word
                            junk_words[y].add_char(temp_string)
                y+=1

                temp = [] #will hold chars to one word      
        x+=1
    #if the phrase is the last word, add it
    if not not temp:
        temp_string = "".join(temp)
        #print(temp_string)
        t = "," + temp_string.lower() + ","            
        if t.lower() in data:
            if first_time or y > min_words:
                        phrase.append(LetterPoints(temp_string, 1))
            else:
                add_to_phrase(phrase,temp_string,y)
            
    first_time = False
    temp = []

holder = ""
c = 0

#i need to make sure the last word in the phrase is like an actual word
#also if two versions of phrase are next to each other and similar combine them but sometimes they can be similar?
for l in phrase:
    print(l.get_phrase())
#phrase.remove("XX" )
while c < len(phrase):
    #print(c)
    #print(phrase[c])
    if phrase[c] == "XX":
        print("yay")
        if c != len(phrase) - 1: #if the last word is junk
            print(junk_words[c].best_phrase())
            holder += junk_words[c].best_phrase()
    else:
         holder += phrase[c].best_phrase()
    c+=1 
   
print("FINAL")
print(holder)  



# Access the data'''
if ",k," in data:
    print("yes") 
   




