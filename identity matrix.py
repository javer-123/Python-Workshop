def get_matrix_from_user():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i}][{j}]: ")))
        matrix.append(row)

    return matrix

def is_identity_matrix(matrix):
    
    if len(matrix) != len(matrix[0]):
        return False
    
 
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j and matrix[i][j] != 1:
                return False
            elif i != j and matrix[i][j] != 0:
                return False
    
    return True

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    print("Enter the matrix elements:")
    matrix = get_matrix_from_user()
    print("\nYou entered the following matrix:")
    print_matrix(matrix)

    if is_identity_matrix(matrix):
        print("\nThe matrix is an identity matrix.")
    else:
        print("\nThe matrix is not an identity matrix.")

if _name_ == "_main_":
    main()
