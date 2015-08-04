# -*- coding: utf-8 -*-
__author__ = 'figarrido'

"""
cargarGrafo:
Recibe el nombre del archivo donde está la información del grafo y el
separador de la información (por defecto es un tabulador). La información debe
estructurarse de la siguiente manera: cada linea representa un vértice, el
primer dato corresponde a la etiqueta del vértice y los siguientes son las
etiquetas de los vértices adjacentes.

Ejemplo de archivo:
1   2   3
2   1   3   4
3   1   2   4
4   2   3


cargarGrafo retorna:
(V, E)

donde cada vertice contiene las aristas a las que pertenece.

V = [Vertex(1), Vertex(2), Vertex(3), Vertex(4)]
E = [Edge(1, 2), Edge(1, 3), Edge(2, 3), Edge(2, 4), Edge(3, 4)]

Cada arista posee dos Vertex, cada uno con la etiqueta correspondiente.
"""


class Vertex:
    V = []

    def __init__(self, label):
        self.label = label
        self.adjacent_list = []

        if self not in Vertex.V:
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

    @staticmethod
    def index(value):
        for i in range(len(Vertex.V)):
            if Vertex.V[i].label == value:
                return i
        return -1


class Edge:
    E = []

    def __init__(self, u, v):
        self.u = u
        self.v = v

        if self not in Edge.E:
            Edge.E += [self]

    def _contain(self, vertex):
        return self.u == vertex or self.v == vertex

    def contain(self, vertex1, vertex2=None):
        if not vertex2:
            return self._contain(vertex1)
        else:
            return self._contain(vertex1) and self._contain(vertex2)

    @property
    def vertexA(self):
        return self.u

    @vertexA.setter
    def vertexA(self, other):
        self.u = other

    @property
    def vertexB(self):
        return self.v

    @vertexB.setter
    def vertexB(self, other):
        self.v = other

    @property
    def vertices(self):
        return self.u, self.v

    @property
    def isLoop(self):
        return self.u == self.v

    def __eq__(self, other):
        if self.u == other.u and self.v == other.v:
            return True
        if self.u == other.v and self.v == other.u:
            return True
        return False

    def __str__(self):
        return "[{0}, {1}]".format(self.u, self.v)


def cargarGrafo(filename, sep='\t'):
    with open(filename, "r") as file:
        info = file.readlines()
    info = [i.strip() for i in info]
    aristas = []
    for line in info:
        data = line.split(sep)
        label = int(data[0])
        u = Vertex(label)
        for i in data[1:]:
            if (label, int(i)) not in aristas\
                    and (int(i), label) not in aristas:
                aristas += [(label, int(i))]

    for a in aristas:
        for j in Vertex.V:
            if j.label == a[0]:
                u = j
            if j.label == a[1]:
                v = j
        e = Edge(u, v)
        u.addEdge(e)
        v.addEdge(e)

    return Vertex.V, Edge.E


def limpiar():
    Vertex.V.clear()
    Edge.E.clear()
