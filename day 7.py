def listToString(x): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in x: 
        str1 += ele  
    
    # return string  
    return str1 

def swap_case(s):
    list = []
    for element in s:
        if element.isupper() == True:
            list.append(element.lower())
        elif element.isupper() == False:
            list.append(element.upper())
        else:
            list.append(element.upper())
    return listToString(list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)