# --------------------------------------
# CSCI 127, Lab 7
# October 17, 2017
# William Riley Roberts
# --------------------------------------


def print_matrix(matrix, rows, columns, text):
    print('\n')
    print(text + '\n')

    for row in range(rows):
        print_header(columns)
        theStr = '|'
        for col in range(columns):
            
            try:
                number = matrix[row, col]
            except:
                number = 0

            theStr += "{:3d}|".format(number)


        print(theStr)
    print_header(columns)

def add_matrices(matrix1, matrix2, rows, columns):
    matrix3 = {}
    for row in range(rows):
        for col in range(columns):
            val1 = matrix1.get((row, col), 0)
            val2 = matrix2.get((row, col),0 )

            if val1 + val2 != 0:
                matrix3[row, col] = val1 + val2
            else:
                None




# A way to do it without any fancy dictionary methods. Came up with this ^ afterwards         
##            try:
##                if matrix1[row, col] + matrix2[row, col] == 0:
##                    None
##                else: matrix3[row, col] = matrix1[row, col] + matrix2[row, col] #This should be the only  needed line of code.. but KeyError...
##            except:
##                try:
##                    matrix3[row, col] = matrix1[row, col] + 0
##                except:
##                    try:
##                        matrix3[row, col] = matrix2[row, col] + 0
##                    except:
##                        None
                
            

    return matrix3

# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def print_header(columns):
    line = "+"
    for i in range(columns):
        line += "---+"
    print(line)

# --------------------------------------

def read_matrix(input_file):
    matrix = {}
    line = input_file.readline().split()
    while line[0] != "stop":
        row = int(line[0])
        column = int(line[1])
        value = int(line[2])
        matrix[(row, column)] = value
        line = input_file.readline().split()
    return matrix

# --------------------------------------

def main (file_name):
    input_file = open(file_name, "r")
    
    line = input_file.readline().split()
    rows = int(line[0])
    columns = int(line[1])

    matrix_1 = read_matrix(input_file)
    print_matrix(matrix_1, rows, columns, "Matrix 1")
    
    matrix_2 = read_matrix(input_file)
    print_matrix(matrix_2, rows, columns, "Matrix 2")

    matrix_3 = add_matrices(matrix_1, matrix_2, rows, columns)
    print_matrix(matrix_3, rows, columns, "Matrix 1 + Matrix 2")
    print("Matrix 3 =", matrix_3)

# --------------------------------------

main ("sparse-matrix.txt")
