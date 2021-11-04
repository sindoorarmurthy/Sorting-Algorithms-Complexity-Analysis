#SINDOORA, 1001862126
#PROGRAM DESC : INSERTION SORT

import time
import os
import random
import math
import matplotlib.pyplot as pyplot
import matplotlib
matplotlib.use('Agg')

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j-1
        array[j + 1] = key

def ismain(noOfExp):
    if os.path.exists("./static/graphs/insertion.png"):
        os.remove("./static/graphs/insertion.png")
    inputSizeList=[]
    runTimeList=[]
    for i in range(noOfExp):
        size = random.randint(10, 10000)
        #print(size)
        inputSizeList.append(size)
        input=[]
        for i in range(size):
            input.append(random.randint(-size,size))
        #print("array is", input)
        start = time.time()
        insertionSort(input)
        #print("Sorted array is : ", input)
        runTimeList.append(time.time() - start)

    x, y = zip(*sorted(zip(inputSizeList, runTimeList)))
    #print(x,y)
    pyplot.clf()
    pyplot.plot(x,y, 'r')
    pyplot.title("INSERTION SORT.  EXPERIMENTS = " + str(noOfExp))
    pyplot.xlabel("Input size ")
    pyplot.ylabel("Run time (seconds)")
    #pyplot.show()
    pyplot.savefig('./static/graphs/insertion.png')

#ismain(<noOfExp>)
