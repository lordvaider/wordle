import copy
from collections import Counter

words = open(r"C:\Users\Admin\Desktop\wordle.txt", "r").read().splitlines()
#words = words[:500]
#secret = 'ABACK'
#words.remove(secret)

N = len(words)


def cliques(G):

    if len(G) == 0:
        return [[]]

    first = list(G.keys())[0]
    Gnbrs = {x: G[x] for x in G[first] if x in G}
    nCliques = cliques(Gnbrs)
    nCliques = [[first]+x for x in nCliques]

    Gminus = copy.deepcopy(G)
    Gminus.pop(first)
    mCliques = cliques(Gminus)

    return nCliques + mCliques


def green(g, s):
    return [ii for ii in range(5) if g[ii] == s[ii]]


def yellow2(g, s, Green):
    nGreen = {0, 1, 2, 3, 4} - set(Green)
    sWG = [s[i] for i in nGreen]
    Y = []
    for i in nGreen:
        if g[i] in sWG:
            Y.append(i)
            sWG.remove(g[i])

    return Y


def yellow(g, s, Green):
    secretWG = [x for ii, x in enumerate(s) if ii not in Green]

    Y = []
    for ii, x in enumerate(g):
        if ii not in Green and x in secretWG:
            Y.append(ii)
            secretWG.remove(x)

    return Y


def gyb(g, s):
    G = green(g, s)
    Y = yellow(g, s, G)

    return G, Y


def longestChain(chain, candidates, ml):
    global leafnodes
    # curr = chain[-1]
    # candidatesnew = candidates & P[curr]
    retChain = chain
    l = len(chain)

    # terminate early if there is already a chain with the max length achievable in this branch
    if len(candidates) == 0 or len(chain) + len(candidates) <= ml:
        leafnodes = leafnodes + 1
        return chain

    candidatesnew = [(c, candidates & P[c]) for c in candidates]
    candidatesnew.sort(key=lambda x:len(x[1]))
    for c in candidatesnew:
        newchain = longestChain(chain+[c[0]], c[1], ml)
        if len(newchain) > l:
            retChain = newchain
            l = len(newchain)
            ml = l

    return retChain


# lchain = []
# ml = 0
# for i in range(N):
#     if i%20 == 0:
#         print('Solving for chain starting with word: ', words[i], ', no:', i)
#     cnd = P[i]
#     schain = longestChain([i], cnd, ml)
#     if len(schain) > ml:
#         lchain = schain
#         ml = len(schain)
#         print('found chain with length', ml)
#         print('the chain is:', lchain)
#


