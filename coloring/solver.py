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
    
    
    ##--------------------------------Tools solutions-----------------
    print(nodeCount,edgeCount)
    solver = pywrapcp.Solver('kick colourer')
    
    max_num_colors = 95

    # declare variables
    colors = [solver.IntVar(0,max_num_colors, 'x%i' % i) for i in range(nodeCount)]
    
    #print(color)
    
    ##Set up contraints
    solver.Add(colors[indexedCount[0][1]] == 0) #make most connected node 0
    for e in edges:
        solver.Add(colors[e[0]] != colors[e[1]])
    
    solution = solver.Assignment()
    solution.Add([colors[i] for i in range(nodeCount)])
    
    collector = solver.FirstSolutionCollector(solution)
    #collector = solver.AllSolutionCollector(solution)
    
    solver.Solve(solver.Phase([colors[i] for i in range(nodeCount)],solver.INT_VAR_SIMPLE, solver.ASSIGN_MIN_VALUE),[collector])
    
    num_solutions = collector.SolutionCount()
    print "num_solutions: ", num_solutions
    if num_solutions > 0:
        for s in range(num_solutions):
            colorval = [collector.Value(s, colors[i]) for i in range(nodeCount)]
            print "color:", colorval
    
    solution = colorval
    outputData = 0
    ##----------------------------------------------------------------
    
    #solution = range(0, nodeCount)

    # prepare the solution in the specified output format
    outputData = str(max(solution)+1) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, solution))

    return outputData


import sys
import copy
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

