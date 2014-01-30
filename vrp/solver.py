#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

def length(customer1, customer2):
    return math.sqrt((customer1[1] - customer2[1])**2 + (customer1[2] - customer2[2])**2)


def tourLen(mlist):
    sum = 0
    
    for i in range(len(mlist)-1):
        sum = sum + length(customers[mlist[i]],customers[mlist[i+1]])

    return sum

tabuCount = 0
def Opt(tours):
    global customerCount
    global remainingCap
    global customers
    global tabu
    global tabuCount
    
    best = []
    
    # Pick random customer
    customer = 0
    while customer == 0:
        orig_i = random.randint(0,vehicleCount-1) # which tour
        orig_j = random.randint(1,len(tours[orig_i])-1) # position in tour i
        
        customer = tours[orig_i][orig_j]
        
        # check if swaping this customer is tabu
        if tabu[customer] >= 0:
            tabu[customer] = tabu[customer] - 1
        else:
            tabuCount += 1
            if (tabuCount>5000):
                tabu = [5]*customerCount
            continue

    # remove from original position
    tours[orig_i].remove(customer)
    remainingCap[orig_i] = remainingCap[orig_i] + customers[customer][0]
    
    # replace in all other possible positions
    minLen = float("inf")
    for i in range(vehicleCount): # use symmetry breaking here
        tour = copy.copy(tours[i])
        
        for j in range(1,len(tours[i])):
            
            if(remainingCap[i] - customers[customer][0] >=0):
                pass
            else:
                continue
            
            tours[i].insert(j,customer)
            
            newLen = totalLen(tours)
            
            if(newLen<=minLen):
                # better swap
                minLen = newLen
                best = copy.copy(tours[i])
                best_i = i
            else:
                # worse swap
                pass
            
            tours[i] = copy.copy(tour)
    
    # select min configuration
    if best != []:
        tours[best_i] = copy.copy(best)
        remainingCap[best_i] = remainingCap[best_i] - customers[customer][0]
    else:
        tours[orig_i].insert(orig_j,customer)
        #print("no best",tours,customer)
    
    return tours

def update(i,j,orig,new):
    # in tour i, j was replaced with new and originally had orig
    if i == -1:
        return
    
    global remainigCap
    global customers
    
    remainingCap[i] = remainingCap[i] + customers[orig][0] - customers[new][0]
    
    

def Opt2(tours):
    global customerCount
    global remainingCap
    global customers
    
    # Pick random customer
    customer = 0
    while customer == 0:
        orig_i = random.randint(0,vehicleCount-1) # which tour
        orig_j = random.randint(1,len(tours[orig_i])-1) # position in tour i
        
        customer = tours[orig_i][orig_j]

    best = []
    sfrom = (-1,-1,-1,-1)
    sto = (-1,-1,-1,-1)
    # swap in all other possible positions
    minLen = float("inf")
    # Select other customer
    for i in range(vehicleCount): # use symmetry breaking here
        for j in range(1,len(tours[i])-1):
            
            orig = copy.deepcopy(tours)
            
            if(remainingCap[i] + customers[tours[i][j]][0] - customers[tours[orig_i][orig_j]][0] >=0 and remainingCap[orig_i] + customers[tours[orig_i][orig_j]][0] - customers[tours[i][j]][0] >=0):
                # feasible swap, swap vehicleTours[i][j[ with customer who is at vehicleTours[orig_i][orig_j]
                temp = tours[i][j]
                tours[i][j] = customer
                tours[orig_i][orig_j] = temp
                
                newLen = totalLen(tours)
                if(newLen<=minLen):
                    minLen = newLen
                    best = copy.deepcopy(tours)
                    sfrom = (i,j,tours[i][j],tours[orig_i][orig_j]) #shows that in the ith tour j was replaced with tours[i][j]
                    sto = (orig_i,orig_j,tours[orig_i][orig_j],tours[i][j])
                    
                tours = copy.deepcopy(orig)
                
            else:
                continue
    
    # select min configuration
    if best == []:
        pass
        #tours = copy.deepcopy(tours)
    else:
        tours = copy.deepcopy(best)
        update(sfrom[0],sfrom[1],sfrom[2],sfrom[3])
        update(sto[0],sto[1],sto[2],sto[3])

    return tours

