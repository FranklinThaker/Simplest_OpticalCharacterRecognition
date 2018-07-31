#Converting  Image into Numeric Form
#Just For Understanding :)

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
i = Image.open('images/dot.png')
iar = np.asarray(i)
print(iar)
plt.imshow(iar)
plt.show() #plotting image 8 x 8

#####################Explaining above code#############
'''[
   [  0   0   0 255] First pixel in FIRST ROW our 8 x 8 image
   [255 255 255 255] Second pixel in FIRST ROW our 8 x 8 image
   [255 255 255 255] Third pixel in FIRST ROW our 8 x 8 image
   [255 255 255 255] ..
   [255 255 255 255] ..
   [255 255 255 255] ..
   [255 255 255 255] ..
   [255 255 255 255] Eight pixel in FIRST ROW our 8 x 8 image
   ]
   meaning of each value :)
   255 255 255 255
    R   G   B Transperancy Level
'''
