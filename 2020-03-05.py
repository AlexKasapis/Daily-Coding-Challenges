# PROBLEM
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.
#
# SOLUTION
# Imagine a binary tree, in the topological sense, meaning each node has one or two branches. This tree does not
# help us search anything faster. Now, the root of this tree is the whole encoded string and each branch node is
# a different letter we can extract from the parent node, starting from the start. Because we can either take one
# or two numbers that will be translated into a letter, the tree is in the form of a binary tree. For example, for
# the encoded string "111" which is the root, two new nodes branch out, the left one extracting the letter 'a' for
# the number 1, leaving the rest of the encoded string to be "11", and the right one extracting the letter 'k' for
# the number 11, leaving the rest of the encoded string to be "1". This continues for each node until there is no
# more string to parse. The leaves of this tree are all the possible translations for the message. Now, because
# creating a new subtree for each node requires parsing the tree every time, we are going to forfeit the idea of
# the tree, which does not even serve a purpose except for helping visualizing the solution. We are instead going
# to have a list of the current "branches" and a list of the solutions, which is going to start being populated
# when the string of a "branch" runs out. This solution has a time complexity of O(n).


def get_possible_letters(node):
    # This list will contain the new branch or branches that will result from this node.
    branches = []

    # Get the first letter of the node's remaining message and translate it.
    # Create a new node and add it to the branches list.
    branches.append((node[0][1:], node[1] + mapper.get(node[0][0])))

    # If there are two or more numbers in the node, see if there is
    # a possibility to translate the two numbers into a letter.
    if len(node[0]) >= 2 and int(node[0][:2]) <= 26:
        branches.append((node[0][2:], node[1] + mapper.get(node[0][:2])))

    return branches


# Declare the starting message and the mapper
message = '111'
mapper = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k',
    '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u',
    '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'
}

if __name__ == '__main__':
    # Initialize the branches list with the starting message.
    # The second item of the tuple is the translated part of the message for that node.
    currentBranches = [(message, '')]

    # Create an empty list that will store the translations.
    solutions = []

    # While there are more branches to parse, keep going.
    while len(currentBranches) > 0:
        # Remove the first node from the vector.
        currentNode = currentBranches.pop(0)

        # Decode the next letter or letters from the current node.
        newNodes = get_possible_letters(currentNode)

        # Add the contents of the new list to the currentBranches if there is more of the message
        # to decode. If the message is done, add the translated value to the solutions list.
        for newNode in newNodes:
            if len(newNode[0]) == 0:
                solutions.append(newNode[1])
            else:
                currentBranches.append(newNode)

    # Print the final result.
    print(f'There are {len(solutions)} possible ways to decode the message {message}')
