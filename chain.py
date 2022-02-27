import copy
import functools
import sys

# code that takes a wordle graph as input and spits out the longest chain
#
maxlength = 0
graph = {}
components = {}
rcmap = {}
sys.setrecursionlimit(1500)

def init(G):
    global graph, components, rcmap, maxlength
    maxlength = 0
    graph = G
    components = scc(G.keys())
    for k, vs in enumerate(components):
        for v in vs:
            rcmap[v] = k


def longestChain(mask, cl, ml):
    # Longest chain that can be formed on the graph with vertices in mask
    global graph

    # Early termination
    if len(mask) == 0 or cl + len(mask) <= ml:
        return []

    retchain = []
    for m in mask:
        child = [m] + longestChain(mask & graph[m], cl+1, ml)
        if cl + len(child) > ml:
            retchain = child
            ml = cl + len(child)

    return retchain


def lChain(mask, currchain):
    # Longest chain that can be formed on the graph with vertices in mask
    global graph, maxlength

    # Early termination
    if len(mask) == 0 or len(currchain) + len(mask) <= maxlength:
        return []

    retchain = []
    for m in mask:
        child = lChain(mask & graph[m], currchain + [m])
        if len(child) + len(currchain) > maxlength:
            retchain = currchain + child
            maxlength = len(retchain)

    return retchain


def lain(mask, cl, ml):
    # Longest chain that can be formed on the graph with vertices in mask
    global graph, rcmap

    # Early termination
    if len(mask) == 0 or cl + len(mask) <= ml:
        return []

    retchain = []

    # separate the components of mask into topologically sorted stuff
    splitmask = {}
    for m in mask:
        curr = splitmask.get(rcmap[m], [])
        splitmask[rcmap[m]] = curr + [m]

    comps = list(splitmask.keys())
    comps.sort()

    for c in comps:
        runner = set()
        for m in splitmask[c]:
            child = [m] + lain(mask & graph[m] - runner, cl+1, ml)
            if cl + len(child) > ml:
                retchain = child
                ml = cl + len(child)
            runner.add(m)

    return retchain


def dfs(v, component, visited, G):

    visited[v] = True
    component.add(v)

    for n in G[v]:
        if n not in visited:
            dfs(n, component, visited, G)


def fillOrder(v, visited, stack):
    global graph

    visited[v] = True
    for n in graph[v]:
        if n not in visited:
            fillOrder(n, visited, stack)
    stack.append(v)


def reverseGraph():
    global graph

    rG = {v: set() for v in graph}
    for vertex, neighbors in graph.items():
        for n in neighbors:
            rG[n].add(vertex)

    return rG


def scc(vertices):
    stack = []
    visited = {}

    for v in vertices:
        if v not in visited:
            fillOrder(v, visited, stack)

    rG = reverseGraph()
    visited = {}
    components = []

    while stack:
        v = stack.pop()
        if v not in visited:
            component = set()
            dfs(v, component, visited, rG)
            components.append(component)

    return components


def cliques(G, cs):

    if len(G) == 0 or cs + len(G) < 10:
        return [[]]

    first = list(G.keys())[0]
    Gnbrs = {x: G[x] for x in G[first] if x in G}
    nCliques = cliques(Gnbrs, cs+1)
    nCliques = [[first]+x for x in nCliques]

    Gminus = copy.deepcopy(G)
    Gminus.pop(first)
    mCliques = cliques(Gminus, cs)

    return nCliques + mCliques


def clmask(mask, clique):
    global graph

    return functools.reduce(lambda a, b: a & graph[b], clique, mask)


def fchain(mask, cnum, cl):
    global graph, components, rcmap, maxlength

    # Early termination
    if len(mask) == 0 or cl + len(mask) <= maxlength:
        return []

    cmask = mask & components[cnum]
    subg = {x: graph[x] for x in cmask}
    cls = cliques(subg, 0)
    retchain = []
    for clique in cls:
        # new mask is intersection(mask, clique), remove all vertices from current component
        nmask = clmask(mask, clique) - cmask
        childcomponents = {rcmap[x] for x in nmask}
        retchain1 = []
        for childcomponent in childcomponents:
            childchain = clique + fchain(nmask, childcomponent, cl+len(clique))
            if cl + len(childchain) > maxlength:
                retchain1 = childchain
                maxlength = cl + len(childchain)

        if len(retchain1):
            retchain = retchain1

    return retchain

# given a graph
# perform dfs and break it into SCCs which are topologically sorted.
# list of sorted SCCs, with each one being a set(?)
#
# chain(mask, SCC, cl, ml)
# 	smask = SCC & mask
# 	for cliques in smask:
# 		chain(mask & masks(clique), SCC+1, cl+len(clique))


