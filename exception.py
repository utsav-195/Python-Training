n=input()
l=[]
for i in range(0,int(n)):
    l.append(input())
#print(l)
for i in range(0,len(l)):
    try:
        #print("i",i)
        #ab=l[i].split()
        a=int(l[i][0])
        #print("a",a)
        b=int(l[i][2])
        #print("b",b)
        print(a//b)
    except (ValueError,ZeroDivisionError) as e:
        print("Error Code:",e)