#SINDOORA, 1001862126
#PROGRAM DESC : SELECTION SORT

import time
import random
import math
import os
import matplotlib.pyplot as pyplot
import matplotlib
matplotlib.use('Agg')

def selectionSort(array):
    n=len(array)
    for i in range(0, n-1):
        minPos = i
        for j in range(i+1, n):
            if array[j] < array[minPos]:
                minPos = j       
        array[i], array[minPos] = array[minPos], array[i]

def ssmain(noOfExp):
    if os.path.exists("./static/graphs/selection.png"):
        os.remove("./static/graphs/selection.png")
    inputSizeList=[]
    runTimeList=[]
    for i in range(noOfExp):
        size = random.randint(500, 11000)
        #print(size)
        inputSizeList.append(size)
        input=[]
        for i in range(size):
            input.append(random.randint(-size,size))
        #print("array is", input)
        start = time.time()
        selectionSort(input)
        #print("Sorted array is : ", input)
        runTimeList.append(time.time() - start)

    x, y = zip(*sorted(zip(inputSizeList, runTimeList)))
    #print(x,y)
    pyplot.clf()
    pyplot.plot(x,y, 'g')
    pyplot.title("SELECTION SORT.  EXPERIMENTS = " + str(noOfExp))
    pyplot.xlabel("Input size ")
    pyplot.ylabel("Run time (seconds)")
    #pyplot.show()
    pyplot.savefig('./static/graphs/selection.png')

#ssmain(<noOfExp>)

