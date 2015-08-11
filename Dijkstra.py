from GraphDirected import cargarGrafo
__author__ = 'figarrido'


def dijkstra(V, s):
    length = {s.label: 0}
    seen = [s]

    while len(seen) != len(V):
        minWeight = 1000000**100000
        minE = None
        for v in seen:
            for e in v.edges:
                if e.origen in seen and e.target not in seen:
                    if length[v.label] + e.weight < minWeight:
                        minE = e
                        minWeight = length[v.label] + e.weight
        length[minE.target.label] = length[minE.origen.label] + minE.weight
        seen += [minE.target]

    return length

G = cargarGrafo('../dijkstraData.txt')

distance = dijkstra(G, G[0])
targets = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

for target in targets:
    print(str(target) + ':', distance[target])
