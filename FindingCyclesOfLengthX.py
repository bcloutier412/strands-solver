counter = 0
def find_x_length_cycles(graph, x):
    all_cycles = []

    def dfs(start, current, depth, path, visited):
        if depth == x:
            if start in graph[current]:
                path += [start]
                all_cycles.append(path)
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(start, neighbor, depth + 1, path + [neighbor], visited)
                visited.remove(neighbor)

    for vertex in graph:
        dfs(vertex, vertex, 1, [vertex], set({vertex}))

    return all_cycles
# Example usage:
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D', 'E', 'F', 'G'],
    'C': ['A', 'E', 'F', 'G'],
    'D': ['A', 'B', 'E', 'F'],
    'E': ['B', 'C', 'D', 'F', 'G'],
    'F': ['B', 'C', 'D', 'E', 'G'],
    'G': ['B', 'C', 'D', 'E', 'F']
}

x_length_cycles = find_x_length_cycles(graph, 5)
for cycle in x_length_cycles:
    print(cycle)
