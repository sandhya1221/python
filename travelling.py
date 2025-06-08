def travelling(distance):
    n=len(distance)
    queue=[]
    queue.append((0,[0],0))
    best_cost=float('inf')
    best_path=[]
    while queue:
        city,path,cost=queue.pop(0)
        if len(path)==n:
            total_cost=cost+distance[city][0]
            if total_cost<best_cost:
                best_cost=total_cost
                best_path=path+[0]
        else:
            for next_city in range(n):
                if next_city not in path:
                    new_cost=cost+distance[city][next_city]
                    queue.append((next_city,path+[next_city],new_cost))
    return best_path,best_cost
dist=[[0,10,25,30],
      [10,0,35,20],
      [15,30,0,25],
      [20,30,35,0]]
path,cost=travelling(dist)
print("Best path:",path)
print("Maximum cost:",cost)