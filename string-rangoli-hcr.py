def print_rangoli(size):
    # your code goes here
    #top cone
    dash="-"
    j=0
    print(("-"*(size*2-2))+(chr(ord('a')+size-1))+("-"*(size*2-2)))
    for i in range(size-1,0,-1):
        print (("-"*(i*2-2)),end="")
        for j in range(size+1,i,-1):
            print((chr(ord('a')+j-2)+dash),end="")
        #print (j,end="")
        for k in range(j,size+1):
            if k==size:
                dash=""
            print((chr(ord('a')+k-1))+dash,end="")
            dash="-"
        print (("-"*(i*2-2)))
    for i in range(1,size):
        print("-"*(i*2),end="")
        for j in range(size,i,-1):
            print(chr(ord('a')+j-1)+dash,end="")
        for k in range(j,size):
            print(chr(ord('a')+k)+dash,end="")
        print("-"*((i*2)-1))
            