#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def length(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def endPoints():
    
    global largest
    global smallest
    
    largeX = float(points[0][0])
    smallX = float(points[0][0])
    largeY = float(points[0][1])
    smallY = float(points[0][1])
    
    for i in range(nodeCount):
        if(points[i][0]>largeX):
            largeX = float(points[i][0])
        
        if(points[i][1]>largeY):
            largeY = float(points[i][1])
        
        if(points[i][0]<smallX):
            smallX = float(points[i][0])
        
        if(points[i][1]<smallY):
            smallY = float(points[i][1])
    
    largest = (largeX,largeY)
    smallest = (smallX,smallY)
    
def assignToGrid():
    global devisor
    global grid
    for i in range(nodeCount):
        #print(points[i])
        # grid[x,y]
        grid[int((points[i][0]-abs(smallest[0]))/devisor)][int((points[i][1]-abs(smallest[1]))/devisor)] = grid[int((points[i][0]-abs(smallest[0]))/devisor)][int((points[i][1]-abs(smallest[1]))/devisor)] +( i,)
        #print(grid[int((points[i][0]-smallest[0])/devisor)][int((points[i][1]-smallest[1])/devisor)])

def assignFromList(list):
    global devisor
    global grid
    for i in range(nodeCount):
        # grid[x,y]
        grid[int((list[i][0]-abs(smallest[0]))/devisor)][int((list[i][1]-abs(smallest[1]))/devisor)] = grid[int((list[i][0]-abs(smallest[0]))/devisor)][int((list[i][1]-abs(smallest[1]))/devisor)] +( i,)


def checkRow(start,end,list,grid):
    # Go through the row and append all points to the list
    #global grid
    global countY
    global countX

    #print("CheckRow", start, end,countY)
    
    col = start[1]
    rowStart = start[0]
    rowEnd = end[0]
    
    if(col >= countY or col < 0):
        #print ("killed")
        return

    for i in range (rowStart,rowEnd+1):
        #print("i col",i,col)
        if(i<0 or i>=countX):
            pass
        else:
            for j in range(len(grid[i][col])):
                if(grid[i][col][j] not in list):
                    list.append(grid[i][col][j])
                #print("appended")
    
def checkCol(start,end,list,grid):
    # Go through the col and append all points to the list
    #global grid
    global countY
    global countX

    #print("CheckCol", start, end,countX)
    
    row = start[0]
    colStart = start[1]
    colEnd = end[1]
    
    if(row >= countX or row < 0):
        return

    for i in range (colStart,colEnd+1):
        #print("Row i",row,i)
        if(i<0 or i>=countY):
            pass
        else:
            for j in range(len(grid[row][i])):
                if(grid[row][i][j] not in list):
                    list.append(grid[row][i][j])
                #print("appended")

def getNeighboursFromGrid(index,lgrid):
    global countY
    global points
    global devisor
    
    list = []
    # Append the neighbours to the list    
    pointGridX = int((points[index][0]-abs(smallest[0]))/devisor)
    pointGridY = int((points[index][1]-abs(smallest[1]))/devisor)
    
    #print("after",points[index],pointGridX,pointGridY,lgrid[pointGridX][pointGridY],index)
    
    #print(lgrid)
    
    # Check block itself
    for i in range(len(lgrid[pointGridX][pointGridY])):

        if (lgrid[pointGridX][pointGridY][i] == index):
            pass
        else:
            list.append(lgrid[pointGridX][pointGridY][i])
            
    
    level = 1
    
    #print(index, pointGridX, pointGridY, list, level)
    
    while(len(list)<4):
        # (x,y)
        topLeft = (pointGridX - level, pointGridY + level)
        topRight  = (pointGridX + level, pointGridY + level)
        bottomLeft  = (pointGridX - level, pointGridY - level)
        bottomRight  = (pointGridX + level, pointGridY - level)
        
        #print(topLeft,topRight,bottomLeft,bottomRight)
        
        checkRow(topLeft,topRight,list,lgrid)
        checkRow(bottomLeft,bottomRight,list,lgrid)
        checkCol(bottomLeft,topLeft,list,lgrid)
        checkCol(bottomRight,topRight,list,lgrid)
        
        level = level + 1
        
        if(level>max(countY,countX)*2):
            break
        #print(level)
    
    return list


