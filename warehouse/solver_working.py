#!/usr/bin/python
# -*- coding: utf-8 -*-

def cheapestWarehouse_dist(wlist,n):
    # Selects the nth cheapest warehouse by least avg distance cost whose capacity is greater than 0
    global avgDistanceToWarehouse
    n = n - 1
            
    return avgDistanceToWarehouse[n][1]
    
def cheapestWarehouse_fixed(wlist,n):
    # Selects the nth cheapest warehouse by fixed cost whose capacity is greater than 0
    
    global capacityRemaining
    
    lmin = float("inf")
    index = float("inf")
    
    seen = []
    
    for k in range(n):

        for i in xrange(len(wlist)):
            if(wlist[i][1]<lmin and capacityRemaining[i]>0 and i not in seen):
                lmin = wlist[i][1]
                index = i
                
        seen.append(index)
        lmin = float("inf")
            
    return index


def nearestCustomer(index):
    # Returns the nearest customer to a particular warehouse whose capacity is less then the remaining space at the warehouse
    global customerCount
    global capacityRemaining
    global solution
    
    lmin = float("inf")
    index_r = float("inf")
    
    for i in xrange(customerCount):
        if(customerCosts[i][index] < lmin and customerSizes[i] <= capacityRemaining[index] and i not in connected):
            lmin = customerCosts[i][index]
            index_r = i
    
    return index_r

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    parts = lines[0].split()
    global customerCount
    global warehouseCount
    warehouseCount = int(parts[0])
    customerCount = int(parts[1])

    global warehouses
    warehouses = []
    for i in range(1, warehouseCount+1):
        line = lines[i]
        parts = line.split()
        warehouses.append((int(parts[0]), float(parts[1])))
        # warehouse capacity, warehouse fixed cost

    global customerSizes
    global customerCosts
    
    customerSizes = []
    customerCosts = []

    lineIndex = warehouseCount+1
    for i in range(0, customerCount):
        customerSize = int(lines[lineIndex+2*i])
        customerCost = map(float, lines[lineIndex+2*i+1].split())
        customerSizes.append(customerSize)
        customerCosts.append(customerCost)
        # demand in customerSizes, transportation cost to n warehouse in customerCosts
        # customerSizes[n] returns demand of nth customer
        # customerCosts[n] returns a list of distances to mth warehouse
    
    global solution
    solution = [-1] * customerCount # initialization for the solution array
    global capacityRemaining
    capacityRemaining = [w[0] for w in warehouses] # Shows the  capacity remaining at n warehouse

    global connected
    connected = [] #shows all the customers connected to warehouses
    
    global avgDistanceToWarehouse
    avgDistanceToWarehouse = [0]*warehouseCount # Shows the avg distance to nth warehouse
    
    for i in range(customerCount):
        for k in range(warehouseCount):
            avgDistanceToWarehouse[k] = customerCosts[i][k] + avgDistanceToWarehouse[k]
    
    for k in range(warehouseCount):
        avgDistanceToWarehouse[k] = (avgDistanceToWarehouse[k] * warehouses[k][1]) / warehouseCount 
        
    for k in range(warehouseCount):
        avgDistanceToWarehouse[k] = (avgDistanceToWarehouse[k],k)
        
    avgDistanceToWarehouse.sort()
    
    valid = []
    
    for k in range(20):
        valid.append(avgDistanceToWarehouse[k][1])
    
    #------------------------INIT----------------------
    
    print(warehouseCount,customerCount)
    print valid
    #print(avgDistanceToWarehouse)
    #print("warehouses",warehouses)
    #print("customer Costs",customerCosts)
    #print("customer Sizes",customerSizes)
    #print ("cap remaining",capacityRemaining)


    count = 1
    while (-1 in solution):

        warehouseIndex = cheapestWarehouse_dist(warehouses,count)
        #print("Cheapest warehouse",warehouseIndex)
        
        while(capacityRemaining[warehouseIndex] > 0 and -1 in solution):
            customerIndex = nearestCustomer(warehouseIndex)
            
            #print("closest customer", customerIndex)
            
            
            if(customerIndex == float("inf")):
                count = count + 1
                if(count > warehouseCount):
                    count = 1
                break
            
            
            
            capacityRemaining[warehouseIndex] = capacityRemaining[warehouseIndex] - customerSizes[customerIndex]
            
            solution[customerIndex] = warehouseIndex
            connected.append(customerIndex)
            
            #print (solution)

    
    #print(capacityRemaining,solution)
    # calculate the cost of the solution
    
    used = [0]*warehouseCount
    for wa in solution:
        used[wa] = 1
    
    obj = sum([warehouses[x][1]*used[x] for x in range(0,warehouseCount)])
    for c in range(0, customerCount):
        obj += customerCosts[c][solution[c]]

    # prepare the solution in the specified output format
    outputData = str(obj) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, solution))

    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print 'Solving:', fileLocation
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/wl_16_1)'

