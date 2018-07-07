def wrap(string, max_width):
    start=0
    end=max_width
    result=""
    for i in range(0,len(string)):
        result+=string[start:end]+"\n"
        start=end
        end+=max_width
        if end>len(string):
            break
    result+=string[start:len(string)]
    return result