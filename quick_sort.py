#SINDOORA, 1001862126
#PROGRAM DESC : QUICK SORT

import time
import random
import os
import math
import matplotlib.pyplot as pyplot
import sys
import matplotlib
matplotlib.use('Agg')

def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    for j in range(low,high):
        if (arr[j] < pivot):
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i + 1],arr[high]=arr[high],arr[i+1]
    return i + 1

def quick_sort(array,start,end):   
    #print(sys.getrecursionlimit())
    if sys.getrecursionlimit()!=100000:
        sys.setrecursionlimit(100000)
    if (start>=end):
        return 
    index =partition(array,start,end)
    quick_sort(array,start, index-1)
    quick_sort(array,index+1 ,end)

def qsmain(noOfExp):
    if os.path.exists("./static/graphs/quick.png"):
        os.remove("./static/graphs/quick.png")
    inputSizeList=[]
    runTimeList=[]
    for i in range(noOfExp):
        size = random.randint(100, 100000)
        #print(size)
        inputSizeList.append(size)
        input=[]
        for i in range(size):
            input.append(random.randint(-size,size))
        #print("array is", input)
        start = time.time()
        quick_sort(input,0,len(input)-1)
        #print("Sorted array is : ", input)
        runTimeList.append(time.time() - start)

    x, y = zip(*sorted(zip(inputSizeList, runTimeList)))
    #print(x,y)
    pyplot.clf()
    pyplot.plot(x,y, 'g')
    pyplot.title("QUICK SORT.  EXPERIMENTS = " + str(noOfExp))
    pyplot.xlabel("Input size ")
    pyplot.ylabel("Run time (seconds)")
    #pyplot.show()
    pyplot.savefig('./static/graphs/quick.png')
    
#qsmain(<noOfExp>)