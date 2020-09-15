'''
def translate(img, key):
  if key == "up":
    size = len(img.pop(0))
    img.append([0]*size)
    return img
  elif key == "down":
    size = len(img.pop(-1))
    img.insert(0, [0]*size)
    return img
  elif key == "left":
    for x in range(len(img)):
      img[x].pop(0)
      img[x].append(0)
    return img
  elif key == "right":
    for x in range(len(img)):
      img[x].pop(-1)
      img[x].insert(0, 0)
    return img
def overlap(img1, img2):
  count = 0
  for x in range(len(img1)):
    for y in range(len(img2)):
      if img1[x][y] == 1 and img1[x][y] == img2[x][y]:
        count+=1
  return count

def largestOverlap(img1, img2, max_num):
  trls = []
  olap = []
  trls.append(translate(img1, 'up'))
  trls.append(translate(img1, 'down'))
  trls.append(translate(img1, 'left'))
  trls.append(translate(img1, 'right'))
  olap.append(overlap(trls[0], img2))
  olap.append(overlap(trls[1], img2))
  olap.append(overlap(trls[2], img2))
  olap.append(overlap(trls[3], img2))
  max_key = olap.index(max(olap))
  if olap[max_key] > max_num:
    largestOverlap(trls[max_key] ,img2, max_num)
  else:
    return max_num
'''
def largestOverlap(img1, img2):
  dimensions = len(img1)
  def shift_count(x_shift, y_shift, img1, img2):
    l_shitft_count, r_shift_count = 0, 0
    for x1, x2 in enumerate(range(y_shift,dimensions)):
      for y1, y2 in enumerate(range(x_shift,dimensions)):
        if img1[x2][y2] == 1 and img1[x2][y2] == img2[x1][y1]:
          l_shitft_count +=1
        if img1[x2][y1] == 1 and img1[x2][y1] == img2[x1][y2]:
          r_shift_count +=1
    return(max(l_shitft_count, r_shift_count))
  max_nums = 0
  for y in range(0,dimensions):
    for x in range(0,dimensions):
      max_nums= max(max_nums, shift_count(x, y, img1, img2))
      max_nums= max(max_nums, shift_count(x, y, img2, img1))
  return max_nums


img1 = [[1,1,0],
        [0,1,0],
        [0,1,0]]
img2 = [[0,0,0],
        [0,1,1],
        [0,0,1]]

print(largestOverlap(img1, img2))