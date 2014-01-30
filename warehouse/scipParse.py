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
        
    valid = [64, 51, 59]
    
    print(warehouseCount,customerCount)
    #print(avgDistanceToWarehouse)
    #print("warehouses",warehouses)
    #print("customer Costs",customerCosts)
    #print("customer Sizes",customerSizes)
    #print ("cap remaining",capacityRemaining)
    
    f = open('test.pip','w')
    

    f.write("Minimize\n"),
    #f.write ("obj:")
    
    # Sum of all warehouses and there fixed costs
    for i in range(warehouseCount):
        if i in valid:
            f.write (repr(warehouses[i][1]) + ' x_' + repr(i) + '+\n' ),

    # Sum of travel costs between all customers
    for i in range(warehouseCount):
        for k in range(customerCount):
            if i in valid:
                f.write (repr(customerCosts[k][i]) + ' y_' + repr(i) + '_' + repr(k) + '+\n') ,
            
    # Constraints
    f.write ("0\nSubject to\n"),
    
    for i in range(warehouseCount):
        if i in valid:
            s_warehouse = 'x_' + repr(i)
            for j in range(warehouseCount):
                if j in valid:
                    for k in range(customerCount):
                        s_customer = 'y_' + repr(i)+ '_' + repr(k)
                        f.write (s_customer + ' - '  + s_warehouse + ' <=0\n')
                
            
    for j in range(customerCount):
        for k in range(warehouseCount):
            if k in valid:
                s_customer = 'y_' + repr(k) + '_' + repr(j)
                if(k==warehouseCount-1):
                    f.write (s_customer ),
                else:
                    f.write (s_customer + ' + ' ),
            
        f.write (' ==1\n')
        
    for k in range(warehouseCount):
        if k in valid:
            for j in range(customerCount):
                if(j==customerCount-1):
                    s_customer = repr(customerSizes[j]) + ' y_' + repr(k) + '_' + repr(j)
                else:
                    s_customer = repr(customerSizes[j]) + ' y_' + repr(k) + '_' + repr(j) + ' + '
                f.write(s_customer)
            
            f.write(' <= ' + repr(warehouses[k][0]) + '\n')

    #===========================================================================
    # f.write ("Bounds\n"),
    # 
    # for i in range(warehouseCount):
    #     s = 'x' + repr(i)
    #     f.write s,
    # 
    # for i in range(warehouseCount):
    #     for k in range(customerCount):
    #         s = 'y' + repr(i) + repr(k)
    #         f.write s,
    #===========================================================================



    f.write ("\nBinary\n"),
    
    for i in range(warehouseCount):
        if i in valid:
            s = 'x_' + repr(i) +' '
            f.write (s),
    
    for i in range(warehouseCount):
        if i in valid:
            for k in range(customerCount):
                s = 'y_' + repr(i) +'_' + repr(k) +' '
                f.write( s),

    f.write("\n")
    f.write("End")
    return("End")

import sys

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

