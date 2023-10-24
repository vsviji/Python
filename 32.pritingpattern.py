def print_pattern(height, width, pattern):
    for i in range(height):
        for j in range(width):
            print(pattern, end="")
        print()

# Example usage:
height = 5
width = 10
pattern = "*"

print_pattern(height, width, pattern)
