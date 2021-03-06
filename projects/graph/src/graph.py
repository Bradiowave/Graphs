#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        self.vertices.update({label: set()})

    def add_edge(self, start, end, bidirectional = True):
        if start not in self.vertices:
            raise Exception(f'{start} not a vertex')
        if end not in self.vertices:
            raise Exception(f'{end} not a vertex')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start=None, algo='breadth'):
        if not start:
            start = list(self.vertices.keys())[0]

        queue = list(start)
        visited = set()
        order = []

        while queue:
            if algo == 'breadth':
                current_vert = queue.pop(0)
            elif algo == 'depth':
                current_vert = queue.pop()
            visited.add(current_vert)
            order.append(current_vert)
            for child in self.vertices[current_vert]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)

        return order
