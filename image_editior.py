#https://www.geeksforgeeks.org/change-image-resolution-using-pillow-in-python/#
#https://note.nkmk.me/en/python-numpy-opencv-image-binarization/
import numpy as np
from PIL import Image
from reader import Reading 

my_image = "temp.jpg"
open_image = Image.open(my_image)

#default
open_image.save("temp.jpg", quality = 95, dpi = (300,300))
gray_img = np.array(Image.open("temp.jpg").convert('L'))
pil_img = Image.fromarray(gray_img)
print(pil_img.mode)

pil_img.save("to_read.jpg")
Reading.read(True)