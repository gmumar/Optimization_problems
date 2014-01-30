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


def check(colors,domain):
    global edges
    global nodeCount
    flag = 0
    
    count = 0
    node = indexedCount[count][1]
    i = 0
    while(1):
        print(i)
        i = i + 1
        
        adj = []
        #builds adjacency lists
        for e in edges:
            if(e[0] == node):
                adj.append(int(e[1]))
            if(e[1] == node):
                adj.append(int(e[0]))
      
        domainColor = 0
        for a in adj:
            if(int(colors[a]) == (colors[node])):
                #Infeasable
                #print("infeasable" , colors[node],domain[node])
                try:
                    colors[node] = int(domain[node][domainColor])
                except:
                    break
                #print(colors[node])
                
                if(domainColor + 1 > len(domain[node])):
                    domainColor = 0
                else:
                    domainColor = domainColor + 1
                
                continue
            else:
                #OK continue prune
                for a in adj:
                    try:
                        #pass
                        domain[a].remove(int(colors[node]))
                    except:
                        pass
        
        if(count + 1 >= nodeCount):
            if(flag == 0):
                count = 0
                flag = 1
            else:
                break
        else:
            count = count + 1
            node = indexedCount[count][1]
    
    return colors 
            
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
    domain = [[]] #maintains all possible values for a node
    colors = []
    
    #col = []
    #for i in range(nodeCount):
    #    col.append(i) #Colors initially in domain

    for i in range(nodeCount):
        colors.append(0) #initially all colors are 0
    
    #for i in range(nodeCount):
    #    domain.append(copy.copy(col))
        
    #domain.pop(0)
    
    #Pick the node with most edges first
    #count = 0
    #node = indexedCount[count][1] 
    
    #adj = []
    #maxChoice = 1
    #localColors = []
    
    for run in range(1):
        print("run",run)
        col = []
        domain = [[]]
        
        for i in range(nodeCount-run):
            col.append(int(i))

        
        for o in range(nodeCount):
            if(int(colors[o])==col[-1]):
                colors[o]=0
        
        for i in range(nodeCount):
            domain.append(copy.copy(col))
        
        domain.pop(0)

#===============================================================================
#         while(1):
#             adj = []
#             #builds adjacency lists
#             for e in edges:
#                 if(e[0] == node):
#                     adj.append(int(e[1]))
#                 if(e[1] == node):
#                     adj.append(int(e[0]))
#             
#             #constraint checking
#             domainColor = 0
#             localColors = []
#             
#             for aC in range(len(adj)):
#                 
#                 #Count local colors
#                 for k in range(len(adj)):
#                     if(colors[adj[k]] in localColors):
#                         pass
#                     else:
#                         localColors.append(colors[adj[k]])
#     
#                 maxChoice = len(localColors)
#                 
#                 if(int(colors[node]) == int(colors[adj[aC]])):
#                     #adj color matching: INFESABLE
#                     colors[node] = int(domain[node][domainColor])
#                     
#                     #if(domainColor + 1 > len(domain[node])):
#                     if(domainColor == maxChoice):
#                         domainColor = 0
#                     else:
#                         domainColor = domainColor + 1
#                     
#                     #aC = 0
#                     continue
#                 else:
#                     #adj nodes different so prune
#                     for a in adj:
#                         try:
#                             domain[a].remove(colors[node])
#                         except:
#                             pass
# 
#             
#             if(count + 1 == nodeCount):
#                 break
#             else:
#                 count = count + 1
#                 node = indexedCount[count][1] 
#===============================================================================
                    
        solution = check(colors,domain)
        #print(solution)
    
    #solution = range(0, nodeCount)

    # prepare the solution in the specified output format
    outputData = str(max(colors)+1) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, solution))

    return outputData


import sys
import copy

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

