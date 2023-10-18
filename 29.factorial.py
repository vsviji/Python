def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage:
number = int(input("enter the number"))
factorial = calculate_factorial(number)
print(f"The factorial of {number} is {factorial}")
