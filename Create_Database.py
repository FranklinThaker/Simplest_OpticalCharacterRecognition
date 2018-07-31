import numpy as np
from PIL import Image
def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVersion in versionsWeHave:
            print (str(eachNum)+'.'+str(eachVersion))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVersion)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.asarray(ei)            
            eiar1 = str(eiar.tolist())
           
            lineToWrite = str(eachNum)+'::'+eiar1+'\n'
            numberArrayExamples.write(lineToWrite)

createExamples()

print("Database successfully created :) ")
