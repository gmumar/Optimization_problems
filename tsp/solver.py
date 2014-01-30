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
    
    
def pickLargestEdge_old(list,n):
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
    r_list.append(startV)
    r_list.append(endV)

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
            if mlist[i] == mlist[j]:
                pass
            else:
                #mlist = swap(mlist,[a,b])   
                
                temp = mlist[i]
                mlist[i] = mlist[j]
                mlist[j] = temp
                
                l_len = getLen(mlist)
                
                if(l_len<minLen):
                    listOrig = copy.copy(mlist)
                    #break
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
                
                temp = mlist[i]
                mlist[i] = mlist[j]
                mlist[j] = temp
                
                l_len = getLen(mlist)
                
                if(l_len<minLen):
                    listOrig = copy.copy(mlist)
                    break
                    #print("kep",getLen(mlist))
                else:
                    mlist = copy.copy(listOrig)
                
    return listOrig
    #print("final",getLen(mlist))
            
def switchOpt2(mlist):
    
    minLen = getLen(mlist)
    listOrig = copy.copy(mlist)
    
    #print(getLen(mlist))

    for a in mlist:
        nei = getNeighboursFromGrid(a,gridOrig)
        c = closest(a,nei)
        update(mlist,[a,c])
        
        for d in mlist:
            for b in mlist:
                #print(a,b)
                if d == b or d == a or d == c or b == a or b == c:
                    pass
                else:
                    mlist = swap(mlist,[d,b])   
                    l_len = getLen(mlist)
                    
                    if(l_len<minLen):
                        listOrig = copy.copy(mlist)
                        break
                        #print("kep",getLen(mlist))
                    else:
                        mlist = copy.copy(listOrig)
                
    return listOrig
    #print("final",getLen(mlist))

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
    devisor = 10000 #Controls size of blocks
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
    curPoint = 0
    tested.append(curPoint)
    
    #print(int((points[50][0]-smallest[0])/devisor) ,int((points[50][1]-smallest[1])/devisor))
    #for l in range(nodeCount-1):
    for l in range(0):
        
        solution.append(curPoint)
        for i in range(len(points)-1):
            neighbours = []
            getNeighbours(curPoint,neighbours)
            #print(i ,"Printing from main",neighbours,curPoint)
            connection = connect(curPoint,neighbours)
            curPoint = connection[1]
            #print curPoint
            solution.append(curPoint)
            #print "Solution",solution

        #print("before",solution)
        
        for k in range(10):
            for j in range(10):
                solution = switchOpt(solution)
        
        #print("here",solution)
        
        curLen = getLen(solution)
        
        if(curLen<minl):
            minl = curLen
            best = copy.copy(solution)
            #print(curLen,best)
        
        while(curPoint in tested):
            curPoint = random.randint(0,nodeCount-1)
            #curPoint = solution[-1]
        print(curLen , curPoint)
        
        tested.append(curPoint)
        solution = []
        grid =  copy.deepcopy(gridOrig)

    #solution = copy.copy(best)
        #rand = random.randint(0,nodeCount-2)
        #pickedVertex1 = [solution[rand], solution[rand+1]]
         
        #pickedVertex1 = pickLargestEdge(solution,1)
        #solution = twoOpt(solution, pickedVertex1)
    
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
    
    print(nodeCount)
    
    solution = [219, 218, 220, 221, 222, 224, 223, 217, 216, 215, 214, 213, 212, 211, 210, 209, 205, 206, 207, 208, 203, 204, 202, 201, 200, 199, 198, 197, 196, 195, 194, 184, 185, 183, 182, 186, 188, 187, 540, 538, 539, 537, 536, 535, 534, 487, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 475, 567, 566, 565, 564, 563, 562, 561, 560, 559, 558, 557, 556, 554, 553, 552, 101, 551, 550, 549, 548, 545, 546, 547, 544, 543, 541, 542, 107, 110, 111, 109, 108, 173, 174, 172, 175, 176, 177, 178, 179, 181, 180, 169, 171, 170, 168, 162, 163, 167, 166, 164, 165, 154, 153, 147, 148, 152, 149, 150, 151, 141, 140, 139, 138, 137, 129, 130, 131, 132, 133, 134, 135, 136, 144, 143, 142, 146, 145, 158, 157, 159, 156, 155, 160, 161, 113, 112, 114, 115, 116, 128, 127, 126, 125, 124, 69, 70, 68, 67, 66, 65, 72, 71, 123, 122, 121, 120, 119, 118, 117, 106, 105, 104, 103, 102, 100, 99, 98, 96, 95, 97, 94, 89, 88, 78, 77, 74, 73, 75, 76, 64, 63, 62, 79, 80, 81, 61, 60, 59, 58, 57, 82, 83, 56, 55, 53, 54, 52, 50, 51, 84, 85, 86, 87, 90, 93, 92, 91, 555, 45, 46, 47, 48, 49, 43, 44, 42, 39, 41, 40,38, 37, 36, 35, 34, 33, 32, 30, 31, 29, 28, 27, 26, 25, 24, 21, 22, 23, 12, 13, 14, 15, 16, 11, 10, 9, 7, 8, 17, 18, 19, 20, 568, 569, 570, 474, 473, 472, 494, 495, 471, 470, 469, 468, 467, 466, 571, 573, 572, 6, 5, 0, 4, 1, 2, 3, 437, 438, 436, 435, 434, 433, 432, 430, 429, 428, 427, 426, 425, 424, 423, 422, 421, 420, 419, 418, 417, 413, 414, 416, 415, 351, 352, 353, 354, 355, 402, 403, 401, 360, 359, 361, 362, 363, 364, 346, 345, 347, 348, 350, 349, 358, 357, 356, 412, 411, 410, 384, 383, 385, 409, 408, 407, 406, 405, 404, 400, 399, 398, 397, 394, 393, 391, 392, 390, 389, 388, 387, 386, 382, 431, 381, 380, 379, 378, 377, 376, 375, 395, 396, 371, 372, 373, 374, 315, 314, 316, 313, 312, 451, 311, 310, 309, 308, 505, 504, 503, 502, 498, 501, 500, 499, 452, 453, 440, 441, 450, 449, 442, 446, 448, 447, 445, 444, 443, 439, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 496, 497, 519, 518, 520, 517, 516, 515, 514, 522, 521, 523, 526, 525, 524, 493, 492, 491, 490, 529, 528, 527, 512, 513, 511, 510, 509, 506, 507, 508, 302, 301, 303, 304, 307, 305, 306, 318, 317, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 366, 367, 370, 369, 368, 365, 342, 343, 344, 341, 340, 330, 331, 332, 333, 339, 338, 337, 336, 335, 334, 283, 284, 285, 286, 287, 280, 281, 282, 279, 278, 277, 276, 288, 289, 290, 275, 274, 273, 272, 271, 267, 268, 269, 270, 293, 292, 291, 294, 295, 296, 297, 298, 266, 265, 264, 263, 262, 261, 260, 259, 258, 299, 300, 257, 256, 255, 253, 254, 252, 251, 250, 249, 248, 241, 242, 243, 244, 245, 247, 246, 238, 239, 240, 237, 236, 235, 234, 232, 233, 530, 531, 532, 489, 488, 533, 231, 230, 229, 228, 227, 189, 225, 226, 190, 191, 192, 193]
    
    
    
    
    
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

