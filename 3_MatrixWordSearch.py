def findWord(matrix, x, y, word, ind):
  if ind >= len(word):
    # print("FOUND THE WORD: " + word)
    return True
  else:
    #print("checking adjacent matricies for " + word[ind])
    if(x+1 < len(matrix) and matrix[x+1][y] == word[ind]):
      #print(matrix[x+1][y] + " found in matrix")
      if(findWord(matrix, x+1, y, word, ind+1)):
        return True
    if(x-1 >= 0 and matrix[x-1][y] == word[ind]):
      #print(matrix[x-1][y] + " found in matrix")
      if(findWord(matrix, x-1, y, word, ind+1)):
        return True
    if(y+1 < len(matrix[x]) and matrix[x][y+1] == word[ind]):
      #print(matrix[x][y+1] + " found in matrix")
      if(findWord(matrix, x, y+1, word, ind+1)):
        return True
    if(y-1 >= 0 and matrix[x][y-1] == word[ind]):
      #print(matrix[x][y-1] + " found in matrix")
      if(findWord(matrix, x, y-1, word, ind+1)):
        return True
    #print(word[ind] + " NOT found in matrix")
    return False

def findStr(matrix, word):
  for x in range(len(matrix)):
    for y in range(len(matrix[x])):
      if matrix[x][y] == word[0]:
        #print('Found: ' + str(matrix[x][y]))
        matrix[x][y] = ' '
        ind = 1
        if(findWord(matrix, x, y, word, ind)):
          return True
      #print(matrix[x][y])
  return False


test_matrix = [
  ['A', 'X', 'S', 'G'],
  ['B', 'B', 'A', 'T'],
  ['T', 'T', 'C', 'U']
]
print(findStr(test_matrix,"UTA"))