def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum
num = 12345
result = sum_digits(num)
print(result)
