# function of sum

def sum_or_triple_sum(a, b, c):
    if a == b == c:
        result = (a * b * c)
    else:
        result = a + b + c
    return result


# User Input

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the third number:"))

# calculate

result = sum_or_triple_sum(num1, num2, num3)
print(f"The result is: {result}")
