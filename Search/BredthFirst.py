from collections import deque
__author__ = 'figarrido'


def BFS(G, s):
    for v in G:
        v.explored = False

    nodes = deque([s])

    def loop():
        global nodes
        while nodes:
            current = nodes.popleft()
            current.explored = True

            for adj in current.edges:
                if not adj.explored:
                    nodes.append(adj)

    loop()
