def work(listduples):
    directory = dict()
    for duple in listduples:
        for name in duple:
            if name not in directory.keys() and name is duple[0]:
                list = []
                list.append(duple[1])
                directory[name] = list
            elif name not in directory.keys() and name is duple[1]:
                list = []
                list.append(duple[0])
                directory[name] = list
            elif name in directory.keys() and name is duple[0]:(
                    directory[name].append(duple[1]))
            elif name in directory.keys() and name is duple[1]:(
                    directory[name].append(duple[0]))
            print(directory)


listduples = [['Tom', 'Jerry'], ['Tim', 'Bo'], ['Tom', 'Bo']]
work(listduples)
