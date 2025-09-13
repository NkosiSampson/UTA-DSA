"""Assignment 1: Friend of a Friend

Please complete these functions, to answer queries given a dataset of
friendship relations, that meet the specifications of the handout
and docstrings below.

Notes:
- you should create and test your own scenarios to fully test your functions, 
  including testing of "edge cases"
"""

"""
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************
************** READ THIS ***************

If you worked in a group on this project, please type the EIDs of your groupmates below (do not include yourself).
Leave it as TODO otherwise.
Groupmate 1: TODO
Groupmate 2: TODO
"""


def load_pairs(filename):
    """
    Args:
        filename (str): name of input file

    Returns:
        List of pairs, where each pair is a Tuple of two strings

    Notes:
    - Each non-empty line in the input file contains two strings, that
      are separated by one or more space characters.
    - You should remove whitespace characters, and skip over empty input lines.
    """

# ------------ BEGIN YOUR CODE ------------

    list_of_pairs = []
    with open("friends-NkosiSampson/myfriends.txt", "rt") as infile:
        for line in infile:
            if line == "\n":
                pass
            else:
                list_of_pairs.append(tuple((line.split()))) #converted to tuple
    return list_of_pairs
print(load_pairs("friends-NkosiSampson/myfriends.txt"))
directory = dict()

# ------------ END YOUR CODE ------------