def getNeighbours(index,list):
    global countY
    global points
    global grid
    global devisor
    # Append the neighbours to the list    
    pointGridX = int((points[index][0]-abs(smallest[0]))/devisor)
    pointGridY = int((points[index][1]-abs(smallest[1]))/devisor)
    
    #print "here",grid[pointGridX][pointGridY],index
    newTuple = ()
    
    for i in range(len(grid[pointGridX][pointGridY])):
        num = grid[pointGridX][pointGridY][i]

        if(num==index):
            pass
        else:
            newTuple = newTuple + (num,)
            
    #print ("newTuple",newTuple, grid[pointGridX][pointGridY],index)
    grid[pointGridX][pointGridY] = copy.copy(newTuple)
    #print("after",points[index],pointGridX,pointGridY,grid[pointGridX][pointGridY],index)
    
    #print(grid)
    
    # Check block itself
    for i in range(len(grid[pointGridX][pointGridY])):
        if (grid[pointGridX][pointGridY][i] == index):
            pass
        else:
            list.append(grid[pointGridX][pointGridY][i])
            
    
    level = 1
    
    #print(index, pointGridX, pointGridY, list, level)
    
    while(len(list)<10 ): #or level < max(countY,countX)
        # (x,y)
        topLeft = (pointGridX - level, pointGridY + level)
        topRight  = (pointGridX + level, pointGridY + level)
        bottomLeft  = (pointGridX - level, pointGridY - level)
        bottomRight  = (pointGridX + level, pointGridY - level)
        
        #print(topLeft,topRight,bottomLeft,bottomRight)
        
        checkRow(topLeft,topRight,list,grid)
        checkRow(bottomLeft,bottomRight,list,grid)
        checkCol(bottomLeft,topLeft,list,grid)
        checkCol(bottomRight,topRight,list,grid)
        
        level = level + 1
        
        if(level>max(countY,countX)*2):
            break
        #print(level)

def connect(point,list):
    # connects point to the nearest vertex in the list
    
    #print(point,list)
    
    global points
    min = float("inf")
    minIndex = point
    
    for i in range(len(list)):
        adj = list[i]
        #print point,adj,i
        l_len = length(points[point],points[adj])
        
        if(l_len<min):
            min = l_len 
            minIndex = adj
        
    return [point,minIndex]
    
def semiConnect(point,list):
    # connects point to the nearest vertex in the list
    
    #print(point,list)
    
    global points
    min = float("inf")
    
    i = random.randint(0,len(list)-1)
    adj = list[i]
    minIndex = adj
        
    return [point,minIndex]
    
    
def pickLargestEdgeO(list,n):
    # Pick the largest edge and return the vertexes connected to it

    l_list = copy.copy(list)
    startV = 0
    endV = 0
    l_max = 0
    
    r_list = []
    
    for j in range(n):
        
        for i in range(len(l_list)):
            if(i+1>=len(l_list)):
                break
            l_len = length(points[int(l_list[i])],points[int(l_list[i+1])])
            if( l_len > l_max ):
                l_max = l_len
                startV = l_list[i]
                endV = l_list[i+1]
        
        l_list.remove(startV)
        l_list.remove(endV)
        l_max = 0
    
    #print(startV,endV)
        r_list.append((startV,endV))

    return r_list

def pickLargestEdge(list,n):
    # Pick the largest edge and return the vertexes connected to it

    l_list = copy.copy(list)
    startV = 0
    endV = 0
    l_max = 0
    
    r_list = []
    
    for j in range(n):
        for i in range(len(l_list)):
            l_len = length(points[int(l_list[i])],points[int(l_list[fix(i+1)])])
            if( l_len > l_max ):
                l_max = l_len
                startV = l_list[i]
                endV = l_list[fix(i+1)]
        
        l_list.remove(startV)
        l_list.remove(endV)
        l_max = 0
    
    #print(startV,endV)
    r_list.append(startV)
    r_list.append(endV)

    return r_list

def pickLargestEdgeIndex(l_list):
    # Pick the largest edge and return the vertexes connected to it

    #l_list = copy.copy(list)
    startV = 0
    endV = 0
    l_max = 0

    for i in range(len(l_list)):
        l_len = length(points[int(l_list[i])],points[int(l_list[fix(i+1)])])
        if( l_len > l_max ):
            l_max = l_len
            startV = i
            endV = fix(i+1)

    l_max = 0
    

    return [startV,endV]

