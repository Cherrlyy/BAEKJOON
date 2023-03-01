from datetime import datetime

red = set()
blue = set()
all = []
times = []

for i in range(8):
    time = input().split()
    time[0] = datetime.strptime(time[0], '%M:%S:%f')
    all.append(time)
    times.append(time[0])


times.sort()
for i in range(len(all)):
    for h in range(len(times)):
        if all[i][0] == times[h]:
            if all[i][1] == 'R':
                red.add(h)
            else:
                blue.add(h)

scores = {0: 10, 1: 8, 2:6, 3:5, 4:4, 5:3, 6:2, 7:1}

red_score = 0
for i in red:
    red_score += scores[i]

blue_score = 0
for i in blue:
    blue_score += scores[i]

if red_score > blue_score:
    print('Red')
elif red_score < blue_score:
    print('Blue')
else:
    if 0 in red:
        print('Red')
    else:
        print('Blue')
