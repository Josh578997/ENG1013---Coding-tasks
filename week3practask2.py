pollData = ['Western Food','Halal','Sushi','Mexican Food','Finger Food','Vegetarian',
            'Vegetarian','Pizza','Finger Food','Malaysian Food','Malaysian Food','Western Food',
            'Sushi','Indonesian Food','Vegetarian','Finger Food','Malaysian Food','Halal',
            'Western Food','Finger Food','Pizza','Mexican Food','Halal','Indonesian Food',
            'Australian Food','Pizza','Chinese Food','Chinese Food', 'Indonesian Food',
             'Vegetarian','Malaysian Food','Indonesian Food','Greek Food','Greek Food', 'Australian Food',
             'Australian Food','Australian Food','Chinese Food','Halal','Western Food',
             'Halal','Finger Food']

preflist = []
typelist = []
for i in range(len(pollData)-1):
    food = pollData[i]
    count = 0
    if food not in pollData[:i]:
        for j in range(len(pollData)-1):
            if pollData[j] == food:
                count += 1
        preflist.append(count)
        typelist.append(pollData[i])

max = preflist[0]
for i in preflist:
    if i > max:
        max = i

dict = {}
for j,k in zip(preflist,typelist):
    dict[j] = k

print(dict[max])