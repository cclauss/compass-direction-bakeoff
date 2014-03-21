# current source is at https://github.com/cclauss/compass-direction-bakeoff
# started from http://omz-forums.appspot.com/pythonista/post/5268418009759744

import collections

def compass_dir_0(x):
    if x >= 340 or x <= 20:
        return 'N'
    elif x > 20  and x < 70:
        return 'NE'
    elif x >= 70 and x <= 110:
        return 'E'
    elif x > 110 and x < 160:
        return 'SE'
    elif x >= 160 and x <= 200:
        return 'S'
    elif x < 250 and x > 200:
        return 'SW'
    elif x >= 250 and x <= 290:
        return 'W'
    else:
        return 'NW'

COMPASS = 'N NE E SE S SW W NW N'.split()  # list
def compass_dir_1(degrees):
    return COMPASS[int((degrees+22.5)/45)]

COMPASSV = 'NN SSS N'
COMPASSH = ' EEE WWW'
def compass_dir_2(degrees):
    octant = int((degrees+22.5)/45) % 8
    return (COMPASSV[octant] + COMPASSH[octant]).strip()

def compass_dir_3(x):
    compass = ['N', 'NE', 'E', 'SE',  'S', 'SW',  'W', 'NW', 'N'     ]
    angles  = [-20,   20,  70,  110,  160,  200,  250,  290, 340, 380]
    i = 0
    while i<len(compass):
        if i%2==0:   # Index is even
            if angles[i] <= x <= angles[i+1]:
                return compass[i]
        else:        # Index is odd
            if angles[i] < x < angles[i+1]:
                return compass[i]
        i = i + 1
    return "Error"

def compass_dir_4(x = 0):
    if x >= 340 or x <= 20:
        return 'N'
    elif 20 < x < 70:  # optimization for 20 < x and x < 70
        return 'NE'
    elif 70 <= x <= 110:
        return 'E'
    elif 110 < x < 160:
        return 'SE'
    elif 160 <= x <= 200:
        return 'S'
    elif 200 < x < 250:
        return 'SW'
    elif 250 <= x <= 290:
        return 'W'
    else:
        return 'NW'

def compass_dir_5(x = 0):
    if x >= 340 or x <= 20:
        return 'N'
    if x < 70:  # no elifs
        return 'NE'
    if x <= 110:
        return 'E'
    if x < 160:
        return 'SE'
    if x <= 200:
        return 'S'
    if x < 250:
        return 'SW'
    if x <= 290:
        return 'W'
    else:
        return 'NW'

def compass_dir_6(x = 0):
    if x >= 340:
        return 'N'
    direction_dict = collections.OrderedDict([
        ( 21, 'N'),
        ( 70, 'NE'),
        (111, 'E'),
        (160, 'SE'),
        (201, 'S'),
        (250, 'SW'),
        (291, 'W'),
        (340, 'NW') ])
    for i in direction_dict.keys():
        if x < i:
            return direction_dict[i]

def bakeoff(i):
    print(i, compass_dir_0(i), compass_dir_1(i),
             compass_dir_2(i), compass_dir_3(i),
             compass_dir_4(i), compass_dir_5(i), compass_dir_6(i))
    assert (compass_dir_0(i) == compass_dir_1(i) ==
            compass_dir_2(i) == compass_dir_3(i) ==
            compass_dir_4(i) == compass_dir_5(i) == compass_dir_6(i))

for angle_in_degrees in range(360):
    bakeoff(angle_in_degrees)

# optional negative user testing
bakeoff(20.9)
bakeoff(-1)
bakeoff(10000)
bakeoff('a')
