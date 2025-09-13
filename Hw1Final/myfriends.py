"""Assignment 1: Friend of a Friend

Please complete these functions, to answer queries given a dataset of
friendship relations, that meet the specifications of the handout
and docstrings below.

Notes:
- you should create and test your own scenarios to fully test your functions, 
  including testing of "edge cases"
"""

from py_friends.friends import Friends

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
    list_of_pairs = []
    with open(filename, 'rt') as infile:

# ------------ BEGIN YOUR CODE ------------
        for line in infile:
            if line == "\n":
                pass
            else:
                list_of_pairs.append(tuple(line.split()))


# ------------ END YOUR CODE ------------

    return list_of_pairs 

def make_friends_directory(pairs):
    """Create a directory of persons, for looking up immediate friends

    Args:
        pairs (List[Tuple[str, str]]): list of pairs

    Returns:
        Dict[str, Set] where each key is a person, with value being the set of 
        related persons given in the input list of pairs

    Notes:
    - you should infer from the input that relationships are two-way: 
      if given a pair (x,y), then assume that y is a friend of x, and x is 
      a friend of y
    - no own-relationships: ignore pairs of the form (x, x)
    """
    directory = dict()

    # ------------ BEGIN YOUR CODE ------------

    for duple in pairs:
        for name in duple:
            if name not in directory.keys() and name is duple[0]:
                myset = set()
                myset.add(duple[1])
                directory[name] = myset
            elif name not in directory.keys() and name is duple[1]:
                myset = set()
                myset.add(duple[0])
                directory[name] = myset
            elif name in directory.keys() and name is duple[0]:
                directory[name].add(duple[1])
            elif name in directory.keys() and name is duple[1]:
                directory[name].add(duple[0])
    print(directory)
    return directory


    # ------------ END YOUR CODE ------------

    return directory


def find_all_number_of_friends(my_dir):
    """List every person in the directory by the number of friends each has

    Returns a sorted (in decreasing order by number of friends) list 
    of 2-tuples, where each tuples has the person's name as the first element,
    the number of friends as the second element.
    """
    friends_list = []

    # ------------ BEGIN YOUR CODE ------------

    from operator import itemgetter
    for name in my_dir.keys():
        duple = []
        duple.append(name)
        numfriends = len(my_dir[name])
        duple.append(numfriends)
        friends_list.append(tuple(duple))
        friends_list = sorted(friends_list, key=itemgetter(1), reverse=True)
        friends_list = sorted(friends_list, key=itemgetter(0))
    

    # ------------ END YOUR CODE ------------

    return friends_list


def make_team_roster(person, my_dir):
    """Returns str encoding of a person's team of friends of friends
    Args:
        person (str): the team leader's name
        my_dir (Dict): dictionary of all relationships

    Returns:
        str of the form 'A_B_D_G' where the underscore '_' is the
        separator character, and the first substring is the 
        team leader's name, i.e. A.  Subsequent unique substrings are 
        friends of A or friends of friends of A, in ASCII order
        and excluding the team leader's name (i.e. A only appears
        as the first substring)

    Notes:
    - Team is drawn from only within two circles of A -- friends of A, plus 
      their immediate friends only
    """
    assert person in my_dir
    label = person

    # ------------ BEGIN YOUR CODE ------------

    list = []
    for lvl1Friend in my_dir[person]:
        if lvl1Friend not in list:
            list.append(lvl1Friend)
        for lvl2Friend in my_dir[lvl1Friend]:
            if lvl2Friend not in list:
                list.append(lvl2Friend)
    list = sorted(list)
    if person in list:
        list.remove(person)
        list.insert(0, person)
    else:
        list.insert(0, person)
    label = '_'.join(list)
    label = str(label)
    print(label)


    # ------------ END YOUR CODE ------------

    return label


def find_smallest_team(my_dir):
    """Find team with smallest size, and return its roster label str
    - if ties, return the team roster label that is first in ASCII order
    """
    smallest_teams = []

    # ------------ BEGIN YOUR CODE

    allteams = []
    for teamleader in my_dir.keys():
        list = []
        for lvl1Friend in my_dir[teamleader]:
            if lvl1Friend not in list:
                list.append(lvl1Friend)
            for lvl2Friend in my_dir[lvl1Friend]:
                if lvl2Friend not in list:
                    list.append(lvl2Friend)
        list = sorted(list)
        if teamleader in list:
            list.remove(teamleader)
            list.insert(0, teamleader)
        else:
            list.insert(0, teamleader)
        teamsize = str(len(list))
        list.insert(0, teamsize)
        allteams.append(list)
        allteams.sort()
        teamstied = []
        for i in allteams:
            if i[0] == allteams[0][0]:
                teamstied.append(i)
        teamstied.sort()
        teamsmallest = []
        for team in teamstied:
            teamsmallest.append(team[1:len(team) + 1])
        smallest_teams = []
    for team in teamsmallest:
        team = '_'.join(team)
        smallest_teams.append(team)

    
    # ------------ END YOUR CODE

    return smallest_teams[0] if smallest_teams else ""



if __name__ == '__main__':
    # To run and examine your function calls

    print('\n1. run load_pairs')
    my_pairs = load_pairs('../HW1/myfriends.txt')
    print(my_pairs)

    print('\n2. run make_friends_directory')
    my_dir = make_friends_directory(my_pairs)
    print(my_dir) 

    print('\n3. run find_all_number_of_friends')
    print(find_all_number_of_friends(my_dir))

    print('\n4. run make_team_roster')
    my_person = 'DARTHVADER'   # test with this person as team leader
    team_roster = make_team_roster(my_person, my_dir)
    print(team_roster) 

    print('\n5. run find_smallest_team')
    print(find_smallest_team(my_dir))

    print('\n6. run Friends iterator')
    friends_iterator = Friends(my_dir)
    for num, pair in enumerate(friends_iterator):
        print(num, pair)
        if num == 10:
            break
    # since index 0 we read 11 elements
    print(len(list(friends_iterator)) + num + 1)
