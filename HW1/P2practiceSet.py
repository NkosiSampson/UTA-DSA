def work(listduples):
    directory = dict()
    for duple in listduples:
        for name in duple:
            if name not in directory.keys() and name is duple[0]:
                myset = set()
                myset.add(duple[1])
                directory[name] = myset
            elif name not in directory.keys() and name is duple[1]:
                myset = set()
                myset.add(duple[0])
                directory[name] = myset
            elif name in directory.keys() and name is duple[0]:(
                    directory[name].add(duple[1]))
            elif name in directory.keys() and name is duple[1]:(
                    directory[name].add(duple[0]))
            print(directory)


listduples = [['Tom', 'Jerry'], ['Tim', 'Bo'], ['Tom', 'Bo']]
work(listduples)


