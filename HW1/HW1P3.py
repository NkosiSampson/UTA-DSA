from operator import itemgetter
def find_all_number_of_friends(dir):
#listofnames = []
#duple = []
#for name in directory.keys():
    #duple.append(name)
    #numfriends = len(directory[name])
    #duple.append(numfriends)
#listofnames.append(duple)
#listofnames = sorted(listofnames)
#print(listofnames)

    friends_list = []

# ------------ BEGIN YOUR CODE ------------

    for name in dir.keys():
            duple = []
            duple.append(name)
            numfriends = len(dir[name])
            duple.append(numfriends)
            friends_list.append(tuple(duple))
            friends_list = sorted(friends_list, key = itemgetter(1), reverse = True)
    friends_list = sorted(friends_list, key = itemgetter(0))

# ------------ END YOUR CODE ------------

    print(friends_list)
directory = {'CHEWBACCA': {'C-3PO', 'LUKE', 'Yoda', 'Dave'}, 'Ron': {'CHEWBACCA', 'C-3PO', 'BERU'},
 'Luke': {'Yoda', 'Darth Vader', 'Darth Maul'}}
simple_dir = {'CHEWBACCA': {'HAN', 'LUKE'}, 'HAN': {'CHEWBACCA', 'LEIA'},
                'LUKE': {'CHEWBACCA'}, 'LEIA': {'HAN'}}
find_all_number_of_friends(simple_dir)