def getLen(list):
    obj = length(points[list[-1]], points[list[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[list[index]], points[list[index+1]])
            
    return obj


def twoOpt(list,connection):
    # List is gona be solutions
    # connection is the one connection i know i am gona break
    
    # Go through the whole list breaking connections and see if any give better solution

    #print("Connection",connection)
    minLen = float("inf")
    listOrig = copy.deepcopy(list) 
    lenOrig = getLen(list)
    #print("Orig",lenOrig)
    
    r_list = []
    i2 = 0
    
    for k in range(6):
        for i in range(len(list)):
            
            if(i>=len(list)-1):
                i2 = 0
            else:
                i2 = i + 1
    
            if(connection[0] == list[i] or connection[0] == list[i2] or connection[1] == list[i] or connection[1] == list[i2]):
                pass
            else:
                # con[0] -> new[0]
                update(list,[connection[0],list[i]])
                update(list,[connection[1],list[i2]])
                newLen = getLen(list)
                
                if(newLen<lenOrig and newLen<minLen):
                    minLen = newLen
                    print("1",minLen)
                    r_list = copy.copy(list)
                else:
                    if(r_list == []):
                        list = copy.copy(listOrig)
                    else:
                        list = copy.copy(r_list)
                
           
                # con[0] -> new[1]        
                update(list,[connection[0],list[i2]])
                update(list,[connection[1],list[i]])
                newLen = getLen(list)
                
                if(newLen<lenOrig and newLen<minLen):
                    minLen = newLen
                    print("2",minLen)
                    r_list = copy.copy(list)
                else:
                    if(r_list == []):
                        list = copy.copy(listOrig)
                    else:
                        list = copy.copy(r_list)
    
    if(r_list == []):
        return list
    else:
        return r_list


def nodeConnectingTo(list,node):
    
    for i in range(len(list)):
        if(list[i]==node):
            if(i-1<0):
                return list[-1]
            else:
                return list[i-1]
    
def closest(node,list):
    if len(list) > 0:
        min = length(points[node],points[list[0]])
        index = list[0]
        
        for i in range(1,len(list)):
            l_len = length(points[node],points[list[i]])
            if(l_len<min):
                min = l_len
                index = list[i]
                
        return index
    else:
        return -1

def forceConnect(list,edge):
    #forces the edge to exist
    print list,edge
    for i in range(len(list)):
        
        if list[i] == edge[0]:
            if(i+1>=len(list)):
                list[0] = edge[1]
            else:
                list[i+1] = edge[1]
            break
    
    print "after",list,edge
    return list

def forceConnectOld(list,edge):
    #forces the edge to exist
    print list,edge
    for i in range(len(list)):
        
        if list[i] == edge[0]:
            if(i+1>=len(list)):
                list[0] = edge[1]
            else:
                list[i+1] = edge[1]
            break
        
        elif list[i] == edge[1]:
            if(i+1>len(list)):
                list[0] = edge[0]
            else:
                list[i+1] = edge[0]
            break 
    
    print "after",list,edge
    return list

def pred(list,node):
    for i in range(len(list)):
        if(list[i]==node):
            if(i-1<0):
                return list[-1]
            else:
                return list[i-1]
            
def succ(list,node):
    for i in range(len(list)):
        if(list[i]==node):
            if(i+1>=nodeCount):
                return list[0]
            else:
                return list[i+1]
      
def fix(k):
    
    
    if(k<0):
        return nodeCount-1
    
    if(k>=nodeCount):
        return 0
    
    return k
          
def feasibleKoptMove(mlist,t1,t2,t3,t4):
    # t1 -> t4
    # t2 -> t3
    # check feaiility by going through all nodes and adding every unique to a list if the list len is equal to points len then its feasible
        
    for i in range(len(mlist)):
        
        if(mlist[i]==t1):
            if(mlist[fix(i-1)]==t2):
                mlist[fix(i-1)]=t4
            elif(mlist[fix(i+1)]==t2):
                mlist[fix(i+1)]=t4
        
        if(mlist[i]==t3):
            if(mlist[fix(i-1)]==t4):
                mlist[fix(i-1)]=t2
            elif(mlist[fix(i+1)]==t4):
                mlist[fix(i+1)]=t2
    
    check = []
    for i in range(len(mlist)):
        if(mlist[i] not in check):
            check.append(mlist[i])
    
    if(len(check) == len(points)):
        #print getLen(mlist)
        return mlist
    else:
        print("<----LIST MESSSEDD--->")
        return False
    
    #print("after",mlist)

def kOpt(list,connection):
    
    global gridOrig
    global points
    
    links = []
    
    t1 = connection[0]
    t2 = connection[1]
    
    links.append(t2)
    
    t3 = connection[0]
    t4 = connection[1]
    
    gain = []
    gain.append(0)
    gain.append(0)
    gain.append(0)
    
    
    
    for t2 in [pred(list,t1),succ(list,t1)]:
        gain[0] = length(points[t1],points[t2])
        nei = getNeighboursFromGrid(t2,gridOrig)

        for t3 in nei:
            
            # Checking to see if the new length is shorter then the original edge were gona break
            gain[1] = gain[0] - length(points[t2],points[t3])
            
            if( t3 != pred(list,t2) and t3 != succ(list,t2) and gain[1]>0):
                
                for t4 in [pred(list,t3),succ(list,t3)]:
                    if(t3 == None or t4 == None or t4==t1):
                        break
                    gain[2] = gain[1] + length(points[t3],points[t4])
                    gainTotal = gain[2] - length(points[t4],points[t1])
                    
                    listOrig = copy.deepcopy(list)
                    
                    if(feasibleKoptMove(copy.copy(list),t1,t2,t3,t4) and (gainTotal > 0)):
                        print(t1,t2,t3,t4,gainTotal)
                        list = feasibleKoptMove(list,t1,t2,t3,t4)
                        if list == False:
                            list = copy.copy(listOrig)
                        else:    
                            return list

    return list

   
def update(list,connection):
    # Takes an array and makes the new connection, will update list
    
    # Takes the solution array and swaps the connection
    #print(list)
    first = 0
    second = 0
    for i in range(len(list)):
        if(list[i]==connection[0]):
            first = i
        
        elif(list[i]==connection[1]):
            second = i
    # Swap
    l_max = max(first,second) + 1
    if(l_max>=nodeCount):
        l_max = 0
    l_min = min(first,second)
    temp = list[l_max]

    list[l_max] =  list[l_min]
    list[l_min] = temp
    
    #print("after",list)

def swap(list,point):
    
    #print(point,list)
    for i in range(len(list)):
        if list[i] == point[0]:
            first = i
        
        if list[i] == point[1]:
            second =i
            
    temp = list[first]
    list[first] = list[second]
    list[second] = temp
    
    #print("after Swap",list)
    
    return list
    

def switchOpt(mlist):
    
    minLen = getLen(mlist)
    listOrig = copy.copy(mlist)
    
    #print(getLen(mlist))
    ran = len(mlist)
    
    for i in xrange(ran):
        for j in xrange(ran):
            #print(a,b)
            if i == j:
                pass
            else:
                #mlist = swap(mlist,[a,b])   
                
                temp = mlist[i]
                mlist[i] = mlist[j]
                mlist[j] = temp
                a = min(i,j) + 1
                b = max(i,j) - 1
                while(a<b):
                    temp = mlist[a]
                    mlist[a] = mlist[b]
                    mlist[b] = temp
                    a = a + 1
                    b = b - 1
                
                l_len = getLen(mlist)
                
                if(l_len<minLen):
                    listOrig = copy.copy(mlist)
                    break
                    #print("kep",getLen(mlist))
                else:
                    mlist = copy.copy(listOrig)
                
    return listOrig
    #print("final",getLen(mlist))


def switchOpt1(mlist):
    
    minLen = getLen(mlist)
    listOrig = copy.copy(mlist)
    
    #print(getLen(mlist))
    
    ran = len(mlist)
    
    largest = pickLargestEdgeIndex(mlist);
    
    for i in [largest[0],largest[1]]:
        for j in xrange(ran):
            #print(a,b)
            if mlist[i] == mlist[j]:
                pass
            else:
                #mlist = swap(mlist,[a,b])   
                
                #print(mlist[i],mlist[j],mlist,"b")
                
                temp = mlist[i]
                mlist[i] = mlist[j]
                mlist[j] = temp
                a = min(i,j) + 1
                b = max(i,j) - 1
                while(a<b):
                    temp = mlist[a]
                    mlist[a] = mlist[b]
                    mlist[b] = temp
                    a = a + 1
                    b = b - 1
                
                #print(i,j,mlist)
                
                l_len = getLen(mlist)
                
                if(l_len<minLen):
                    listOrig = copy.copy(mlist)
                    #break
                    #print("kep",getLen(mlist))
                else:
                    mlist = copy.copy(listOrig)
                
    return listOrig
    #print("final",getLen(mlist))

def Metro(mlist,t):
    
    minLen = getLen(mlist)
    #print("<-Orig->",minLen)
    listOrig = copy.copy(mlist)
    
    i = random.randint(0,nodeCount-1)
    j = i
    while i == j:
        j = random.randint(0,nodeCount-1)
    
    # Swap the nodes flipping all the ones in between    
    a = min(i,j)
    b = max(i,j)
    while(a<b):
        temp = mlist[a]
        mlist[a] = mlist[b]
        mlist[b] = temp
        a = a + 1
        b = b - 1
    
    l_len = getLen(mlist)
    
    # listOrig -> dont accept neighbour
    # mlist -> accept neighbour
    
    if(l_len<=minLen):
        #print("<----Better--->",getLen(mlist))
        return mlist
    else:
        prob = math.exp(-(l_len-minLen)/t)
        rnd = random.random()
        
        if (rnd<prob):
            #print("Prob - Selected",getLen(mlist))
            return mlist
        else:
            return listOrig
tabu = []
def tabuMetro(mlist,t):
    
    global tabu 
    count = 0
   
    while(1): 
        minLen = getLen(mlist)
        #print("<-Orig->",minLen)
        
        listOrig = copy.copy(mlist)
        
        i = random.randint(0,nodeCount-1)
        j = i
        while i == j:
            j = random.randint(0,nodeCount-1)
        
        # Swap the nodes flipping all the ones in between    
        a = min(i,j)
        b = max(i,j)
        while(a<b):
            temp = mlist[a]
            mlist[a] = mlist[b]
            mlist[b] = temp
            a = a + 1
            b = b - 1
        
        l_len = getLen(mlist)
        
        # listOrig -> dont accept neighbour
        # mlist -> accept neighbour
        
        if (i,j) in tabu:
            count = count + 1
            if count > (nodeCount):
                count = 0
                tabu = []
                print("reset")
            continue
        else:
            tabu.append((i,j))
            break
    
    if(l_len<=minLen):
        #print("<----Better--->",getLen(mlist))
        return mlist
    else:
        prob = math.exp(-(l_len-minLen)/t)
        rnd = random.random()
        
        if (rnd<prob):
            #print("Prob - Selected",getLen(mlist))
            return mlist
        else:
            return listOrig

def zeroOpt(mlist):
    
    # Pick up random customer
    rand = random.randint(0,len(mlist)-1)
    customer = mlist[rand]
    
    #print mlist
    
    # Get original length
    minLen = getLen(mlist)
    morig = copy.copy(mlist)
    
    # Remove the customer from original position
    mlist.remove(customer)
    removed = copy.copy(mlist)
    
    best = []
    # Replace customer at all places and select best
    for i in range(0,len(mlist)):
        #if(customer not in mlist):
        mlist.insert(i,customer)
        newLen = getLen(mlist)
        
        #print(i,customer,mlist)
        
        if(newLen<minLen):
            minLen = newLen
            best = copy.copy(mlist)
            break
        
        mlist = copy.copy(removed)
    

    if best == []:
        return morig
    else:
        return best
    
        
    
    
def simAnneal(mlist,N):
    temp = 55
    best = copy.copy(mlist)
    
    mintemp = getLen(mlist)

    count = 0
    #for j in range(N):
    while(1):
        
        for k in range(160):
            mlist = zeroOpt(mlist)
           
        for k in range(800):
            count = count + 1 
            
            mlist = Metro(mlist,temp)
            newtemp = getLen(mlist)
            #print(temp,newtemp,mintemp)
            
            if(newtemp<mintemp):
                count = 0
                mintemp = newtemp
                #print(mintemp,temp)
                #print(mlist)
                print(mintemp,temp)
                best = copy.copy(mlist)
        
        #temp = temp * 0.9999
        if(count>100000):
            count = 0
            print(best)
            print(getLen(best))
            
            #for i in range(3):
            #swap(mlist,[ random.randint(0,nodeCount-1), random.randint(0,nodeCount-1)])
            temp = temp * 1.001
            if temp > 250:
                temp = 250
            if temp < 1:
                temp = 15
            print temp
            
        temp = temp * 0.99991    
    return best

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    global nodeCount
    nodeCount = int(lines[0])

    global points
    points = []
    #points (x,y)
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append((float(parts[0]), float(parts[1])))
    
    # init
    # Get the endPoints of the the grid
    global largest
    global smallest
    
    endPoints()
    
    print (largest,smallest)
    
    # Build the Grid with grid size of 0.25x0.25
    global devisor
    devisor = 100000 #Controls size of blocks
    global grid
    global countX
    global countY
    countX = int(math.floor((largest[0]-abs(smallest[0]))/devisor)) + 1
    countY = int(math.floor((largest[1]-abs(smallest[1]))/devisor)) + 1
    grid = [[() for i in range(countY)] for j in range(countX)]
    
    print("gridSize:",countX,countY)
    
    assignToGrid()
    
    global gridOrig
    gridOrig = copy.deepcopy(grid)
    
    #print(grid)
    #print("first",gridOrig)
    
    solution = []
    best = []
    minl = float("inf")
    #solution.append(0)
    tested = []
    curPoint = random.randint(0,nodeCount-1)
    #curPoint = 4
    tested.append(curPoint)
    
    
    
#    for l in range(nodeCount-1):
    solution.append(curPoint)
    for i in range(len(points)-1):
        neighbours = []
        getNeighbours(curPoint,neighbours)
        connection = connect(curPoint,neighbours)
        curPoint = connection[1]
        solution.append(curPoint)
 
    #Gives initial solution
     
    #for i in range(10):
    print("main",getLen(solution))
    #for k in range(7000):
    #    solution = zeroOpt(solution)
    #    print getLen(solution)
    solution = simAnneal(solution,10000)
     
#         curLen = getLen(solution)
#            
#         if(curLen<minl):
#             minl = curLen
#             best = copy.copy(solution)
#             print(curLen,best)
#            
#         while(curPoint in tested):
#             curPoint = random.randint(0,nodeCount-1)
#             #curPoint = solution[-1]
#         print(curLen , curPoint)
#            
#         tested.append(curPoint)
#         solution = []
#         grid =  copy.deepcopy(gridOrig)
     
     
#    solution = copy.copy(best)
    
    
  #=============================================================================
  #   for l in range(nodeCount-1):
  #         
  #       solution.append(curPoint)
  #       for i in range(len(points)-1):
  #           neighbours = []
  #           getNeighbours(curPoint,neighbours)
  #           connection = connect(curPoint,neighbours)
  #           curPoint = connection[1]
  #           solution.append(curPoint)
  # 
  #       for k in range(10):
  #           for j in range(20):
  #               solution = switchOpt1(solution)
  #               #print(getLen(solution))
  #         
  #       curLen = getLen(solution)
  #         
  #       if(curLen<minl):
  #           minl = curLen
  #           best = copy.copy(solution)
  #           print(curLen,best)
  #         
  #       while(curPoint in tested):
  #           curPoint = random.randint(0,nodeCount-1)
  #           #curPoint = solution[-1]
  #       print(curLen , curPoint)
  #         
  #       tested.append(curPoint)
  #       solution = []
  #       grid =  copy.deepcopy(gridOrig)
  # 
  #   solution = copy.copy(best)
  #=============================================================================

    
    
    
    
    
    
    
    #===========================================================================
    # for j in range(1):
    #     nMax = 1
    #     for i in range(1):
    #         pickedVertex1 = pickLargestEdge(solution,nMax)
    #         nMax = nMax+1
    #         solution = kOpt(solution, pickedVertex1)
    #         
    #         #rand = random.randint(0,nodeCount-2)
    #         #pickedVertex1 = [solution[rand], solution[rand+1]]
    #         
    #         solution = kOpt(solution, pickedVertex1)
    #===========================================================================
    
    print(solution)
    
    
#===============================================================================
#     nthMax = 1
#      
#     for k in range(100):
#         pickedVertex1 = pickLargestEdge(solution,nthMax)
# #         nthMax = nthMax + 1
# #         if nthMax > nodeCount/2:
# #             nthMax = 1
#         print(getLen(solution))
#         solution = kOpt(solution, pickedVertex1)
#         print(solution)
#===============================================================================
    
#===============================================================================
#     #Optimization
#     nthMax = 1
#     hold = 0
#     for j in range(1000):
#          
#         pickedVertex1 = pickLargestEdge(solution,nthMax)
#         if(hold==pickedVertex1):
#             nthMax = nthMax + 1
#             if nthMax > nodeCount/2:
#                 nthMax = 1
#         hold = pickedVertex1
#         #print(pickedVertex1)
#         solution = twoOpt(solution, pickedVertex1)
#              
# #         rand = random.randint(0,nodeCount-2)
# #         pickedVertex1 = [solution[rand], solution[rand+1]]
# #         solution = twoOpt(solution, pickedVertex1)
#          
#         #print("len",getLen(solution))
#===============================================================================

    
    # calculate the length of the tour
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])

    # prepare the solution in the specified output format
    outputData = str(obj) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, solution))

    return outputData


import sys
import random
import copy

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)'

