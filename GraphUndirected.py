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
1	2	3
2	1	3	4
3	1	2	4
4	2	3


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

    def add_edge(self, edge):
        self.adjacent_list += [edge]

    def __eq__(self, other):
        return self.label == other.label

    def __str__(self):
        return str(self.label)


class Edge:
    E = []

    def __init__(self, u, v):
        self.v = v
        self.u = u

        if self not in Edge.E:
            Edge.E += [self]

    def contain(self, vertex):
        if self.u == vertex or self.v == vertex:
            return True
        return False

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

    for v in info:
        data = v.split(sep)
        label = int(data[0])
        u = Vertex(label)
        [Edge(u, Vertex(int(i))) for i in data[1:]]

    for v in Vertex.V:
        for e in Edge.E:
            if e.contain(v):
                v.add_edge(e)

    return Vertex.V, Edge.E
