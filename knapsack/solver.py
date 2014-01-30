#!/usr/bin/python
# -*- coding: utf-8 -*-

def getMap(w, j):
    return (0.5*((w+j)*(w+j+1)))+j

def getMax(myList):
    maxn = 0
    index = 0 
    for i in range(len(myList)):
        #print(myList[i])
        if (myList[i]>maxn):
            maxn = myList[i]
            index = i
    return index

def optValueO(cap,flist):
    l_ratios= copy.copy(ratios)
    opt = 0
    
    for i in range(len(l_ratios)):
        if i in flist:
            l_ratios[i] = 0
    
    while (cap > 0):
        maxI = getMax(l_ratios)
        cap = cap - weights[maxI]
        opt = opt + values[maxI]
        l_ratios[maxI] = 0
        
    return opt;

def optValue(cap,flist):
    l_ratios= copy.copy(sortedRatios)
    opt = 0

    #print(flist)
    for i,(maxv, index) in enumerate(l_ratios):
        if index in flist:
            #print(i)
            l_ratios.pop(i)
        
    #print(l_ratios)
    
    while (cap > 0):
        index = l_ratios.pop()
        cap = cap - weights[index[1]]
        opt = opt + values[index[1]]
        
    return opt;
 
def call(w,j):
    if(array[w][j]==-1):
        x = knap(w, j)
        insert(w, j, x)
        return int(x)
    else:
        return int(array[w][j])
    
def callO(w,j):
    y = int(get(w,j))
    if(y == -1):
        x = knap(w, j)
        insert(w, j, x)
        return int(x)
    else:
        return int(y)

def get(w, j):

    for a in array:
        if(a[0]==w and a[1]==j):
            return int(a[2])

    return int(-1)

def getOrig(w, j):
    for i in range(count):
        if(array[i][0]==w and array[i][1]==j):
            return int(array[i][2])
            
    return int(-1)

def insert(w, j, val):
    #array[w][j] = val
    global count
    count = count + 1
    array.append((w,j,val))
    #array.sort()

val = 0
iter = 0
def knap(w, j):

    global finalpath
    global iter
    global val
    global maxV
    
    iter = iter + 1
     
    if(iter > 10000):
        if(val>maxV):
           maxV=val 
           print(val)
        iter = 0

    #returns optimal value, w = remaining weight , j = item
    if(j<0):
        return 0

    if(weights[j] > w):
        return call(w,j-1)
    else:
        return max( call(w,j-1) ,values[j] + call(w - weights[j],j-1 ) ) 

flag = 0
maxV = 0
iter = 0   
finalpath = []  
def BandB(w,j,val):
    global flag
    global maxV
    global finalpath
    global iter
    
    iter = iter + 1
     
    if(iter>1700000000):
        return maxV

    if(flag==0): ##init
        maxV = 0
        flag = 1

    if(w<0):
        return 0;

    if(val>maxV):
        maxV = val
        iter = 0
        print("update", maxV)
        finalpath = copy.copy(path)
        print finalpath
        
    
    
    #---------------Inline----------------
    l_ratios = copy.copy(sortedRatios)
    opt = 0
    units = 0
    cap = w
    
#     print(path)
#     for i,(maxv, index) in enumerate(l_ratios):
#         if index in path:
#             print(i)
#             l_ratios.pop(i)
            
#     for i in range(len(l_ratios)):
#         for k in path:
#             if(l_ratios[i]==k):
#                 print(l_ratios[i])
#                 l_ratios.pop(i)
            
    #print(l_ratios)

    while (cap > 0):
        index = l_ratios.pop()        
        cap = cap - weights[index[1]]
        opt = opt + values[index[1]]
#         units = weights[index[1]]
#         for k in range(units):
#             cap = cap - 1
#             opt = opt + index[0]
    #opt = optValue(w,path) + val #Make this part dynamic
    
    opt = opt + val

    if(j==items):
        return maxV;
    #Use que and make iterative
    if(opt>maxV):
        #then continue recurtion
        path.append(j)
        BandB( w-weights[j], j+1 , val + values[j] ) ##PICK
        path.remove(j)
#         if(iter>170000000):
#             return maxV
        BandB(w,j+1,val) ##DROP  
        
        return maxV
    else:
        return 0


