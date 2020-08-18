class Graph:
  def __init__(self):
    self.verticies = {}


  def add_node(self,node):
    self.verticies[node] = []


  def add_edge(self,node_a,node_b):
    self.verticies[node_a].append(node_b)
    self.verticies[node_b].append(node_a)
### CODE BELOW IS MINE, REST IS PROVIDED ###
  def subgraph(self, start):
    # Implement the subgraph traversal
    to_visit = [start]
    visited = set()
    while len(to_visit)>0:
      curr = to_visit.pop(0)
      if curr not in visited:

        visited.add(curr)
        for x in self.verticies[curr]:
          to_visit.append(x)
    return(visited)
  
graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('Z')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('D', 'B')
print(graph.subgraph('A'))