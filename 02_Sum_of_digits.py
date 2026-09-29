def Sum_of_digit(n):
    sum = 0
    while n>0:
        digit = n % 10
        sum = sum + digit
        n = n//10
    return sum
print(Sum_of_digit(6932))