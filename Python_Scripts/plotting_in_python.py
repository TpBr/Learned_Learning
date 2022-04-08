import matplotlib.pyplot as plt
import math

def FirstPlot(x,y,c):
    logx = []
    logy = []
    for i in x:
        logx.append(math.log10(i))
    for i in y: 
        logy.append(math.log10(i))   
    print('Plotting now!')
    plt.plot(logx,logy,label=c)
    plt.legend()
    print('Done plotting!')
    
    
def SecondPlot(x,y,c):
    logx = []
    
    
    logy = []
    for i in x:
        logx.append(math.log10(i)) 
        
    for i in range(0, len(y)):
        logy.append(y[i]/x[i])
        
        
        
    print('Plotting now!')
    plt.plot(logx,logy,label=c)
    plt.legend()
    print('Done plotting!') 


    
    
    
    
if __name__=='__main__':
    #First Plot
    plt.figure("First Plot")
    nlist = [10,30,100,300, 1000, 3000, 10000, 100000]
    nc_sorted_MergeSort = [19, 77, 356, 1308, 5044, 18076, 69008, 853904]
    FirstPlot(nlist,nc_sorted_MergeSort,'Reverse Array-MergeSort')  
    
    nlist = [10,30,100,300, 1000, 3000, 10000, 100000]
    nc_sorted_MergeSort = [22, 106, 550, 2107, 8727, 30926, 120483, 1536096]
    FirstPlot(nlist,nc_sorted_MergeSort,'Random Array - MergeSort') 
    
    nlist = [10,30,100,300, 1000, 3000, 10000, 100000]
    nc_sorted_MergeSort = [15, 71, 316, 1180, 4932, 16828, 64608, 815024]
    FirstPlot(nlist,nc_sorted_MergeSort,'Sequential Array-MergeSort') 
    
    
    
    nlist = [10,30,100,300, 1000, 3000, 10000, 100000]
    nc_sorted_MergeSort = [54, 464, 5049, 45149, 500499, 4501499, 50004999, 5000049999]
    FirstPlot(nlist,nc_sorted_MergeSort,'Reverse Array-InstertionSort')  
    
    nlist = [10,30,100,300, 1000, 3000, 10000, 100000]
    nc_sorted_MergeSort = [44, 216, 2481, 22845, 238048, 225488, 24754009, 2505191376]
    FirstPlot(nlist,nc_sorted_MergeSort,'Random Array - InstertionSort') 
    
    nlist = [10,30,100,300, 1000, 3000, 10000, 100000]
    nc_sorted_MergeSort = [9, 29, 99, 299, 999, 2999, 9999, 99999]
    FirstPlot(nlist,nc_sorted_MergeSort,'Sequential Array-InstertionSort')
    
    
    
    plt.show()
    
    
    
    #Second Plot
    plt.figure("Second Plot")
    nlist = [10,30,100,300, 1000, 3000, 10000, 100000]
    nc_sorted_MergeSort = [19, 77, 356, 1308, 5044, 18076, 69008, 853904]
    SecondPlot(nlist,nc_sorted_MergeSort,'Reverse Array-MergeSort')  
    
    nlist = [10,30,100,300, 1000, 3000, 10000, 100000]
    nc_sorted_MergeSort = [22, 106, 550, 2107, 8727, 30926, 120483, 1536096]
    SecondPlot(nlist,nc_sorted_MergeSort,'Random Array - MergeSort') 
    
    nlist = [10,30,100,300, 1000, 3000, 10000, 100000]
    nc_sorted_MergeSort = [15, 71, 316, 1180, 4932, 16828, 64608, 815024]
    SecondPlot(nlist,nc_sorted_MergeSort,'Sequential Array-MergeSort') 
    
    plt.show()
    
    
    print('done')