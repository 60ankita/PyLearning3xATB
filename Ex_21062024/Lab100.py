my_dict = {'b': 2,'w': 5,'e':6}
print(my_dict)

for k,v in my_dict.items():
    print(k,v)

from collections import OrderedDict
od = OrderedDict()
od['b'] = 45
od['f'] = 78
print(od)

# Dict - it will not keep the order of insertion
# OrderDict - It will keep the order insertion
