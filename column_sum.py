def column_matrix_sum(given_matrix, number_of_rows, number_of_columns):
    column_sum = []
    for column in range(number_of_columns):
        col_sum = 0
        for row in range(number_of_rows):
            col_sum += given_matrix[row][column]
        column_sum.append(col_sum)
    return column_sum


try:
    rows = int(input("Enter number of rows : "))
    columns = int(input("Enter number of columns : "))
    matrix = [[int(input("Enter an integer to insert into the matrix : ")) for column in range(columns)] for row in
              range(rows)]
    print("The column sum of given matrix is : ", column_matrix_sum(matrix, rows, columns))
except ValueError:
    print("Invalid Input. Please enter only integers")
