'''
Created on 2013-07-20

@author: Umar
'''

import sys

if __name__ == '__main__':
    file = open('sol.txt', 'r')
    input = ''.join(file.readlines())
    file.close()
    lines = input.split('\n')
    solution = []
    for line in lines:
        if 'y' in line:
            solution.append(-1)
    for line in lines:
        if 'y' in line:
            one = line.split(' ')
            connection = one[0].split('_')
            
            solution[int(connection[2])] = int(connection[1])
            
    print solution