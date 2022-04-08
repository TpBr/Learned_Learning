import random


# Insertion sort code
def insertion_sort(a):
    """insertion_sort(a) -- sorts a by insertion sort
    Returns number of comparisons"""
    n_comparisons = 0
    for i in range(1,len(a)):
        j = i-1
        n_comparisons = n_comparisons + 1
        while a[j] > a[j+1]:
            n_comparisons = n_comparisons + 1
            # swap a[j] and a[j+1]
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            j = j-1
            if j < 0:
                break
    return n_comparisons


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
        nc = insertion_sort(a)
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
        nc = insertion_sort(a)
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
        nc = insertion_sort(a)
        print("Input size is " + str(i))
        print('Number of comparisons =',nc)
        #print('a =',a_old)
        #print('sorted a =',a)
        print()
        print()
