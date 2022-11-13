from Graph import Graph, Vertex

def dijkstra(graph, start):
	unvisited_nodes = list(graph.getVertices())
	shortest_path = {}
	prev_nodes = {}
	max_size = float("inf")

	for node in unvisited_nodes:
		shortest_path[node] = max_size

	shortest_path[start.getId()] = 0
	
	while unvisited_nodes:
		cur_min_node = None
		for node in unvisited_nodes:
			if cur_min_node == None:
				cur_min_node = node
			elif shortest_path[node] < shortest_path[cur_min_node]:
				cur_min_node = node
		
		neighbors = []
		for neighbor in graph.getVertex(cur_min_node).getConnections():
			neighbors.append(neighbor.getId())
		for neighbor in neighbors:
			n = graph.getVertex(neighbor)

			tentative_value = shortest_path[cur_min_node] + graph.getVertex(cur_min_node).getWeight(n)
			if tentative_value < shortest_path[neighbor]:
				shortest_path[neighbor] = tentative_value
				prev_nodes[neighbor] = cur_min_node
		unvisited_nodes.remove(cur_min_node)
	return prev_nodes, shortest_path

def print_result_path(prev_nodes, shortest_path, start_node, finish_node):
	path = []
	node = finish_node
	while node != start_node:
		path.append(node)
		node = prev_nodes[node]
	path.append(start_node)
	path.reverse()
	print("Лучший маршрут:", end=" ")
	print(" -> ".join(path))
	print("Расстояние:", shortest_path[finish_node])

graph = Graph()

graph.addEdge("Белово", "Ленинск-Кузнецкий", 31)
graph.addEdge("Ленинск-Кузнецкий", "Киселевск", 79)
graph.addEdge("Белово", "Киселевск", 51)
graph.addEdge("Белово", "Гурьевск", 28)
graph.addEdge("Гурьевск", "Киселевск", 55)
graph.addEdge("Ленинск-Кузнецкий", "Мыски", 150)
graph.addEdge("Киселевск", "Кемерово", 154)
graph.addEdge("Кемерово", "Новосибирск", 204)
graph.addEdge("Мыски", "Новосибирск", 348)

startNode = graph.getVertex("Белово")
endNode = graph.getVertex("Новосибирск")

prev_nodes, shortest_path = dijkstra(graph, startNode)
print_result_path(prev_nodes, shortest_path, startNode.getId(), endNode.getId())



