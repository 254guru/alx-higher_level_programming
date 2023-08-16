#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []

    # Iterate through the rows of the input matrix
    for row in matrix:
        squared_row = []

        # Iterate through the elements in each row and square them
        for element in row:
            squared_element = element ** 2
            squared_row.append(squared_element)

            # Add the squared row to the squared_matrix
        squared_matrix.append(squared_row)

        return squared_matrix
