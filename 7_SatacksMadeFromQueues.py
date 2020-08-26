class stack():
  def __init__(self):
      self.q1 = []
      self.q2 = []
      return 

  def push(self, x):
    if len(self.q1) == 0:
      self.q1.append(x)
    else: 
      self.q2.append(x)
      while len(self.q1) >0:
        self.q2.insert(0, self.q1.pop())
      self.q1 = self.q2.copy()
      self.q2 = []
    print(self.q1)
    return
        
  def pop(self):
    if len(self.q1) == 0:
      return("Stack is empty")
      
    else:
      return self.q1.pop()
  
stak = stack()
stak.push(4)
stak.pop() #return 4
stak.push(5)
stak.push(6)
stak.push(7)
stak.push(8)
print(stak.pop())
print(stak.pop())
print(stak.pop())
print(stak.pop())
print(stak.pop())