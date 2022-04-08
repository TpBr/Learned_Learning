from graph import Graph
def warshall(G):
    # apply Warshall's alg to graph G
    kList = [k for k in G.getVertices()]
    #print(kList)
    # list of vertex keys
    n = len(kList)
    # create adjacency matrix for graph G
    mat = [None]*n
    # create n x n matrix
    for i in range(n):
        #or pick max integer to represent "infinity"
        mat[i] = [10000000000000]*n
        # for every i,j where there is an edge set to True
    for i in range(n):
        c1 = kList[i]
        nbrs = [v.id for v in G.getVertex(c1).getConnections()]
        for c2 in nbrs:
            j = kList.index(c2) 
            mat[i][j] = G.getVertex(c1).getWeight(G.getVertex(c2))
            
    for i in range(0, len(mat)):
        mat[i][i] = 0
    #print out initial matrix
    for i in range(len(mat)):
        print(mat[i])
         #main loop (Warshall Algorithm)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(mat[i][j] > mat[i][k] + mat[k][j]):
                     mat[i][j] = (mat[i][k] + mat[k][j])

    return kList, mat

import random 
if __name__ == '__main__':
    G = Graph()
    alphabet = 'abcdefg'
    for c in alphabet:
         G.addVertex(c)    
    kList = [v for v in G.getVertices()]
    print(kList)
    n = len(kList) # number of vertices
    # create random graph with degree <=2 for each vertex
    random.seed(23472578)
    for c1 in kList:
         for i in range(2):
              c2 = kList[random.randrange(n)]
              G.addEdge(c1,c2, random.randrange(0,10))
  #   printing the original graph just created
    for c1 in kList:     
         print('Vertex:',c1,'AdjList:', \
                [v.id for v in G.getVertex(c1).getConnections()])
    wList,mat = warshall(G)
     #printing vertices and matrix for graph after Warshall
    print('wList =',wList)
    for i in range(len(mat)):
        print(mat[i])