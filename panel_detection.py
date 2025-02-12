from PIL import Image
import imageio.v2 as imageio
import os
import sys
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from skimage.measure import label
from skimage.color import label2rgb
import numpy as np
from skimage.color import rgb2gray
from skimage.feature import canny
from skimage.morphology import dilation
from scipy import ndimage as ndi
from skimage.measure import regionprops

class Slice():
    def split_panels():
        #root = Tk()
        #root.lift()
        #root.withdraw()
        # now this code copied from tutorial blog Max Halford
            #https://maxhalford.github.io/blog/comic-book-panel-segmentation/

        #path = askdirectory(title='Select Folder containing jpg image') # shows dialog box and return the path
        #if path == "" : sys.exit(0)
        path_of_the_directory = "path" 

        #answer = messagebox.askyesno("Question!","Show preview page before panels?")
        #initd= os.path.dirname(path)
        pathd = "path/panels"
        #if pathd == "" : sys.exit(0)
        t = 1000
        os.makedirs(pathd+'/panels',exist_ok=True)

        #process all files in directory image
        for files in os.listdir(path_of_the_directory):
            #if files.endswith(ext):
            #Loading an image
            im = imageio.imread(path_of_the_directory+'/'+files)
            Image.fromarray(im)
            '''if answer == True:
                t += 1
                Image.fromarray(im).save(f'{pathd}/panels/{t}.jpg')'''

            #Canny edge detection
            grayscale = rgb2gray(im)
            Image.fromarray((grayscale * 255).astype('uint8'), 'L')
            edges = canny(grayscale)
            Image.fromarray(edges)

            # Edge thickening via dilation
            thick_edges = dilation(dilation(edges))
            Image.fromarray(thick_edges)

            #Filling holes
            segmentation = ndi.binary_fill_holes(thick_edges)
            Image.fromarray(segmentation)


            #Labelling each patch
            labels = label(segmentation)
            Image.fromarray(np.uint8(label2rgb(labels, bg_label=0) * 255))


            # Regrouping patches into panels
            def do_bboxes_overlap(a, b):
                return (
                    a[0] < b[2] and
                    a[2] > b[0] and
                    a[1] < b[3] and
                    a[3] > b[1]
                )

            def merge_bboxes(a, b):
                return (
                    min(a[0], b[0]),
                    min(a[1], b[1]),
                    max(a[2], b[2]),
                    max(a[3], b[3])
                )

            regions = regionprops(labels)
            panels = []

            for region in regions:

                for i, panel in enumerate(panels):
                    if do_bboxes_overlap(region.bbox, panel):
                        panels[i] = merge_bboxes(panel, region.bbox)
                        break
                else:
                    panels.append(region.bbox)

            # Remove small panels
            for i, bbox in reversed(list(enumerate(panels))):
                area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
                if area < 0.01 * im.shape[0] * im.shape[1]:
                    del panels[i]

            # Now i add this code to "order" panel in the correct order
            # (the code in the tutorial stopped with recursive error,
            # maybe I copied a few lines wrong)
            # I don't know python and english sorry :)


            for j in range(0, len(panels)-1):
                for i in range(j+1 ,len(panels)):
                    if int(panels[i][0] - panels[j][0])>=0 and int(panels[i][0] - panels[j][0]) <= 100 :
                        if panels[i][1] <= panels[j][1]:
                            swap = panels[i]
                            panels[i]=panels[j]
                            panels[j]=swap
                        else:
                            if panels[i][0] <= panels[j][0] :
                                swap = panels[i]
                                panels[i]=panels[j]
                                panels[j]=swap


            #swap "double height panels"
            i=len(panels)-2
            for j in enumerate(panels):
                if i >= 0:
                    #print (panels[i])
                    #print (panels[i+1])
                    if panels[i+1][2] - panels[i][2] > -10 and panels[i+1][2] - panels[i][2]<10 :
                        if panels[i+1][0] - panels[i][0] > 40:
                            swap = panels[i]
                            panels[i]=panels[i+1]
                            panels[i+1]=swap
                i = i-1
            # save panels in "panels" sub-folder
            for i, bbox in enumerate(panels, start=1):
                #print (bbox[0])  #'punto alto sinistra riga
                #print ( bbox[1]) #'        ''          colonna
                #print(bbox[2])   #'punto basso destra  riga
                #print (bbox[3])  #'        ''          colonna
                t += 1
                panel = im[bbox[0]:bbox[2], bbox[1]:bbox[3]]
                Image.fromarray(panel).save(f'{pathd}/panels/{t}.jpg')


        #else:

            # continue
        #answer = messagebox.askyesno("Save PDF","Convert panels in one pdf file? (Panel.pdf)")

        '''if answer == True:
            os.chdir(pathd+ "/panels/")
            images = [i for i in os.listdir(os.getcwd()) if i.endswith(".jpg")]

            with open(f'{pathd}/Panels.pdf', "wb") as f:
                f.write(img2pdf.convert(images))'''

        #if pdfinp == 1 : shutil.rmtree(path)
Slice.split_panels()