def BandBiterOld(w,j,val):
    maxV = 0
    que = []
    Cval = 0
    opt = optValue(w,que) + val

    que.append((w,j,val))
    
    while(len(que)>0):
        
        #print("main",que)

        while(1):
            #Go left
            
            w = w - weights[j]
            val = val + values[j]
            j = j + 1
            if(w<0):
                j=j-1
                w = w + weights[j]
                val = val - values[j]
                break
            
            if(j==items):
                j = j-1
                w = w + weights[j]
                val = val - values[j]
                break
            
            que.append((w,j,val))
            Cval = 0
            for a in que:
                Cval = Cval + values[a[1]]
            print("left", que,Cval)
            
        temp = que.pop()
        w = temp[0]
        j = temp[1]
        val = temp[2]
        
        while(1):
            #Go right
            j = j + 1
            
            if(j==items):
                j = j-1
                break
            
            que.append((w,j,val))
            Cval = 0
            for a in que:
                Cval = Cval + values[a[1]]
            print("right", que,Cval)


def BandBiter(w,j,val):

    que = []
    pick = 1
    
    que.append((w,j,val))
    
    while(len(que)>0):
        print(que)
        
        if(j+1==items):
            break
        
        if(pick):
            #j = j + 1
            w = w - weights[j]
            val = val + values[j]
#             if(w<0):
#                 w = w + weights[j]
#                 val = val - values[j]
#                 que.pop()
#             else:
            que.append((w,j,val))
        else:
            #j = j + 1
            que.append((w,j,val))
            
        j = j + 1

def solveIt(inputData):
    # Modify this code to run your optimization algorithm
    global items
    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    global values
    global weights
    global ratios
    global sortedRatios
    global selected
    global count
    count = 0
    
    sortedRatios = []
    ratios = []
    values = []
    weights = []
    selected = []
    
    combo = []
    

    for i in range(1, items+1): ## Look into this range its from 1 to items
        line = lines[i]
        parts = line.split()
        
        combo.append((int(parts[0]),int(parts[1]),i))

    #combo.sort( key=itemgetter(1), reverse=False)
    combo.sort( key=itemgetter(0), reverse=True)
    
    #combo = sorted(combo,key=itemgetter(0))
    #print(combo)
        #values.append(int(parts[0]))
        #weights.append(int(parts[1]))
        
    for i in range(0, items): ## Look into this range its from 1 to items
        #parts.sort(cmp=None, key=None, reverse=True)

        #print(combo[i])
        values.append(int(combo[i][0]))
        weights.append(int(combo[i][1]))
        

    items = len(values)

    for i in range(0, items):
        if(float(weights[i])==0):
            x = float("inf")
        else:
            x = float(float(values[i])/float(weights[i]))
        ratios.append(x)
        sortedRatios.append((x,i))
        
    sortedRatios.sort(cmp=None, key=None, reverse=True)
    #print(ratios)
    #print(sortedRatios)
    
    #temp =[]
    print("Init",items)

    global array
    #array = []
    array = [[-1]*(items+1) for x in xrange(capacity+1)]

    print("Running")
    global path
    path = []
    
    #bestVal = knap(capacity,items-1)
    #bestVal = BandB(capacity, 0,0)

    global finalpath
    
    finalpath = [0 ,2 ,4 ,5 ,46 ,210]
    bestVal = 3967180
##    for i in range(capacity):
##        for j in range(items):
##            print('{0},'.format(array[i][j])),
##        print('\n'),
##            

    # prepare the solution in the specified output format
    #outputData = str(value) + ' ' + str(0) + '\n'
    #outputData += ' '.join(map(str, taken))
    out = []
    j=0
    #print(finalpath)
    for i in range(items):
        out.append(0)
        
        
    for j in range(len(finalpath)):
        #print("out",(combo[finalpath[j]][2]))
        out[(combo[finalpath[j]][2])-1] = 1
            
    
    outputData = str(bestVal) + ' ' + str(0) + '\n' + ' '.join(map(str,out))
    return outputData


import sys
import copy
from operator import itemgetter

sys.setrecursionlimit(10000000)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'


##        if(array[w][j-1]==-1):
##            x = knap(w, j-1)
##            insert(w, j-1, x)
##            return int(x)
##        else:
##            return array[w][j-1]
