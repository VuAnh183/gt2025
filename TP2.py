# Find components of a graph which is represented by Adjacency matrix
# Behavior:
#  - Input: Graph represented by matrix 
#  - Output: Number of componenets both weak and strong 
# Suggestions: BFS and DFS algorithms
# Given graph matrix:
graph = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0], # (1,2) (1,4)
    [0, 0, 1, 0, 0, 1, 0, 0, 0], # (2,3) (2,6)
    [0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
    [0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
    [0, 0, 0, 1, 1, 0, 0, 0, 1], # (5,4) (5,5) (5,9)
    [0, 0, 1, 1, 0, 0, 0, 0, 0], # (6,3) (6,4)
    [0, 0, 1, 0, 1, 1, 0, 1, 0], # (7,3) (7,5) (7,6) (7,8)
    [0, 0, 1, 0, 0, 0, 0, 0, 1], # (8,3) (8,9)
    [0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
]

def count_components(directed_g):
    def dfs(i, c, g, visited):
        stack = [i]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                c.add(current + 1)
                to_extend = []
                for j in range(len(g[current])):
                    if g[current][j] == 1 and j not in visited:
                        to_extend.append(j)
                stack.extend(to_extend)

    undirected_g = [[1 if directed_g[i][j] or directed_g[j][i] else 0 for j in range(len(directed_g))] for i in
                    range(len(directed_g))]

    directed_visited = set()
    directed_components = []
    for i in range(len(directed_g)):
        if i not in directed_visited:
            component = set()
            dfs(i, component, directed_g, directed_visited)
            directed_components.append(component)

    undirected_visited = set()
    undirected_components = []
    for i in range(len(undirected_g)):
        if i not in undirected_visited:
            component = set()
            dfs(i, component, undirected_g, undirected_visited)
            undirected_components.append(component)

    return {"strong": directed_components, "weak": undirected_components}


if __name__ == '__main__':
  res = count_components(graph)
  print(res)
  