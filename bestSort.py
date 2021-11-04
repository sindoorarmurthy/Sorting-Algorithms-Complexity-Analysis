#SINDOORA, 1001862126
#PROGRAM DESC : COMPARING ALL ALGORITHMS FOR SAME INPUT

import time
import random
import math
import os
import matplotlib.pyplot as pyplot
import matplotlib
matplotlib.use('Agg')

from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from selection_sort import selectionSort
from merge_sort import mergeSort, merge
from quick_sort import quick_sort, partition
from quicksort_threeMedians import mq_quick_sort, medianQuickSort, medianPivot, mq_partition
from heap_sort import heap_sort, heapify

def bestMain(noOfExp):
    if os.path.exists("./static/graphs/bestSorting.png"):
        os.remove("./static/graphs/bestSorting.png")

    sorting_functions = [
        bubbleSort,
        insertionSort,
        selectionSort,
        mergeSort,
        heap_sort,
        quick_sort,
        medianQuickSort
        ]

    inputSizeList=[]

    #RUN TIMES OF ALL 7 ALGORITHMS FOR ALL EXPERIMENTS ARE STORED IN A 2D ARRAY

    runTimeList=[[None for x in range(7)] for y in range(noOfExp)] #2D ARRAY INITIALIZATION

    for i in range(noOfExp):
        size = random.randint(10, 3000)
        inputSizeList.append(size)
        #print(size)

        input=[]
        for x in range(size):
            input.append(random.randint(-size,size))
        
        #print(input)
        for j in range(7):
            start = time.time()
            if (sorting_functions[j]==quick_sort or sorting_functions[j]==medianQuickSort):
                sorting_functions[j](input,0,len(input)-1)
            else:
                sorting_functions[j](input)
            
            runTimeList[i][j]=time.time() - start 
        
    #print(inputSizeList, runTimeList)

    x, y = zip(*sorted(zip(inputSizeList, runTimeList)))
    #print(x,y)

    bubbleSortAlg=[] 
    insertionSortAlg=[] 
    selectionSortAlg=[] 
    mergeSortAlg=[] 
    heapSortAlg=[]
    quickSortAlg=[]
    medianQuickSortAlg=[]
    algorithms=[]
    algorithms=[bubbleSortAlg,insertionSortAlg,selectionSortAlg,mergeSortAlg,heapSortAlg,quickSortAlg,medianQuickSortAlg]
    names=['BUBBLE SORT','INSERTION SORT','SELECTION SORT','MERGE SORT','HEAP SORT','QUICK SORT', 'MEDIAN QUICK SORT']
    for j in range(7):
        for i in range(noOfExp):
            algorithms[j].append(y[i][j])

    graphColours=['g','r','b','k','y','m','c']
    pyplot.clf()
    for j in range(len(algorithms)):
        pyplot.plot(x,algorithms[j], graphColours[j], label=names[j])
    pyplot.legend(loc="upper left")
    pyplot.title("COMPARING RUN TIME OF ALL ALGORITHMS.  EXPERIMENTS = " + str(noOfExp))
    pyplot.xlabel("Input size")
    pyplot.ylabel("Run time (seconds)")
    #pyplot.show()
    pyplot.savefig('./static/graphs/bestSorting.png')

#bestMain(<noOfExp>)

