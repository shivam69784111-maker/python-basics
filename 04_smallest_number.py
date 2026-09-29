def smallest_number(n):
    smallest = 9
    while n>0:
        digit = n% 10
        if(smallest>digit):
            smallest = digit
        n = n//10
    return smallest
print(smallest_number(692486))    
