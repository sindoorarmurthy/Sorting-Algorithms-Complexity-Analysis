#SINDOORA, 1001862126
#PROGRAM DESC : QUICK SORT USING 3 MEDIANS

import time
import random
import math
import os
import matplotlib.pyplot as pyplot
import matplotlib
matplotlib.use('Agg')

def medianPivot(array, start, end):
    first = array[start]
    last = array[len(array)-1]
    mid = end // 2
    mediansList = [first, array[mid], last]
    #print("Median list", mediansList)
    mediansList.sort()
    middleValue = mediansList[1]
    #print("Median list", mediansList)
    dummy = array[end]
    array[end] = middleValue
    if (middleValue == first):
        first = dummy
    elif (middleValue == array[mid]):
        array[mid] = dummy
    #print("Array is:",array)
    return mq_partition(array, start, end)

def mq_quick_sort(array,start,end):   
    if (start>=end):
        return 
    index =mq_partition(array,start,end)
    mq_quick_sort(array,start, index-1)
    mq_quick_sort(array,index+1 ,end)

def mq_partition(array, start, end):
    pivot = array[end]
    i = (start - 1)
    for j in range(start,end):
        if (array[j] < pivot):
            i=i+1
            array[i],array[j]=array[j],array[i]

    array[i + 1],array[end]=array[end],array[i+1]
    return i + 1

def medianQuickSort(array, start, end):
    if (start >= end):
        return
    if (start < end):
        pi = medianPivot(array, start, end)
        mq_quick_sort(array, start, end)

def mqsmain(noOfExp):   
    if os.path.exists("./static/graphs/median.png"):
        os.remove("./static/graphs/median.png")
    inputSizeList=[]
    runTimeList=[]
    for i in range(noOfExp):
        size = random.randint(10, 150000)
        #print(size)
        inputSizeList.append(size)
        input=[]
        for i in range(size):
            input.append(random.randint(-size,size))
        #print("array is", input)
        start = time.time()
        medianQuickSort(input ,0, len(input)-1)
        #print("Sorted array is : ", input)
        runTimeList.append(time.time() - start)

    x, y = zip(*sorted(zip(inputSizeList, runTimeList)))
    #print(x,y)
    pyplot.clf()
    pyplot.plot(x,y, 'g')
    pyplot.title("QUICK SORT WITH 3 MEDIANS.  EXPERIMENTS = " + str(noOfExp))
    pyplot.xlabel("Input size ")
    pyplot.ylabel("Run time (seconds)")
    #pyplot.show()
    pyplot.savefig('./static/graphs/median.png')

#mqsmain(<noOfExp>)