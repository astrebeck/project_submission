import os, sys
from PIL import Image
import glob

size = 512,512
num = 1

for filename in glob.glob("C:\Users\Smartsrc-alex\Documents\ML_class\project_submission\Images\In\*.jpg"):

    outfile = "C:\Users\Smartsrc-alex\Documents\ML_class\project_submission\Images\Out\img_" + str(num) + ".JPEG"
    # try:
    f = open(outfile, "w+")
    f.close() 

    im = Image.open(filename)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile,"JPEG")
    # except IOError:
    #     print "cannot create thumbnail"
    print num
    num += 1