count = 0
swap = []
def validSwap(a,b):
    global swap
    global count
    
    if((a,b) in swap ): #or (b,a) in swap
        #this swap has happened before 
        count = count + 1
        if(count > 50):
            count = 0
            swap = []
            #print("<<<----------------------reset")
        return False
    else:
        count = 0
        swap.append((a,b))
        return True

def totalLen(Tours):
    obj = 0
    for v in range(0, vehicleCount):
        vehicleTour = Tours[v]
        if len(vehicleTour) > 0:
            obj += length(customers[0],customers[vehicleTour[0]])
            for i in range(0, len(vehicleTour) - 1):
                #print i,vehicleTour[i+1]
                obj += length(customers[vehicleTour[i]],customers[vehicleTour[i + 1]])
            obj += length(customers[vehicleTour[-1]],customers[0])
            
    return obj

def uniqueTours(tours):
    # This is to break symmetry
    global vehicleTours

    #print vehicleTours
    seen = []
    tourcount = 0
    for tour in vehicleTours:
        if tour not in seen:
            seen.append(tour)
            tourcount = tourcount + 1
    
    return tourcount

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')
    
    global vehicleCount
    global customers
    global customerCount

    parts = lines[0].split()
    customerCount = int(parts[0])
    vehicleCount = int(parts[1])
    vehicleCapacity = int(parts[2])
    depotIndex = 0
    
    print(customerCount,vehicleCount,vehicleCapacity)

    customers = []
    for i in range(1, customerCount+1):
        line = lines[i]
        parts = line.split()
        customers.append((int(parts[0]), float(parts[1]),float(parts[2])))

    # demand ,x ,y
    
    sortedCustomers = copy.copy(customers)
    for i in range(len(sortedCustomers)):
        sortedCustomers[i] = (sortedCustomers[i],i)
    sortedCustomers.sort()
    #sortedCustomers.reverse()
    
    global tabu
    tabu = [5]*customerCount
    #---------------------------------------------INIT-----------------------------------------------

    global vehicleTours
    vehicleTours = []

    vehicleTours = [[0, 5, 49, 33, 10, 39, 45, 15, 44, 37, 17, 12, 0], [0, 18, 13, 41, 40, 19, 42, 4, 47, 0], [0, 32, 1, 22, 3, 29, 21, 34, 30, 9, 50, 16, 38, 46, 0], [0, 11, 2, 20, 35, 36, 28, 31, 8, 0], [0, 27, 48, 26, 7, 23, 43, 24, 25, 14, 6, 0]]
    
    
    
    


    #print remainingCap
    #print vehicleTours    
    # checks that the number of customers served is correct
    #assert sum([len(v) for v in vehicleTours]) == customerCount - 1

    # calculate the cost of the solution; for each vehicle the length of the route
    obj = 0
    for v in range(0, vehicleCount):
        vehicleTour = vehicleTours[v]
        if len(vehicleTour) > 0:
            obj += length(customers[depotIndex],customers[vehicleTour[0]])
            for i in range(0, len(vehicleTour) - 1):
                obj += length(customers[vehicleTour[i]],customers[vehicleTour[i + 1]])
            obj += length(customers[vehicleTour[-1]],customers[depotIndex])



    # prepare the solution in the specified output format

    for v in range(0,vehicleCount):
        for p in range(len(vehicleTours[v])-2):
            if (vehicleTours[v][p] == 0 and vehicleTours[v][p+1] == 0):
                vehicleTours[v].pop(0)
                
            

    for v in range(0, vehicleCount):
        #print v
        if(len(vehicleTours[v])<=2):
            #vehicleTours[v].pop()
            vehicleTours[v] = []
            #print "breaking",v
            #break
        else:
            vehicleTours[v].pop()
            vehicleTours[v].pop(0)
    
    
    outputData = str(obj) + ' ' + str(0) + '\n'
    for v in range(0, vehicleCount):
        outputData += str(depotIndex) + ' ' + ' '.join(map(str,vehicleTours[v])) + ' ' + str(depotIndex) + '\n'

    return outputData


import sys
import copy
import random

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print 'Solving:', fileLocation
        print solveIt(inputData)
    else:

        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/vrp_5_4_1)'

