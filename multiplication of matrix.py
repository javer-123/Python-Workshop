def get_matrix_from_user(prompt):
    rows = int(input(f"{prompt} Enter the number of rows: "))
    cols = int(input(f"{prompt} Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"{prompt} Enter element [{i}][{j}]: ")))
        matrix.append(row)

    return matrix

def multiply_matrices(matrix1, matrix2):
   
    if len(matrix1[0]) != len(matrix2):
        return None

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    print("Matrix 1:")
    matrix1 = get_matrix_from_user("Matrix 1")
    print("\nMatrix 2:")
    matrix2 = get_matrix_from_user("Matrix 2")

    print("\nMatrix 1:")
    print_matrix(matrix1)
    print("\nMatrix 2:")
    print_matrix(matrix2)

    result = multiply_matrices(matrix1, matrix2)
    if result is not None:
        print("\nResult:")
        print_matrix(result)
    else:
        print("\nMatrices cannot be multiplied.")

if _name_ == "_main_":
    main()
