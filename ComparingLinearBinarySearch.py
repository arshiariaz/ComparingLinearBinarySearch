# File: ComparingLinearBinarySearch.py
# Student: Arshia Riaz
# 
# Date Created: 10/31/2021
# Date Last Modified: 11/05/2021
# Description of Program: This program performs linear and binary searches to see on average how many probes are made when searching a list

def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    return (-low - 1, count)

import random
import math
index = 1000 
list = [] 
for i in range(index):
    list.append(i) 
random.shuffle(list)
print("Linear Search:")
n = 10
while n <= 100000:
    probes = 0
    for i in range(n):
        index = random.randint(1,1000)
        probes += linearSearch(list,index)
    probes /= n
    print("  Tests:",format(n," <7d")," Average Probes:",probes)
    n *= 10
list.sort()
probes = 0

for i in range(1000):
    index,count = binarySearch(list,random.randint(1,1000))
    probes += count
probes /= 1000
print("Binary Search:")
print("  Average number of probes:",probes)
diff = math.log(1000,2) - probes
if diff < 0:
    diff *= -1
print("  Differs from log2(1000) by:",diff)

