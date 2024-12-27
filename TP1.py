edges = [
  (1, 2),
  (2, 5),
  (1, 5),
  (3, 6),
  (6, 4),
  (4, 7),
  (7, 6)
]

def create_graph(edges):
  graph ={}
  for start, end in edges:
    if(start not in graph):
      graph[start] = []
    if(end not in graph):
      graph[end] = []
    graph[start].append(end)
    graph[end].append(start)
    
  return graph


def print_graph(graph):
  for vertex, neighbours in graph.items():
    print(f"{vertex}: {neighbours}")

def path_existance(g, s, t):
  for vertex, neighbour in g.items():
    if(vertex == s):
      if(t in neighbour):
        return True
  
  return False

if __name__ == '__main__':
  graph = create_graph(edges)
  print_graph(graph)
  
  start = int(input("Enter a starting node: "))
  end = int(input("Enter a destination node: "))
  
  print(path_existance(graph, start, end))