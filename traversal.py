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

def row_major_traversal(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")

def column_major_traversal(matrix):
    for col in range(len(matrix[0])):
        for row in matrix:
            print(row[col], end=" ")

def diagonal_traversal(matrix):
    for k in range(len(matrix) + len(matrix[0]) - 1):
        for i in range(max(0, k - len(matrix[0]) + 1), min(k + 1, len(matrix))):
            j = k - i
            print(matrix[i][j], end=" ")

def spiral_traversal(matrix):
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1

def main():
    print("Enter the matrix elements:")
    matrix = get_matrix_from_user()
    print("\nMatrix:")
    for row in matrix:
        print(row)

    while True:
        print("\nTraversal Options:")
        print("1. Row-Major Traversal")
        print("2. Column-Major Traversal")
        print("3. Diagonal Traversal")
        print("4. Spiral Traversal")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nRow-Major Traversal:")
            row_major_traversal(matrix)
        elif choice == "2":
            print("\nColumn-Major Traversal:")
            column_major_traversal(matrix)
        elif choice == "3":
            print("\nDiagonal Traversal:")
            diagonal_traversal(matrix)
        elif choice == "4":
            print("\nSpiral Traversal:")
            spiral_traversal(matrix)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
main()
