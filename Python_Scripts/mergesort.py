import random


def mergesort1(a):
    """mergesort1(a) -- returns sorted list of a's elements
    Uses mergesort algorithm applied to lists using append
    Returns pair of sorted list and number of comparisions"""
    n = len(a)
    if n <= 1:
        return a,0
    else:
        m = n // 2
        a1 = a[0:m]
        a2 = a[m:n]
        b1,nc1 = mergesort1(a1)
        b2,nc2 = mergesort1(a2)
        b, nc3 = merge1(b1,b2)
        return b,(nc1+nc2+nc3)

def merge1(l1,l2):
    """merge1(l1,l2) -- returns merged list containing entries of lists l1 & l2
    Returns pair of the merged list and the number of comparisons between items"""
    l = []
    n1 = len(l1)
    n2 = len(l2)
    i1 = 0
    i2 = 0
    n_comparisons = 0
    while i1 < n1 and i2 < n2:
        n_comparisons = n_comparisons + 1
        if l1[i1] <= l2[i2]:
            l.append(l1[i1])
            i1 = i1 + 1
        else:
            l.append(l2[i2])
            i2 = i2 + 1
    while i1 < n1:
        l.append(l1[i1])
        i1 = i1 + 1
    while i2 < n2:
        l.append(l2[i2])
        i2 = i2 + 1
    return l,n_comparisons


def generateListRandom(n):
    
    outputList = []
    
    
    for i in range(0, n):
    
        outputList.append(random.randint(0, 1000))
        
    return outputList


def generateListSeq(n):
    
    outputList = []
    
    
    for i in range(0, n):
    
        outputList.append(i)
        
    return outputList

def generateListReverse(n):
    
    outputList = []
    
    i = n
    while i > 0:
    
        outputList.append(i)
        i-=1
        
    return outputList


if __name__ == '__main__':
    
    listInputSize = [10, 30, 100, 300, 1000, 3000, 10000, 100000]
    
    print("RANDOM")
    for i in listInputSize:
        a = generateListRandom(i)
        a_old = a.copy()
        a,nc = mergesort1(a)
        print("Input size is " + str(i))
        print('Number of comparisons =',nc)
        #print('a =',a_old)
        #print('sorted a =',a)
        print()
        print()
    print("SEQUENCIAL")
    for i in listInputSize:
        a = generateListSeq(i)
        a_old = a.copy()
        a,nc = mergesort1(a)
        print("Input size is " + str(i))
        print('Number of comparisons =',nc)
        #print('a =',a_old)
        #print('sorted a =',a)
        print()
        print()
    print("REVERSE")    
    for i in listInputSize:
        a = generateListReverse(i)
        a_old = a.copy()
        a,nc = mergesort1(a)
        print("Input size is " + str(i))
        print('Number of comparisons =',nc)
        #print('a =',a_old)
        #print('sorted a =',a)
        print()
        print()
    
    


