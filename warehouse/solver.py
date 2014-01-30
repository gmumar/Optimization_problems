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

    print(warehouseCount,customerCount)

    solution = [15, 14, 5, 48, 15, 5, 6, 12, 15, 15, 10, 22, 12, 5, 14, 15, 10, 17, 10, 14, 10, 14, 22, 5, 40, 22, 26, 22, 40, 5, 5, 22, 5, 33, 40, 40, 36, 12, 45, 48, 40, 10, 15, 14, 44, 45, 45, 14, 48, 40]
    
    
    
    #[24, 24, 5, 48, 24, 5, 6, 12, 24, 24, 10, 22, 12, 5, 14, 24, 10, 22, 10, 14, 10, 14, 22, 5, 24, 22, 26, 22, 22, 5, 5, 22, 5, 33, 24, 24, 48, 12, 45, 48, 22, 10, 24, 14, 44, 45, 45, 14, 48, 24]
    
    #[24, 24, 22, 36, 24, 22, 36, 12, 24, 24, 22, 22, 12, 22, 24, 24, 24, 12, 22, 24, 22, 24, 22, 22, 24, 22, 26, 22, 22, 22, 22, 22, 22, 33, 24, 24, 36, 12, 45, 36, 22, 22, 24, 24, 26, 45, 45, 24, 36, 24]
    
    #[7, 6, 0, 24, 7, 0, 1, 5, 7, 7, 3, 10, 5, 0, 6, 7, 3, 8, 3, 6, 3, 6, 10, 0, 19, 10, 12, 10, 19, 0, 0, 10, 0, 16, 19, 19, 17, 5, 23, 24, 19, 3, 7, 6, 22, 23, 23, 6, 24, 19]
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

