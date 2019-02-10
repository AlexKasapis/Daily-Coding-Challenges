# ===== PROBLEM DESCRIPTION =====
#
# Given a string and a set of characters, return the shortest substring containing all the characters in the set.
# For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".
# If there is no substring containing all the characters in the set, return null.
#
# I will assume the substring must be case sensitive.
#
# ===== SOLUTION =====
#
# I am traversing the string, keeping an eye for the last time I found each character in the input string. Once I have
# encountered every charater in the string, a substring is created, with starting index the index of the character I
# found less recently, and ending index the index of the character I found most recently. When I re-encounter a
# character, its index changes to the newest one. Each time a character updates its index, I check whether the substring
# created is shorter than the last shortest substring. If yes, I store that as the shortest substring. Through this
# process, at the end of the input string traversal I will have the shortest substring containing all the characters in
# the set.
#
# If we assume the length of the input string to be N and the number of characters to search for to be M, the time
# complexity of this solution is O(N*M) and the space complexity is O(N+M).
#
# ====================


def solve_problem(input_string, character_set):
    """
    Runs the algorithm described above.
    :param input_string: The input string to search for substrings
    :param character_set: The characters of interest
    :return: The shortest substring created, or None, if no substrings were found through the process
    """

    # Create a dictionary with keys the characters in the set, and values their latest position in the string
    character_catalog = {char: -1 for char in character_set}
    shortest_substring = None

    # Go through the string, updating the latest positions of the characters of interest
    for i in range(len(input_string)):
        char = input_string[i]
        if char in character_set:
            character_catalog[char] = i

            # If the substring found is shorter than the currently shortest substring, replace it
            substring = get_substring(input_string, character_catalog)
            if not shortest_substring or len(substring) < len(shortest_substring):
                shortest_substring = substring

    # Return the shortest substring found, after the input string traversal
    # If no substrings were found, the return value will be None
    return shortest_substring


def get_substring(string, character_catalog):
    """
    Get the substring created by a set of specified characters and all other characters inbetween those.
    :param string: The input string
    :param character_catalog: A dictionary. {'character': position of character in the string}
    :return: The substring created.
    """

    # Make sure each character in the catalog has been found at least once in the input string, so far
    complete_catalog = True
    for index in character_catalog.values():
        if index == -1:
            complete_catalog = False

    # Keep the first and last indices of the substring
    if complete_catalog:
        start_index = len(string)
        end_index = -1
        for index in character_catalog.values():
            if index < start_index:
                start_index = index
            if index > end_index:
                end_index = index

        # Return the substring created by the two indices
        return string[start_index:end_index+1]

    # If the character catalog is not complete, a substring is not created
    return None


if __name__ == '__main__':
    input_str = 'figehaeci'
    char_set = ['a', 'e', 'i']
    result = solve_problem(input_str, char_set)

    # Print the result
    print('Input string: \'{}\''.format(input_str))
    print('Character set: \'{}\''.format('\', \''.join(char_set)))
    if result:
        print('The result is: \'{}\''.format(result))
    else:
        print('No substring in the input string that contains these characters')
