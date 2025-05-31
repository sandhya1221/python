#adjacency list
'''def printGraph(V,E,edges):
        # code here
        adjList=[]
        for i in range(V):
            adjList.append([])
        for n,m in edges:
            adjList[n].append(m)
            adjList[m].append(n)
        for lst in adjList:
            lst.sort()
        return adjList
V = 5, E = 7
edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
print(printGraph(V,E,edges))'''

#BFS in graph same like trees
def bfs(self, adj):
        # code here
    v=len(adj)
    visited=[0]*v
    startNode=0
    ans=[]
    q=[]
    if (visited[startNode]==0):
        visited[startNode]=1
        q=[startNode]
        while(q):
            node=q.pop(0)
            ans.append(node)
            for i in adj[node]:
                if(visited[i]==0):
                    visited[i]=1
                    q.append(i)
        return ans
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(bfs(adj))