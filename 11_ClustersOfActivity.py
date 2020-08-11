def find_center(matrix):
  xs = 0
  ys = 0
  num_cases = 0
  for key, value in matrix.items():
    x_y = key.split(",")
    num_cases += value
    xs += int(x_y[0]) * value
    ys += int(x_y[1]) * value
  xs = round(xs/num_cases)
  ys = round(ys/num_cases)
  return(str(xs) + "," + str(ys))
    


reported_outbreak = {
  "5,5": 10,
  "5,6": 8,
  "5,4": 8,
  "4,5": 8,
  "4,5": 8,
  "4,6": 8,
  "6,6": 7,
  "6,5": 8,
  "4,4": 8,
  "3,4": 4,
  "3,3": 2,
  "6,7": 2 
}

print(find_center(reported_outbreak))