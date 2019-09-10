
for i in range( 1 , 10 ):
    for j in range( 1 , i ):    
        print(end='            ')
    for j in range( i , 10 ):
        print(f"{j:<2d}x{i:2d} = {j*i:2d}",end='  ')
    print()
    
    