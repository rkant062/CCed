graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = []
queue = [] # Set to keep track of visited nodes.

def bfs(queue, graph, node):
        #print(node)
        #queue.append(node)
        visited.append(node)
        queue.append(node)

        while(len(queue) != 0 ):
            x = queue.pop(0)
            print(x, end = " ")
            for i in graph[x]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)


bfs(queue, graph, 'A')