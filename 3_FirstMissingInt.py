def first_missing_positive_integer(integers):
  integers.sort()
  count = 1
  for y in integers:
    if y == count:
      count += 1
  return count