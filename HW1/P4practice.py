directory = {'CHEWBACCA': ['Ron', 'LUKE', 'Yoda', 'Dave', 'Pam'], 'Ron': ['CHEWBACCA', 'BERU'],
 'LUKE': ['Yoda'], 'Dave': [ 'BERU'], 'BERU': [ 'CHEWBACCA'], 'Yoda': [ 'CHEWBACCA', 'BERU'], 'Pam': []}

dir = {}

for teamleader in directory.keys():
    list = []
    list.append(teamleader)
    for lvl1Friend in directory[teamleader]:
        if lvl1Friend not in list:
            list.append(lvl1Friend)
        for lvl2Friend in directory[lvl1Friend]:
            if lvl2Friend not in list:
                list.append(lvl2Friend)
    string = '_'.join(list)
    string = str(string)
    print(string)