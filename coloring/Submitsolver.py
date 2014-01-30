#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkBase(nodes):
    for n in nodes:
        #Check number of possible colors for each node
        if(len(n)==1):
            #If number of colors is one for all then 
            pass
        else:
            return 0
    return 1

def prune(nodes,c):
    pass

def reduce(nodes):
    for i in range(len(nodes)):
        nodes[i] = nodes[i] - 1
        if(nodes[i]<0):
            nodes[i] = 0


def check(colors):
#Looks at colors and checks if its feasible
#If it is then prunes the domain
#Else return number of node causing the infeasibility

    global edges
    global nodeCount
    global domain
    global adj
    flag = 0
    count = 0
    node = indexedCount[count][1]
    
    #print("check",node)
    
    while(1):
      
        for a in adj[node]:
            if(int(colors[int(a)]) == int(colors[node])):
                #Infeasable
                return node
            else:
                #OK continue prune             
                for a in adj[node]:
                    if(int(colors[node]) in domain[int(a)]):
                        domain[int(a)].remove(int(colors[node]))
                    else:
                        #print(domain[a],int(colors[node]))
                        pass
                    if(len(domain[int(a)])==1):
                        colors[int(a)] = int(domain[int(a)][0])
                #return -1
        
        #Iterator - to cycle through all nodes
        if(count + 1 >= nodeCount):
            if(flag == 0):
                count = 0
                flag = 1
            else:
                break
        else:
            count = count + 1
            node = indexedCount[count][1]
    
    return -1 

def setValue(colors,node):
    global domain
    global lvlMax
    global adj
    
    localColors = []
    maxChoice = 1
    flag = 0
    
    #print("set", node)
  
    for k in range(len(adj[node])):
        if(colors[int(adj[node][k])] in localColors):
            pass    
        else:
            localColors.append(int(colors[adj[node][k]]))
    
    maxChoice = max(localColors) +1
    #print(maxChoice,node,domain[node])

    for i in range(maxChoice):
        if(len(domain[node])>i):
            colors[node] = domain[node][i]
        else:
            for l in range(lvlMax):
                for a in adj[node]:
                    if(l == colors[int(a)]):
                        pass
                    else:
                        colors[node] = l
                        domain[node].append(l)
                        #print(domain[node][-1],colors)
                        break

#         for a in adj[node]:
#             if(colors[node] == colors[int(a)]):
#                 flag=0
#                 break
#             else:
#                 flag=1

        if(colors[node] in localColors):
            continue
        else:
            return

        if(flag==1):
            return
    
            
def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    global nodeCount
    nodeCount = int(firstLine[0])
    edgeCount = int(firstLine[1])

    global edges
    edges = []
    for i in range(1, edgeCount + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
        
    counts = []
    for i in range(nodeCount):
        counts.append(0)
    
    for e in edges:
        counts[e[0]] = counts[e[0]] + 1
        counts[e[1]] = counts[e[1]] + 1
         
    global indexedCount
    indexedCount = []
    for i in range(nodeCount):
        indexedCount.append((counts[i],i))
        
    indexedCount.sort(cmp=None, key=None, reverse=True)
    
    #print(indexedCount)
    
    global colors
    global domain
    global lvlMax
    domain = [[]] #maintains all possible values for a node
    colors = []
    
    global adj
    list = []
    adj = [[]]*nodeCount
    #builds adjacency lists
    for i in range(nodeCount):

        list = []
        for e in edges:
            if(int(e[0]) == i):
                list.append(int(e[1]))
            if(int(e[1]) == i):
                list.append(int(e[0]))
        
        adj[i] = copy.copy(list)
    
    #col = []
    #for i in range(nodeCount):
    #    col.append(i) #Colors initially in domain

    for i in range(nodeCount):
        colors.append(0) #initially all colors are 0
    
    #for i in range(nodeCount):
    #    domain.append(copy.copy(col))
        
    #domain.pop(0)
    
    #Pick the node with most edges first
    count = 0
    node = indexedCount[count][1] 
    
    #adj = []
    #maxChoice = 1
    #localColors = []
    initMax = 0
    flag1 = 0
    
    for run in range(10):
        
        col = []
        domain = [[]]
        
        if(flag1==0):
            for i in range(nodeCount-run):
                col.append(int(i))
        else:
            for i in range(initMax-run+1):
                col.append(int(i))
            

        lvlMax = int(col[-1])+1
        print("run",run,nodeCount,edgeCount)
        #print(col)
        for o in range(nodeCount):
            if(int(colors[o])==lvlMax):
                colors[o]=0
        
        #print(max(colors)+1,colors)
        
        for i in range(nodeCount):
            domain.append(copy.copy(col))
        
        domain.pop(0)

#----Quick run code------
        if(flag1==0):
            while(1):
                #constraint checking
                domainColor = 0        
                for aC in range(len(adj[node])):
                     
                    if(int(colors[node]) == int(colors[adj[node][aC]])):
                        #adj color matching: INFESABLE
                        colors[node] = int(domain[node][domainColor])
                         
                        if(domainColor + 1 > len(domain[node])):
                            domainColor = 0
                        else:
                            domainColor = domainColor + 1
                         
                        #aC = 0
                        continue
                    else:
                        #adj nodes different so prune
                        for a in adj[node]:
                            if(colors[node] in domain[a]):
                                domain[a].remove(colors[node])
                            else:
                                pass
                            
                        if(len(domain[int(a)])==1):
                            colors[int(a)] = int(domain[int(a)][0])
     
                 
                if(count + 1 == nodeCount):
                    break
                else:
                    count = count + 1
                    node = indexedCount[count][1] 

            print("quick",max(colors)+1)
        
#--------Optimizer Code---------------- 
        temp = 0
        holder = 0
        iter = 0
        x = 1000
        while(1):
            print("Iteration" , iter)
            temp = check(colors)
            
            if(holder==temp):
                iter = iter + 1
            else:
                iter = 0
                #x = 1000
            
            if(iter==x):
                colors[random.randint(0,len(colors)-1)] = int(random.randint(0,lvlMax))
                temp = check(colors)
                print("rand")
                x = x + 100
                iter = iter -1
            
            if(iter>=100):
                break
            holder = temp
            #print(temp)
            if(temp!=-1):
                #infeasiable
                #print("bf",colors,temp)
                temp = setValue(colors,temp)
                
                #print("af",colors)
            else:
                solution = copy.copy(colors)
                break
        
        #solution = colors
        if(flag1==0):
            initMax = max(colors)+1
            flag1 = 1
        print(max(solution)+1,solution)
    
    #solution = range(0, nodeCount)

    # prepare the solution in the specified output format
    outputData = str(max(solution)+1) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, solution))

    return outputData


import sys
import copy
import random
from constraint_solver import pywrapcp

if __name__ == '__main__':
    
    
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

