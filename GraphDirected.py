__author__ = 'figarrido'
from time import time


class Vertex:
    V = []

    def __init__(self, label):
        self.label = label
        self.adjacent_list = []
        Vertex.V += [self]

    def addEdge(self, edge):
        self.adjacent_list += [edge]

    @property
    def edges(self):
        return self.adjacent_list

    @edges.setter
    def edges(self, other):
        self.adjacent_list = other

    def __eq__(self, other):
        return self.label == other.label

    def __str__(self):
        return str(self.label)

    def __hash__(self):
        return id(self)

    @staticmethod
    def index(value):
        for i in range(len(Vertex.V)):
            if Vertex.V[i].label == value:
                return i
        return None


class Edge:
    E = []

    def __init__(self, origen, target, weight):
        self._origen = origen
        self._target = target
        self._weight = weight

        Edge.E += [self]

    @property
    def origen(self):
        return self._origen

    @origen.setter
    def origen(self, other):
        self._origen = other

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, other):
        self._target = other

    @property
    def weight(self):
        return self._weight

    @property
    def vertices(self):
        return self._origen, self._target

    def __eq__(self, other):
        return self._origen == other.origen and self._target == other.target

    def __str__(self):
        return "{} -({})> {}".format(self._origen, self._weight, self._target)


def cargarGrafo(filename, sep='\t'):
    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            info = line.strip().split(sep)
            v = Vertex(int(info[0]))
            v.aux = []
            for i in info[1:]:
                x, y = i.split(',')
                v.aux += [(int(x), int(y))]
            line = file.readline()


    for v in Vertex.V:
        v.aux = getattr(v, 'aux', [])
        for e in v.aux:
            i = Vertex.index(e[0])
            u = Vertex.V[i] if i is not None else Vertex(e[0])
            v.addEdge(Edge(v, u, e[1]))
        del v.aux

    print('VERTICES CARGADOS', len(Vertex.V))
    print('ARISTAS CARGADAS', len(Edge.E))
    print('-' * 20, end='\n\n')

    return Vertex.V
