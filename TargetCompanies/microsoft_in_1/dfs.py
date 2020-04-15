# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end = " ")
        visited.add(node)
        for depth_node in graph[node]:
            dfs(visited, graph, depth_node)

dfs(visited, graph, 'A')