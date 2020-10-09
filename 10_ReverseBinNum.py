num = int(input())
b_num = bin(num)[2:]
print(int(b_num[::-1], 2))
