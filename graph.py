import wordle as wrdl
import re

# words = open(r"C:\Users\Admin\Desktop\wordle.txt", "r").read().splitlines()


def clueBuckets(secret, words):
    # bucket the words by which clues they generate

    clueBuckets = {}
    strclueMap = {}

    for w in words:
        clue = wrdl.gyb(w, secret)
        # clue = (set(G), len(Y))
        cluestr = str(clue)
        if cluestr in clueBuckets:
            clueBuckets[cluestr].append(w)
        else:
            clueBuckets[cluestr] = [w]
            strclueMap[cluestr] = clue

    return clueBuckets, strclueMap


def metaGraph(cb, scMap):
    # make a graph of connections between clueBuckets

    mg = {}

    for cs1 in cb.keys():
        mg[cs1] = set()
        G1, Y1 = scMap[cs1]
        for cs2 in cb.keys():
            G2, Y2 = scMap[cs2]
            if set(G1).issubset(set(G2)) and len(Y2) >= len(Y1) + len(G1) - len(G2):
                mg[cs1].add(cs2)

    return mg


def quickGraph(secret, words):
    # graph is a dict with keys = word indices, and values = sets of words they are connected to
    # words.remove(secret)

    graph = {}

    cb, scMap = clueBuckets(secret, words)
    mg = metaGraph(cb, scMap)
    for cs, bucket in cb.items():
        G, Y = scMap[cs]
        for w in bucket:
            graph[w] = set()
            for cs2 in mg[cs]:
                for x in cb[cs2]:
                    if G == wrdl.green(w, x) and Y == wrdl.yellow(w, x, G) and x != secret:
                        graph[w].add(x)

    return graph


def possV(guess, s):
    p = set()
    G, Y = wrdl.gyb(guess, s)
    for w in words:
        if G == wrdl.green(guess, w) and Y == wrdl.yellow(guess, w, G):
            p.add(w)

    return p


def graph(secret):
    return {g: possV(g, secret) for g in words}


def saveToFile(secret, G):
    file = open(r"C:\Users\Admin\Desktop\wordGraphs\{}.txt".format(secret), 'w')
    for k, v in G.items():
        file.write('{}:{}\n'.format(k, ', '.join(v)))


def readFromFile(secret):
    file = open(r"C:\Users\Admin\Desktop\wordGraphs\{}.txt".format(secret), 'r')
    G = {}

    for l in file.read().splitlines():
        x, y = re.findall('(.*):(.*)$', l)[0]
        G[x] = set([a for a in y.split(', ')])

    return G


def saveToFile2(secret, G):
    file = open(r"C:\Users\Admin\Desktop\wordGraphs\{}.txt".format(secret), 'w')
    file.write(str(G))


def readFromFile2(secret):
    file = open(r"C:\Users\Admin\Desktop\wordGraphs\{}.txt".format(secret), 'r')
    return eval(file.read())

