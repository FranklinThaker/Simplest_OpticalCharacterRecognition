from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from functools import reduce
   
'''def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            #print(eachPix)
            avgNum = reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr)/len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 0
    return newAr
'''
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
    
    
'''
i1 = Image.open('images/numbers/0.1.png')
iar1 = np.asarray(i1, dtype='int64')

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.asarray(i2, dtype='int64')

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.asarray(i3, dtype='int64')

i4 = Image.open('images/sentdex.png')
iar4 = np.asarray(i4, dtype='int64')


threshold(iar1)
threshold(iar2)
threshold(iar3)
threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax1.imshow(iar1)

ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax2.imshow(iar2)

ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax3.imshow(iar3)

ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)
ax4.imshow(iar4)

plt.show()
'''
