def find_index(sorted_list, target):
	x = 0
	while x <= len(sorted_list)-1:
		if sorted_list[x] >= target:
			return  x
		x += 1
	return  x

l1 = [1,3,5,6]
print(find_index(l1, 0))