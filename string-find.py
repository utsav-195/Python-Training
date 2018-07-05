def count_substring(string, sub_string):
    co=0
    set=0
    for i in range(0,len(string)):
        #print(set)
        #print(count)
        string=string[set:]
        num=string.find(sub_string)
        #print(num)
        set=num+1
        co+=1
        if set<=0:
            break
    #print (co)
    return co-1