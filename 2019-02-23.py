# PROBLEM DESCRIPTION
# Given a sorted list of integers, square the elements and give the output in sorted order.
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
#
# SOLUTION
# Lets assume two pointers, pointing to the start and end of the list. The pointer which points to the number with the
# highest absolute value moves towards the other. The number, after it has been squared, is inserted to the start of
# the output list. This loop stops when the two pointers pass each other. This solution has a time complexity of O(n).

if __name__ == '__main__':
    numbers = [-9, -2, 0, 2, 3]  # Example list
    output = []

    # Initiate the left and right pointers
    left_pointer = 0
    right_pointer = len(numbers) - 1

    # Loop until the two pointers pass each other, meaning that right pointer will be on the left side of the left
    # pointer and thus having a lower value than the right pointer.
    while left_pointer <= right_pointer:
        if abs(numbers[left_pointer]) > abs(numbers[right_pointer]):
            output.insert(0, pow(numbers[left_pointer], 2))
            left_pointer += 1
        else:
            output.insert(0, (pow(numbers[right_pointer], 2)))
            right_pointer -= 1

    print(output)
