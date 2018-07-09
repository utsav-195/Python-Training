n,x=map(int,input().split())
l=[]
for _ in range(x):
    l.append(list(map(float,input().split())))
#print(tuple(l))
a=[1,2,3]
b=[2,3,4]
c=[5,5,7]
#print(a)
#print(l[0])
#X=[l[0]]+[l[1]]+[l[2]]
X=[l[0]]
for i in range(1,len(l)):
    X+=[l[i]]
avgMatrix=zip(*X)
#print(*avgMatrix)
for i in avgMatrix:
    avg=0
    for x in i:
        avg+=x
    print(avg/len(i))