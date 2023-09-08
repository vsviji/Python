def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not found in the array

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
result = binary_search(my_list, target_value)

if result != -1:
    print(f"Found {target_value} at index {result}")
else:
    print(f"{target_value} not found in the list")
