def largest_number(n):
    largest = 0
    while n>0:
        digit = n% 10
        if(largest<digit):
            largest = digit
        n = n//10
    return largest
print(largest_number(692486))    
