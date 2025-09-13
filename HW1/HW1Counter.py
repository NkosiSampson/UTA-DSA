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
list = [['Tom', 'Jerry'], ['Tim', 'Bo'], ['Tom', 'Bo']]
for duple in list:
    for name in duple:
        if name not in directory.keys():
            directory[name] = 1
        elif name in directory.keys():
            directory[name] += 1
print(directory)



    # ------------ END YOUR CODE ------------

  #  return directory