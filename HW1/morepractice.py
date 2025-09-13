friends_dir = {'CHEWBACCA': {'Ron', 'LUKE', 'Yoda', 'Dave', 'Pam'}, 'Ron': {'CHEWBACCA', 'BERU'},
 'LUKE': {'Yoda'}, 'Dave': {'BERU', 'Chewbacca'}, 'BERU': {'CHEWBACCA', 'Ron'}, 'Alice': {}, 'Pam': {'Chewbacca'}, 'Aaragon': {}, 'Yoda': {'CHEWBACCA', 'BERU'}}

"""Friends iterator class to return pairs of friends"""
#
# The code for the Friends class below contains a small number of bugs:
# Please find and correct them so that the class meets the specifications
# described in the handout and docstring
#

from typing import Tuple, Set, Dict, Iterator


class Friends(Iterator):
    """Make an iterator to return one unique relationship at a time from friends_dir

    Args:
        friends_dir: dictionary of persons and their friends that was
           constructed by make_friends_directory()

    Returns:
        Iterator type, yielding one pair (as a tuple) at a time in ASCII order

    Notes:
    - Return each tuple in ASCII order:
        ('a', 'b') before ('a','c') before ('b', 'c') etc
    - Return only unique pairs: i.e. if returned (x,y), then do not return (y,x)
    - Read about iterator/generator type in Python Standard Library docs
      https://docs.python.org/3/library/stdtypes.html#typeiter

    Hint:
        You should practice using your visual debugger (PyCharm) here to
        step through the code line by line, set breakpoints, and watch
        the values of local variables and attributes change.
    """

    # ------------ DEBUG CODE BELOW ------------

    def __init__(self, friends_dir: Dict[str, Set]):

        self.dir = friends_dir

        if friends_dir:
            # initially, `persons` is list of all keys;
            # and `friends` is list of the first person's friends
            self.persons = sorted(friends_dir.keys())
            self.friends = sorted(friends_dir[self.persons[0]])

        else:
            # handle edge case when input is an empty directory
            self.person = []

    def __iter__(self) -> Iterator:

        return self

    def __next__(self) -> Tuple[str, str]:

        if not self.persons:  # cannot iterate when already empty
            raise StopIteration
        #print(self.friends)
        while not self.friends:

            # try to move on to next person in `persons` list
            self.persons.pop(0)
            #print(self.persons)
            if not self.persons:  # stop iterating since there is no next person
                raise StopIteration

            # set `friends` to be list of friends of next person
            self.friends = sorted([s for s in self.dir[self.persons[0]]
                                   if s > self.persons[0]])
            #print(self.friends)

        # return the next friendship pair as a tuple
        front = self.friends[0] #added line
        print(self.persons[0], front) #changed self.friends.pop(0) to front
        return (self.persons[0], self.friends.pop(0))



    # ------------ END DEBUG ------------

#print('\n6. run Friends iterator')
friends_iterator = Friends(friends_dir)
for num, pair in enumerate(friends_iterator):
    print(num, pair)
    if num == 10:
        break
# since index 0 we read 11 elements
print(len(list(friends_iterator)) + num + 1)