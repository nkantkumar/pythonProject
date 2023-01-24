from collections import defaultdict

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(float)
for word in words:
    d[word] += 1

print(d)



d = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
keys = d.keys()
print(keys)


keys = sorted(keys)
print(keys)


for key in keys:
    print(key, d[key])