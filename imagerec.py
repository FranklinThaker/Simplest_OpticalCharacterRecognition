from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from functools import reduce
   
def whatNumIsThis(filepath):
    matchedAr = []
    loadExamps = open('numArEx.txt',"r").read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filepath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')

            eachPixInQ = inQuestion.split('],')

            x =0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x += 1
    #print(matchedAr)
    x = Counter(matchedAr)
    print(x)

    graphX = []
    graphY = []

    for eachThing in x:
        print(eachThing)
        graphX.append(eachThing)
        print(x[eachThing])
        graphY.append(x[eachThing])

    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)
    ax1.imshow(iar)
    ax2.bar(graphX,graphY, align='center')
    plt.ylim(400)
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    plt.show()
    

whatNumIsThis('images/test.png')      
