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





words = ['He TRICKED QAD Into__uK_BARFING', 'He TRICKED QAD Into__uK_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED QAD Into__uK_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD Into_un_BARFING','He TRICKED DAD INto_UM_BARFING','He TRICKED DAD INto_UM_BARFING']
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
first_time = True

for i in words: #goes through each phrase in words
    x = 0
    while x < len(i):
        if first_time: #add all chars to the phrase the first time around
            phrase.append(LetterPoints(i[x], 1))
        else:
            if i[x] in phrase[x].get_phrase(): #if the char is in phrase at this specific index
                phrase[x].add_point(phrase[x].get_phrase().index(i[x])) #add a point to the index that corosponds to the char
            else: #if there is no char in this phrase yet
                phrase[x].add_char(i[x])
            
        x+=1
    first_time = False

holder = ""
for i in phrase:
    holder+=i.best_phrase()
print(holder)  
   




