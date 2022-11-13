from Graph import Graph, Vertex

graph = Graph()
graph.addEdge("3/4 cup milk", "1 cup mix")
graph.addEdge("1 egg", "1 cup mix")
graph.addEdge("1 oil", "1 cup mix")
graph.addEdge("1 cup mix", "pour 1/4 cup")
graph.addEdge("1 cup mix", "heat syrup")
graph.addEdge("heat griddle", "pour 1/4 cup")
graph.addEdge("pour 1/4 cup", "turn when bubbly")
graph.addEdge("turn when bubbly", "eat")
graph.addEdge("heat syrup", "eat")

def DFS(graph):
    visited = {}
    unvisited_vert = list(graph.getVertices())
    for vert in unvisited_vert:
        visited[vert] = False
    s = []

    for vert in unvisited_vert:
        if visited[vert] == False:
            DFS_Util(vert, visited, s)
    print(s)

def DFS_Util(vert, visited, s):
    visited[vert] = True

    neighbors = []
    for neighbor in graph.getVertex(vert).getConnections():
        neighbors.append(neighbor.getId())

    for neighbor in neighbors:
        if visited[neighbor] == False:
            DFS_Util(neighbor, visited, s)
    s.insert(0, vert)


DFS(graph)