'''for i in range(5):
    for j in range(i):
        print("*",end='  ')
    print()
    
OUTPUT:
    * 
    * *
    * * *
    * * * * '''
    
#reverse pattern for above  one
'''for i in range(5):
    for j in range(5-i):
        print("*",end=' ')
    print()
OUTPUT:
    * * * * * 
    * * * * 
    * * * 
    * * 
    *'''
    
# tree like pattern: we neeed thre for loops
'''for i in range(5):
    for k in range(5-i):
        print('',end=' ')
    for j in range(i):
        print("*",end=' ')
    print()
    
OUTPUT: *
       * *
      * * *
     * * * *'''