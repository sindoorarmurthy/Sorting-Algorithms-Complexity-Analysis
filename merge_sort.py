#SINDOORA, 1001862126
#PROGRAM DESC : MERGE SORT

import time
import os
import random
import math
import matplotlib.pyplot as pyplot
import matplotlib
matplotlib.use('Agg')

def merge(leftSubArray, rightSubArray):
    i = j = 0
    merged_array=[]
    while (i < len(leftSubArray) and j < len(rightSubArray)):
        if leftSubArray[i] < rightSubArray[j]:
            merged_array.append(leftSubArray[i])
            i=i+1
        else:
            merged_array.append(rightSubArray[j])
            j=j+1
    while i < len(leftSubArray):
        merged_array.append(leftSubArray[i])
        i= i+1
    while j < len(rightSubArray):
        merged_array.append(rightSubArray[j])
        j=j+1
    #print(merged_array)
    return merged_array

def mergeSort(array):
    #print("in merge sort")
    if (len(array) == 1):
        return array
    mid = len(array)//2
    leftSubArray = array[:mid]
    rightSubArray  = array[mid:]
    leftSubArray=mergeSort(leftSubArray)
    rightSubArray=mergeSort(rightSubArray)
    return merge(leftSubArray, rightSubArray)

def msmain(noOfExp):
    if os.path.exists("./static/graphs/merge.png"):
        os.remove("./static/graphs/merge.png")
    inputSizeList=[]
    runTimeList=[]
    for i in range(noOfExp):
        size = random.randint(10, 140000)
        #print(size)
        inputSizeList.append(size)
        input=[]
        for i in range(size):
            input.append(random.randint(-size,size))
        #print("array is", input)
        start = time.time()
        sorted_array=mergeSort(input)
        #print("Sorted array is : ", sorted_array)
        runTimeList.append(time.time() - start)

    x, y = zip(*sorted(zip(inputSizeList, runTimeList)))
    #print(x,y)
    pyplot.clf()
    pyplot.plot(x,y, 'g')
    pyplot.title("MERGE SORT.  EXPERIMENTS = " + str(noOfExp))
    pyplot.xlabel("Input size ")
    pyplot.ylabel("Run time (seconds)")
    #pyplot.show()
    pyplot.savefig('./static/graphs/merge.png')

#msmain(<noOfExp>)