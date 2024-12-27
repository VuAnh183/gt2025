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

def path_existance(graph, start, end):
  for vertex, neighbour in graph.items():
    if(vertex == start):
      if(end in neighbour):
        return True
  
  return False

if __name__ == '__main__':
  graph = create_graph(edges)
  # print_graph(graph)
  
  start = int(input("Enter a starting node: "))
  end = int(input("Enter a destination node: "))
  
  if(path_existance(graph, start, end) == True):
    print(True)
  else:
    print(False)