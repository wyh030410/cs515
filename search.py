def dfs(graph):
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)

    visited = set()

    while len(visited) < len(all_nodes):
        unvisited = sorted([node for node in all_nodes if node not in visited])
        if not unvisited:
            break

        stack = [unvisited[0]]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)
                neighbors = graph.get(node, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)

def bfs(graph):
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)

    visited = set()

    while len(visited) < len(all_nodes):
        unvisited = sorted([node for node in all_nodes if node not in visited])
        if not unvisited:
            break

        queue = [unvisited[0]]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node)
                visited.add(node)
                neighbors = graph.get(node, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)