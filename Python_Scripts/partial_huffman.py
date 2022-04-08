from min_heap import MinHeap

def huffman (frequencies):
    h = MinHeap(frequencies,[i for i in range(len(frequencies))])
    n_nodes = len(frequencies)
    # create parent array for Huffman tree
    parent = [-1]*(2*len(frequencies)-1)
    for i in range(len(frequencies)):
        # print('heap =',h)
        # print('parent =',parent)
        f1,n1 = h.pull()
        f2,n2 = h.pull()
        # print('n1 =',n1,', f1 =',f1,', n2 =',n2,', f2 =',f2)
        h.add(f1+f2,n_nodes)
        parent[n1] = n_nodes
        parent[n2] = n_nodes
        n_nodes = n_nodes + 1
    # print('complete parent array =',parent)
    
    # now create lchild and rchild for the left and right children
    # ... first initialize as arrays or -1's
    lchild = [-1]*len(parent)
    rchild = [-1]*len(parent)
    for n in range(len(parent)): # for each node...
        p = parent[n]
        if p >= len(parent) or p < 0: # invalid parent, so n must be root
            pass
        else: # n is left child of p unless lchild[p] already set
            if lchild[p] < 0:
                lchild[p] = n
            else:
                rchild[p] = n
    # print('lchild =',lchild)
    # print('rchild =',rchild)
    
    # now generate codes for each letter
    codebook = [None]*len(frequencies)
    for n in range(len(frequencies)):
        # go from leaf up to root, 
        # using 0 if you are left child, 1 if a right child
        # Then reverse the list.
        n0 = n # save original letter number
        code = []
        while n < len(parent):
            p = parent[n]
            if p >= len(parent): # n is root
                break # while loop
            else: # add 0 or 1
                if n == lchild[p]:
                    code.append(0)
                else: # n == rchild[p]
                    code.append(1)
                n = p # go to parent node
                
        code.reverse()
        codebook[n0] = code
        # print('n0 =',n0,', code =',code)
        
    return codebook,lchild,rchild

#def decode(lchild,rchild,input):
#    # Decode a list of bits in input according to huffman tree
#    # as represented by the lchild (left child) & rchild (right child)
#    # arrays.
#    # Note that left children correspond to 0, and right children to 1.
#    # ... 15 lines of code ...
#    return output
#
#def encode(codebook,input):
#    output = []
#    # ... two lines of code ...
#    return output
    
       
if __name__== '__main__':
    
    aList = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,14.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074,15]
    ans = huffman(aList)
    print(ans[0])    