import json

f = open('sample-date.json', 'r')
text = f.read()
sample_date = json.loads(text)

for i in sample_date['imdata']:
    if i['l1PhysIf']['attributes']['id'] >= 'eth1/33' and i['l1PhysIf']['attributes']['id'] <= 'eth1/35':
        print("DN:", i['l1PhysIf']['attributes']['dn'], "  Speed:", i['l1PhysIf']['attributes']['speed'], "  MTU:", i['l1PhysIf']['attributes']['mtu'])

"""
print()
for i in sample_date['imdata']:
    print("DN:", i['l1PhysIf']['attributes']['id'], "  Speed:", i['l1PhysIf']['attributes']['speed'], "  MTU:", i['l1PhysIf']['attributes']['mtu'])
"""