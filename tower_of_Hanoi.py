def tower_of_hanoi(n,source,target,auxiliary):
    if n==1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        tower_of_hanoi(n-1,source,auxiliary,target)
        print(f"move disk {n} from {source} to {target}")
        tower_of_hanoi(n-1,auxiliary,target,source)
tower_of_hanoi(3,'A','B','C')