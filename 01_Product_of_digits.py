def Product_of_digit(n):
    product = 1
    while n>0:
        digit = n%10
        product = product*digit
        n= n// 10

    return product
print(Product_of_digit(64287))