class SocialGraph:
  def __init__(self):
    self.members = {}


  def add_node(self,node):
    self.members[node] = set()


  def add_edge(self,node_a,node_b):
    self.members[node_a].add(node_b)
    self.members[node_b].add(node_a)
    
  def subgraph(self, root):
    to_visit = [root]

    visited = set()

    while len(to_visit) > 0:
      node = to_visit.pop(0)
      if node not in visited:
        
        visited.add(node)

        for neighbor in self.members[node]:
          to_visit.append(neighbor)
    return visited
### CODE BELOW IS MINE, REST IS PROVIDED ###
  def suggest_friends(self, me):
    most = 0
    non_friends = {}
    for direct_friend in self.members[me]:
      for potential_friend in self.members[direct_friend]:
        if potential_friend == me or potential_friend in self.members[me]:
          continue
        else:
          if potential_friend in non_friends:
            non_friends[potential_friend] += 1
            if non_friends[potential_friend] > most:
              most = non_friends[potential_friend]
          else:
            non_friends[potential_friend] = 1
            if non_friends[potential_friend] > most:
              most = non_friends[potential_friend]
    friend_suggestions = set()
    for friend in non_friends:
      if non_friends[friend] == most:
        friend_suggestions.add(friend)
    return friend_suggestions