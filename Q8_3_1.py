import collections
data = 'すもももももももものうち'
count = collections.Counter(data)
[v[0] for v in count.items() if v[1] == 1]
print(data)
