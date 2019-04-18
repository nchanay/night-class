#sock sorter

import random

slist = []
stypes = ['ankle', 'crew', 'calf', 'thigh']
scolors = ['black', 'white', 'blue']

# sdict = {"ankle": 0, "crew": 0, "calf": 0, "thigh": 0}
sdict = {}
for socks in range(100):
    item = random.choice(stypes)
    color = random.choice(scolors)
    slist.append((item, color))
    sdict[item, color] = sdict.get((item, color), 0) + 1

for sock in sdict:
    print(f"{sock} has {sdict.get(sock)%2} loner(s)")

for key, value in sdict.items():
    print(f"{key} has {sdict.get(key, value)%2} loner(s)")
