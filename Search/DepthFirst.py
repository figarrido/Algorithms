__author__ = 'figarrido'


def DFS(G, s):
    for v in G:
        v.explored = False

    def loop(s):
        s.explored = True
        for adj in s.edges:
            if not adj.explored:
                loop(adj)

    loop(s)
