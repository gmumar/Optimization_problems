#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    
    
    #------------------------INIT----------------------
    
    valid = []
    
    for i in range(warehouseCount):
        valid.append(i)
        
    #valid = [64, 51, 59]
    
    print(warehouseCount,customerCount)
    #print(avgDistanceToWarehouse)
    #print("warehouses",warehouses)
    #print("customer Costs",customerCosts)
    #print("customer Sizes",customerSizes)
    #print ("cap remaining",capacityRemaining)
    
    
    return("End")

import sys
from zibopt import scip

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        #f.write 'Solving:', fileLocation
        print (solveIt(inputData))
    else:
        print ('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/wl_16_1)')

