#SINDOORA, 1001862126
#PROGRAM DESC : BUBBLE SORT

import time
import os
import random
import math
import matplotlib.pyplot as pyplot
import matplotlib
matplotlib.use('Agg')

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

def bsmain(noOfExp):
    if os.path.exists("./static/graphs/bubble.png"):
        os.remove("./static/graphs/bubble.png")
    inputSizeList=[]
    runTimeList=[]
    for i in range(noOfExp):
        size = random.randint(10, 1000)
        #print(size)
        inputSizeList.append(size)
        input=[]
        for i in range(size):
            input.append(random.randint(-size,size))
        #print("array is", input)
        start = time.time()
        bubbleSort(input)
        #print("Sorted array is : ", input)
        runTimeList.append(time.time() - start)


    x, y = zip(*sorted(zip(inputSizeList, runTimeList)))
    #print(x,y)
    pyplot.clf()
    pyplot.plot(x,y, 'r')
    pyplot.title("BUBBLE SORT.  EXPERIMENTS = " + str(noOfExp))
    pyplot.xlabel("Input size ")
    pyplot.ylabel("Run time (seconds)")
    pyplot.savefig('./static/graphs/bubble.png')

#bsmain(<noOfExp>)