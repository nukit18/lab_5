import sys


def get_determinant(matrix_arr):
    determinant = 0
    for i in range(len(matrix_arr)):
        complement = get_alg_complement(matrix_arr, 0, i)
        if len(complement) == 0:
            determinant = -matrix_arr[0][0]
        elif len(complement) == 1:
            determinant = (determinant * (-1) + matrix_arr[0][i] * complement[0][0])
        else:
            determinant = determinant + matrix_arr[0][i] * get_determinant(complement) * ((-1) ** (i + 1))
    return determinant * (-1)


def get_alg_complement(matrix_arr, index_first_row, index_first_col):
    rang = len(matrix_arr)
    new_matrix_arr = []
    counter = -1
    for i in range(rang):
        if i != index_first_row:
            new_matrix_arr.append([])
            counter += 1
        for j in range(rang):
            if i != index_first_row and j != index_first_col:
                new_matrix_arr[counter].append(matrix_arr[i][j])
    return new_matrix_arr


def multiply_by_number(matrix_arr, number):
    for i in range(len(matrix_arr)):
        for j in range(len(matrix_arr[i])):
            matrix_arr[i][j] *= number
    return matrix_arr


def get_inverse_matrix(matrix_arr):
    inverse_matrix = []
    determinant = get_determinant(matrix_arr)
    if determinant == 0:
        print("Решений нет или их бесконечно много!")
        sys.exit()
    for i in range(len(matrix_arr)):
        inverse_matrix.append([])
        for j in range(len(matrix_arr[i])):
            inverse_matrix[i].append(
                (1 / determinant) * get_determinant(get_alg_complement(matrix_arr, i, j)) * ((-1) ** (j + i)))
    return get_transposed_matrix(inverse_matrix)


def get_transposed_matrix(matrix_arr):
    transposed_matrix = []
    for i in range(len(matrix_arr)):
        transposed_matrix.append([])
        for j in range(len(matrix_arr[i])):
            transposed_matrix[i].append(matrix_arr[j][i])
    return transposed_matrix


def multiply_by_vector(matrix_arr, vector_arr):
    new_matrix_arr = []
    if len(matrix_arr) != len(vector_arr):
        print("Несовместивые данные!")
        sys.exit()
    for i in range(len(matrix_arr)):
        new_matrix_arr.append(0)
        for j in range(len(matrix_arr[i])):
            new_matrix_arr[i] += matrix_arr[i][j] * vector_arr[j]
    return new_matrix_arr


def get_unknown_members(matrix_arr, b_arr):
    if len(matrix_arr) == 0 or len(matrix_arr) != len(b_arr) != len(matrix_arr[0]):
        print("Несовметимые данные!")
        sys.exit()
    determinant = get_determinant(matrix_arr)
    if determinant == 0:
        print("Решений нет или их бесконечно много!")
        sys.exit()
    inverse_matrix = get_inverse_matrix(matrix_arr)
    answer_vector = multiply_by_vector(inverse_matrix, b_arr)

    return answer_vector


if __name__ == '__main__':
    matrix_str = input("Введите матрицу в строку в формате, где разделение между числами-пробел\n")
    matrix_str = matrix_str.split()
    rang = (len(matrix_str)) ** 0.5
    if not rang.is_integer():
        raise IOError("Матрица на квадратная")
    matrix_arr = []
    counter = 0
    for i in range(int(rang)):
        matrix_arr.append([])
        for j in range(int(rang)):
            matrix_arr[i].append(int(matrix_str[counter]))
            counter += 1

    b = input("Введите свободные члены уравнения, вид уравнения A * X = B, B-вектор свободных членов\n")
    b_arr = [int(x) for x in b.split()]
    if len(b_arr) != len(matrix_arr):
        raise IOError("Ранг матрицы и количество свободных членов должны совпадать!")
    print(get_unknown_members(matrix_arr, b_arr))
