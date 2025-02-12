import pyttsx3
import PIL.Image
import easyocr
from PIL import Image
from PIL import ImageDraw

engine = pyttsx3.init()
engine.setProperty('rate',145)

to_read = ["quzet down  class  now can tell tell  me what the engraving  on this ancient greek  grave marker  represents", "mr  perhaps","oh  thats  krckos  eating his  kids  kids","kronos was king of the  gods mean er the titans  ad didnt didnt trust his kids  they wiere the gods  so he ate them  but his wife  gave him arik to eat instead  of zeks and when zeus grew hp  ticked dad into um barfing barfing  hp the other kids then there was  big gods versls titans nar  ad the gods won"]

for r in to_read: #as long as there's something in the results list- so there's text that's being read
    print(r)
    engine.say(r)
    engine.runAndWait()
im = PIL.Image.open("hearstopper.jpg")
reader = easyocr.Reader(['en'], gpu = False) #en = english, there's no gpu (i checked :/)
result = reader.readtext("hearstopper.jpg", contrast_ths=0, adjust_contrast=.9, width_ths= 1.5, add_margin= 0, decoder= 'beamsearch') #conttrast thereshold sets minum contrast and adjusts it, adding margins increase bound box in all directions,                # width: if something outside a box is close to something within one it'll merge the two
draw = ImageDraw.Draw(im)
for results in result:
    p0, p1, p2, p3 = results[0]
    draw.line([*p0,*p1,*p2,*p3,*p0], fill = 'yellow', width = 2)
    im.show()
#print(result)

for r in result:
    print(r[1])
print("done")