#SINDOORA, 1001862126
#PROGRAM DESC : HEAP SORT

import time
import os
import random
import math
import matplotlib.pyplot as pyplot
import matplotlib
matplotlib.use('Agg')

#heap_sort--build a max heap, replace root with last element , heapify if necessary , repeat for all
def heap_sort(array):
    n = len(array)
    noOf_NonLeaf_nodes= n - pow(2, math.floor(math.log2(n))-1)
    for i in range(noOf_NonLeaf_nodes, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]  
        heapify(array, i, 0)

#heapify- compare parent with children and swap if necessary
def heapify(array, n, parent_node_pos):
    max_node_pos = parent_node_pos  
    left_child_pos= (2 * parent_node_pos) + 1     
    right_child_pos = (2 * parent_node_pos) + 2    
 
    if left_child_pos < n and array[max_node_pos] < array[left_child_pos]:
        max_node_pos = left_child_pos
    if right_child_pos < n and array[max_node_pos] < array[right_child_pos]:
        max_node_pos = right_child_pos
 
    if max_node_pos != parent_node_pos:
        array[parent_node_pos], array[max_node_pos] = array[max_node_pos], array[parent_node_pos]  
        #print("array IS :", array)
        heapify(array, n, max_node_pos)
 
def hsmain(noOfExp):
    if os.path.exists("./static/graphs/heap.png"):
        os.remove("./static/graphs/heap.png")
    inputSizeList=[]
    runTimeList=[]
    for i in range(noOfExp):
        size = random.randint(10, 200000)
        #print(size)
        inputSizeList.append(size)
        input=[]
        for i in range(size):
            input.append(random.randint(-size,size))
        #print("array is", input)
        start = time.time()
        heap_sort(input)
        #print("Sorted array is : ", input)
        runTimeList.append(time.time() - start)

    x, y = zip(*sorted(zip(inputSizeList, runTimeList)))
    #print(x,y)
    pyplot.clf()
    pyplot.plot(x,y, 'c')
    pyplot.title("HEAP SORT.  EXPERIMENTS = " + str(noOfExp))
    pyplot.xlabel("Input size ")
    pyplot.ylabel("Run time (seconds)")
    #pyplot.show()
    pyplot.savefig('./static/graphs/heap.png')
    
#hsmain(<noOfExp>)