import wordle
import graph
import time
import chain

# ret = wordle.gyb('KINKY', 'CYNIC')
# print(ret)
# print(str(ret))

words = open(r"C:\Users\Admin\Desktop\wordle.txt", "r").read().splitlines()


def bruteforceProfile(G):
    l = 0
    tic = time.perf_counter()

    for w in words:
        c = chain.longestChain(G[w], 1, 0)
        if len(c) > l:
            l = len(c)
            print('the longest chain so far is', [w] + c)

        toc = time.perf_counter()
        if (toc - tic) > 5:
            print('5 seconds have passed, currently at word:', w)
            tic = time.perf_counter()


def graphProfiling(secret):
    tic = time.perf_counter()
    G = graph.quickGraph(secret)
    toc = time.perf_counter()

    graph.saveToFile2(secret, G)
    print('Quick graph computed in', toc-tic, 'seconds')

    # tic = time.perf_counter()
    # G2 = graph.graph(secret)
    # toc = time.perf_counter()
    #
    # print('Graph computed in', toc-tic, 'seconds')
    #
    # for k, v in G.items():
    #     if v != G2[k]:
    #         print('The two graphs are unequal at', k)


#graphProfiling('GRAZE')
# G = graph.readFromFile2('SILLY')
# a = {3, 4, 6, 1, 57, 2, 22, 64, 81, 5}
#
# for x in a:
#     print(x)

print('v')