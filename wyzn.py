from copy import deepcopy
from numpy import linalg

# 1 sposób

def pom(matrix, row, col):
    new_matrix = deepcopy(matrix)
    new_matrix.remove(matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].remove(new_matrix[i][col])
    return new_matrix

def det(matrix):
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            return None
    if len(matrix) == 2:
        new_matrix = matrix[0][0] * \
                     matrix[1][1] - \
                     matrix[1][0] * \
                     matrix[0][1]
        return  new_matrix
    else:
        result = 0
        num_col = num_rows
        for j in range(num_col):
            pom1 = (-1) ** (0+j) * matrix[0][j] * det(pom(matrix, 0, j))
            result += pom1
        return result


a_mat = [[-1,2,1],[3,-1,2],[1,-2,3]]
print(det(a_mat))


# 2 sposob
b_mat = [[-1,2,1],[3,-1,2],[1,-2,3]]

print(linalg.det(b_mat))
