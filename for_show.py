import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',145)

to_read = ["quzet down  class  now can tell tell  me what the engraving  on this ancient greek  grave marker  represents", "mr  perhaps","oh  thats  krckos  eating his  kids  kids","kronos was king of the  gods mean er the titans  ad didnt didnt trust his kids  they wiere the gods  so he ate them  but his wife  gave him arik to eat instead  of zeks and when zeus grew hp  ticked dad into um barfing barfing  hp the other kids then there was  big gods versls titans nar  ad the gods won"]

for r in to_read: #as long as there's something in the results list- so there's text that's being read
    print(r)
    engine.say(r)
    engine.runAndWait()