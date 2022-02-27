words = open(r"C:\Users\Admin\Desktop\wordle.txt", "r").read().splitlines()


masks = [
    [1, 2, 3, 4],
    [0, 2, 3, 4],
    [0, 1, 3, 4],
    [0, 1, 2, 4],
    [0, 1, 2, 3],
]
cand = []

for m in masks:
    clusters = {}
    for w in words:
        hash = ''.join([w[i] for i in m])
        arr = clusters.get(hash, [])
        clusters[hash] = arr + [w]

    c = [(x, len(y)) for x, y in clusters.items() if len(y) > 5]
    c.sort(key=lambda x: x[1], reverse=True)
    for cc in c:
        cand = cand + clusters[cc[0]]


print(cand)
# clusters = {}
#
# for w in words:
#     hash = len({w[i] for i in range(5)})
#     arr = clusters.get(hash, [])
#     clusters[hash] = arr + [w]
#
# c = [(x, len(y)) for x, y in clusters.items()]
# c.sort(key=lambda x: x[1], reverse=True)


print('v')
