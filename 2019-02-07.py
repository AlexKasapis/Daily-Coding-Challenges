# ===== PROBLEM DESCRIPTION =====
#
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
#
# I am extending the problem by asking to return every list of contiguous elements that sum to K, instead of the first
# one, as it was implied in the description. I am also assuming that these integers can only be positive. I may update
# this problem in the future to include negative numbers and negative Ks.
#
# ===== SOLUTION =====
#
# I am linearly parsing the input list, and for each element I store information about the list of contiguous elements
# that is created with starting index that element. This information is stored as a list of size 3, containing the
# starting index, the ending index and the sum of the elements between these indexes (including them). This list is
# stored in another list, named "candidates" and is updated in each loop while parsing the initial list. If while
# adding new elements, a candidate sums to our desired number K, it is removed from the "candidates" list and placed in
# the "solutions" list. If a candidate's sum exceeds the number K it is altogether removed from the "candidates" list.
# At the end of the initial list's traversal I am returning the solutions I found in a list form.
#
# ====================


def solve_problem(input_list, k):
    # Initialize the candidates and solutions lists
    # These lists are formatted as such: [start_index, end_index, sum_of_elements]
    candidates = []
    solutions = []

    # Parse the input list
    for i in range(len(input_list)):

        # Update the candidates - in reversed order because removing elements may mess up our traversal
        for j in range(len(candidates) - 1, 0, -1):
            # Increase the end index by one
            candidates[j][1] += 1
            # Add the number of the newly added element to the candidate's sum
            candidates[j][2] += input_list[i]

            # Check if the sum matches or exceeds our number K
            if candidates[j][2] >= k:
                if candidates[j][2] == k:
                    solutions.append(candidates[j])
                del candidates[j]

        # Add the the candidates list a new candidate consisting solely of the currently examining element
        candidates.append([i, i, input_list[i]])

    # Return the solutions found in a list of lists form
    return [[input_list[i] for i in range(solution[0], solution[1] + 1)] for solution in solutions]


if __name__ == '__main__':
    initial_list = [1, 1, 3, 8, 5, 7, 1, 2, 5, 9, 3, 1, 10, 2, 5, 6, 2, 8, 10]
    target_sum = 13
    result = solve_problem(initial_list, target_sum)
    print("Initial list is: {}".format(initial_list))
    for result_list in result:
        print("A solution is: {}".format(result_list))

