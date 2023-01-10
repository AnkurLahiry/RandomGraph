from RandomGraph import RandomGraph

if __name__ == "__main__":
    number_of_nodes = 10
    probability = 0.35
    print("Creating a random graph for nodes: ", number_of_nodes)
    print("The probability we take: ", probability)
    graph = RandomGraph(number_of_nodes=number_of_nodes, probability=probability)
    graph.create_graph()
    graph.print_graph()