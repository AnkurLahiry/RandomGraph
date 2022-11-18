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
                # add your random function here what you wish
                loop_probability = random.random()
                if loop_probability >= self.probability:
                    self.add_edge(i, j)

    def add_edge(self, source, destination):
        print("Will add edge in this function")