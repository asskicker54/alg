from Graph import Vertex, Graph

def reverse_graph(graph):
    rev_graph = Graph()

    for vert in graph:
        for neighbour in vert.getConnections():
            rev_graph.addEdge(neighbour.getId(), vert.getId())
    
    return rev_graph

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(2, 1)
graph.addEdge(1, 3)

print("Исходный:")
for vert in graph:
	for neighbor in vert.getConnections():
		print("( %s, %s )" % (vert.getId(), neighbor.getId()))

reversed_graph = reverse_graph(graph)

print("Обращенный:")
for vert in reversed_graph:
	for neighbor in vert.getConnections():
		print("( %s, %s )" % (vert.getId(), neighbor.getId()))