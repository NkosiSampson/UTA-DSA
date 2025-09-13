directory = {'CHEWBACCA': {'Ron', 'LUKE', 'Yoda', 'Dave', 'Pam'}, 'Ron': {'CHEWBACCA', 'BERU'},
 'LUKE': {'Yoda'}, 'Dave': {'BERU'}, 'BERU': {'CHEWBACCA'}, 'Alice': {}, 'Pam': {}, 'Aaragon': {}, 'Yoda': {'CHEWBACCA', 'BERU'}}

allteams = []
metalist = []
for teamleader in directory.keys():
    list = []
    for lvl1Friend in directory[teamleader]:
        if lvl1Friend not in list:
            list.append(lvl1Friend)
        for lvl2Friend in directory[lvl1Friend]:
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
        teamsmallest.append(team[1:len(team)+1])
    smallest_teams = []
for team in teamsmallest:
    team = '_'.join(team)
    smallest_teams.append(team)







#smallest_teams = str(smallest_teams)
smallest_teams = smallest_teams[0]
print(smallest_teams)


#string = '_'.join(teamsmallest)
#string = str(string)
#print(string[0])

    # list.insert(0, str(len(list)))