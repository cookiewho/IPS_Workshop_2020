def matrix_search(matrix, target):
    x = 0
    while(x < len(matrix)):
        if target >= matrix[x][0] and target <= matrix[x][len(matrix[x])-1]:
            for y in range(len(matrix[x])):
                if matrix[x][y] == target:
                    return 1
        return 0
        x+=1
    return 0
m = [
[1,   3,  5,  7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]
print(matrix_search(m, 30))