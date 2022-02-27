import time
import graph
import chain
import sys
import random
print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())

words = open(r"C:\Users\Admin\Desktop\wordle.txt", "r").read().splitlines()
# words = [w for w in words if w[-2:] == 'LY']

def fetchGraph(secret):
    G = graph.readFromFile2(secret)
    G = {x: y - {secret} for x, y in G.items()}

    return G

wordmap = {}
# secrets = ['BOUND', 'FOUND', 'HOUND', 'MOUND', 'POUND', 'ROUND', 'SOUND', 'WOUND', 'COWER', 'LOWER', 'MOWER', 'POWER',
#            'ROWER', 'SOWER', 'TOWER', 'BATCH', 'CATCH', 'HATCH', 'LATCH', 'MATCH', 'PATCH', 'WATCH']
secrets = [
    'EIGHT', 'FIGHT', 'LIGHT', 'MIGHT', 'NIGHT', 'RIGHT', 'SIGHT', 'TIGHT', 'WIGHT',
    'BOUND', 'FOUND', 'HOUND', 'MOUND', 'POUND', 'ROUND', 'SOUND', 'WOUND',
    'BATCH', 'CATCH', 'HATCH', 'LATCH', 'MATCH', 'PATCH', 'WATCH',
#    'COWER', 'LOWER', 'MOWER', 'POWER', 'ROWER', 'SOWER', 'TOWER',
    'BASTE', 'CASTE', 'HASTE', 'PASTE', 'TASTE', 'WASTE',
    'BATTY', 'CATTY', 'FATTY', 'PATTY', 'RATTY', 'TATTY',
    'BILLY', 'DILLY', 'FILLY', 'HILLY', 'SILLY', 'WILLY',
    'DAUNT', 'GAUNT', 'HAUNT', 'JAUNT', 'TAUNT', 'VAUNT',
    'SCORE', 'SHORE', 'SNORE', 'SPORE', 'STORE', 'SWORE',
    'SHADE', 'SHAKE', 'SHALE', 'SHAME', 'SHAPE', 'SHARE', 'SHAVE',
    'GRACE', 'GRADE', 'GRAPE', 'GRATE', 'GRAVE', 'GRAZE',
    'STAGE', 'STAKE', 'STALE', 'STARE', 'STATE', 'STAVE'
]

for secret in secrets:
    # random.graphProfiling(secret)
    print('the secret word is', secret)
    G = graph.quickGraph(secret, words)
    chain.init(G)
    l = 13
    tic = time.perf_counter()
    for w in words:
        # c = chain.longestChain(G[w], 1, l)
        c = chain.lain(G[w], 1, l)
    #    print('v')
        if len(c) > l:
            #wordmap[secret] = c
            l = len(c)
            print('the longest chain so far is', [w] + c)
            print('the length of this chain is', l)

        toc = time.perf_counter()
        if (toc - tic) > 30:
            print('5 seconds have passed, currently at word:', w)
            tic = time.perf_counter()


print(wordmap)