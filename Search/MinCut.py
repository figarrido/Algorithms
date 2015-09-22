from GraphUndirected import cargarGrafo, limpiar
from random import choice


def printG(G):
    for v in G[0]:
        print("Vértice:", v, "N° edges:", len(v.edges))
        for e in v.edges:
            print(e)
        print()


def replaceVertex(V, E, edge):
    u, v = edge.vertices
    E = list(filter(lambda x: x != edge, E))
    V = list(filter(lambda x: x != v, V))
    adjU = list(filter(lambda x: x != edge, u.edges))
    adjV = list(filter(lambda x: x != edge, v.edges))

    for e in adjV:
        if e.vertexA == v:
            e.vertexA = u
        else:
            e.vertexB = u

    u.edges = adjU + adjV
    return V, E


def minCut(V, E):
    while len(V) > 2:
        elected = choice(E)
        V, E = replaceVertex(V, E, elected)
    return V, E

corte = 10000000**10000
per = 0
for _ in range(1060):
    G = cargarGrafo('ejemplo2.txt')
    newG = minCut(*G)
    corte = min(len(newG[1]), corte)
    limpiar()
    if _ % 11 == 0:
        per += 1
        print(per, "%", sep='')

print("EL CORTE MINIMO TIENE:", corte, "ARISTAS")
