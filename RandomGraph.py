import random

class RandomGraph:

    adjacency_list = dict()

    def __init__(self, number_of_nodes, probability):
        self.number_of_nodes = number_of_nodes
        self.probability = probability

    def create_graph(self):
        for i in range(1, self.number_of_nodes + 1):
            for j in range(1, self.number_of_nodes + 1):
                # skipping the probability of being self loop
                if i == j:
                    continue
                if j in self.adjacency_list:
                    list = self.adjacency_list[j]
                    if i in list:
                        continue
                if i in self.adjacency_list:
                    list = self.adjacency_list[i]
                    if j in list:
                        continue
                # add your random function here what you wish
                loop_probability = random.random()
                if loop_probability >= self.probability:
                    self._add_edge_(i, j)
                    self._add_edge_(j, i)

    def _add_edge_(self, source, destination):
        if source in self.adjacency_list:
            edges = self.adjacency_list[source]
            edges.add(destination)
            self.adjacency_list[source] = edges
        else:
            edges = set()
            edges.add(destination)
            self.adjacency_list[source] = edges

    def print_graph(self):
        print(self.adjacency_list)