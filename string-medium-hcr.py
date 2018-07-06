def merge_the_tools(string, k):
    # your code goes here
    start=0
    end=k
    part=[]
    result=""
    for i in range(0,len(string)):
        part.append(string[start:end])
        start=end
        end+=k
        if end>len(string):
            break
    #print(part)
    for p in part:
        print(''.join(sorted(set(p), key=p.index)))