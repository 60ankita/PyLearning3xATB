set1 = (["the test", "for", "the test."])
print(len(set1))

for i in set1:
    print(i)

set1 = set([1,2,3,4,5,6,7,8,9,10,11,12])
print(len(set1))
set1.remove(5)
print(len(set1))
# remove first item
set1.pop()
print(set1)