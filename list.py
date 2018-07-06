students=[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    list=[]
    list.append(name)
    list.append(score)
    students.append(list)
#print students
for i in range(0,len(students)-1):
    for j in range(0,len(students)-1-i):
        if students[j][1]==students[j+1][1]:
            #print students[j][1],students[j+1][0]
            #print students[j][0]<=students[j+1][0]
            if str(students[j][0]) >= str(students[j+1][0]):
                temp=students[j]
                students[j]=students[j+1]
                students[j+1]=temp
        elif students[j][1]<students[j+1][1]:
            temp=students[j]
            students[j]=students[j+1]
            students[j+1]=temp
#print students
min1=9999
min2=9999
for s in students:
    if s[1]<min1:
        min2=min1
        min1=s[1]
#print min2
for s in students:
    if s[1]==min2:
        print s[0]