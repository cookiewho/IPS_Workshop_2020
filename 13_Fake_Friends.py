class SocialGraph:
  def __init__(self):
    self.members = {}


  def add_member(self,node):
    self.members[node] = set()


  def add_friend(self,node_a,node_b):
    self.members[node_a].add(node_b)
    self.members[node_b].add(node_a)
    
  
  def fraud_check(self, user):
    count = 0
    for init_friend in self.members[user]:
      for friend in self.members[init_friend]:
        if friend == user:
          continue
        elif friend in self.members[user]:
          count += 1
          break
    if count != 0:
      num = count
      while num >1:
        if len(self.members[user])% num == 0 and count % num == 0:
          break
        num -= 1
      ans = (count//num, len(self.members[user])//num )
    else:
      ans = (count,len(self.members[user]))
    return ans
    # Return the ratio of (count of friendships) to (count of your friends having at least one friend in common with you)



graph = SocialGraph()

## Friend Group 1
graph.add_member('Alice')
graph.add_member('Bob')
graph.add_member('Carol')
graph.add_member('Dave')
graph.add_member('Eve')
graph.add_member('Faythe')
graph.add_member('Grace')

## Friend Group 2
graph.add_member('Zed')
graph.add_member('Xavier')
graph.add_member('Quill')
graph.add_member('Robert')


## Friend Group 3
graph.add_member('Heidi')
graph.add_member('Niaj')
graph.add_member('Ivan')
graph.add_member('Trent')


## Friend Group 4
graph.add_member('Katy')
graph.add_member('John')
graph.add_member('Kevin')
graph.add_member('Terry')
graph.add_member('Karen')
graph.add_member('Jacob')
graph.add_member('Kelly')
graph.add_member('Tracy')

## Friend Group 5
graph.add_member('Shelly')
graph.add_member('Jon')
graph.add_member('Katherine')
graph.add_member('Marcus')
graph.add_member('Mike')
graph.add_member('Michael')
graph.add_member('Mikey')
graph.add_member('Mike B')

## Friend Group 6
graph.add_member('Alison')
graph.add_member('Kun')
graph.add_member('Zuri')
graph.add_member('Sushma')
graph.add_member('Javier')
graph.add_member('Trent K')
graph.add_member('Paul')
graph.add_member('Xiang')


## Friendships
graph.add_friend('Alice', 'Bob')
graph.add_friend('Alice', 'Carol')
graph.add_friend('Alice', 'Dave')
graph.add_friend('Bob', 'Dave')
graph.add_friend('Carol', 'Dave')
graph.add_friend('Alice', 'Eve')
graph.add_friend('Eve', 'Grace')
graph.add_friend('Eve', 'Bob')
graph.add_friend('Faythe', 'Eve')
graph.add_friend('Dave', 'Faythe')
graph.add_friend('Grace', 'Faythe')


graph.add_friend('Xavier', 'Quill')
graph.add_friend('Robert', 'Quill')
graph.add_friend('Xavier', 'Robert')
graph.add_friend('Zed', 'Quill')
graph.add_friend('Zed', 'Xavier')

graph.add_friend('Heidi', 'Niaj')
graph.add_friend('Heidi', 'Ivan')
graph.add_friend('Heidi', 'Trent')
graph.add_friend('Niaj', 'Trent')
graph.add_friend('Ivan', 'Trent')
graph.add_friend('Niaj', 'Ivan')

graph.add_friend('Katy', 'John')
graph.add_friend('Katy', 'Kevin')
graph.add_friend('Katy', 'Terry')
graph.add_friend('Kelly', 'Katy')
graph.add_friend('John', 'Kevin')
graph.add_friend('Kevin', 'Terry')
graph.add_friend('Terry', 'Karen')
graph.add_friend('Karen', 'John')
graph.add_friend('Jacob', 'John')
graph.add_friend('Tracy', 'Karen')
graph.add_friend('Tracy', 'Kelly')



graph.add_friend('Shelly', 'Jon')
graph.add_friend('Shelly', 'Kevin')
graph.add_friend('Shelly', 'Terry')
graph.add_friend('Kelly', 'Shelly')
graph.add_friend('Kevin', 'Terry')
graph.add_friend('Terry', 'Katherine')
graph.add_friend('Katherine', 'Kevin')
graph.add_friend('Katherine', 'Mike B')
graph.add_friend('Marcus', 'Terry')
graph.add_friend('Marcus', 'Kevin')
graph.add_friend('Marcus', 'Mike')
graph.add_friend('Marcus', 'Mike')
graph.add_friend('Mike', 'Michael')
graph.add_friend('Mike', 'Mikey')
graph.add_friend('Mike', 'Mike B')
graph.add_friend('Mikey', 'Mike B')
graph.add_friend('Mike B', 'Jon')


graph.add_friend('Alison', 'Sushma')
graph.add_friend('Alison', 'Kun')
graph.add_friend('Alison', 'Zuri')
graph.add_friend('Kelly', 'Alison')
graph.add_friend('Javier', 'Kun')
graph.add_friend('Kun', 'Zuri')
graph.add_friend('Zuri', 'Xiang')
graph.add_friend('Xiang', 'Javier')
graph.add_friend('Sushma', 'Javier')
graph.add_friend('Sushma', 'Zuri')
graph.add_friend('Sushma', 'Kun')
graph.add_friend('Sushma', 'Paul')
graph.add_friend('Sushma', 'Xiang')
graph.add_friend('Paul', 'Michael')
# graph.add_friend('Paul', 'Kun')
graph.add_friend('Paul', 'Trent K')
graph.add_friend('Paul', 'Zuri')
graph.add_friend('Trent K', 'Javier')

print(graph.fraud_check('Paul'))

## Real New User
graph.add_member('Eric')
graph.add_friend('Eric', 'Zuri')
graph.add_friend('Eric', 'Xiang')
graph.add_friend('Eric', 'Sushma')
graph.add_friend('Eric', 'Paul')
graph.add_friend('Eric', 'Michael')

print(graph.fraud_check('Eric')) # 1,1

## Fake Spammer
graph.add_member('Sybil')
graph.add_friend('Sybil', 'Xiang')
graph.add_friend('Sybil', 'Kevin')
graph.add_friend('Sybil', 'Grace')
graph.add_friend('Sybil', 'Niaj')
graph.add_friend('Sybil', 'Quill')

print(graph.fraud_check('Sybil')) # 0,5

## Fake Spammer
graph.add_member('David')
graph.add_friend('David', 'Zed')
graph.add_friend('David', 'Quill')
graph.add_friend('David', 'Niaj')
graph.add_friend('David', 'Heidi')

print(graph.fraud_check('David')) # 1,2
##COUNTING METHOD MAY BE OFF? ##