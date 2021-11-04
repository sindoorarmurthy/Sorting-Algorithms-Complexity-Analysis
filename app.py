#SINDOORA, 1001862126
#PROGRAM DESC : BUILDING GUI USING FLASK

import matplotlib.pyplot as pyplot
from flask import Flask, redirect, url_for, render_template, request, make_response
from bubble_sort import bubbleSort , bsmain
from insertion_sort import insertionSort , ismain
from selection_sort import selectionSort , ssmain
from merge_sort import mergeSort, merge , msmain
from quick_sort import quick_sort, partition , qsmain
from quicksort_threeMedians import mq_quick_sort, medianQuickSort, medianPivot, mq_partition , mqsmain
from heap_sort import heap_sort, heapify , hsmain
from bestSort import bestMain

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template('homepage.html')

@app.route("/backToAlgo")
def backToA():
    return render_template('index.html')

@app.route('/selectDisplay', methods=["POST","GET"])
def display():
  if request.method== "POST":
    return render_template('index.html')


@app.route('/selectAlgorithm', methods=["POST","GET"])
def selectAlgorithm():
  if request.method== "POST":
    value=request.form['algorithm']
    noOfExperiments=request.form['noOfExp']
    noOfExperiments=int(noOfExperiments)
    sorting(value,noOfExperiments)
    r = make_response(render_template('graph.html', name=value ))
    r.headers.set('Cache-Control',  "no-cache, no-store, must-revalidate")
    r.headers.set('Pragma', "no-cache")
    r.headers.set('Expires', "0")
    r.headers.set('Cache-Control', "public, max-age=0")
    return r

def sorting(alg, noOfExp):
  if alg == 'bubble_sort' :
    try :
      bsmain(noOfExp)
    except :
      print("Error in execution")

  elif alg == 'insertion_sort' :
    print("Im here")
    try :
      ismain(noOfExp)
    except :
      print("Error in execution")

  elif alg == 'selection_sort' :
    try :
      ssmain(noOfExp)
    except :
      print("Error in execution")

  elif alg == 'merge_sort' :
    try :
      msmain(noOfExp)
    except :
      print("Error in execution")

  elif alg == 'quick_sort' :
    try :
      qsmain(noOfExp)
    except :
      print("Error in execution")

  elif alg == 'median_quicksort' :
    try :
      mqsmain(noOfExp)
    except :
      print("Error in execution")

  elif alg == 'heap_sort' :
    try :
      hsmain(noOfExp)
    except :
      print("Error in execution")
  
  elif alg == 'all_alg' :
    try :
      bestMain(noOfExp)
    except :
      print("Error in execution")

if __name__ == '__main__':
  app.run(debug=True)
 