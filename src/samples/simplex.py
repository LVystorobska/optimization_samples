import numpy as np
from scipy import optimize 
import math

#suppose all arrays in numpy format
def simplex_run(static_coefs, basis_indexes, solution_vector, input_matrix, delta_back_step):
    dynamic_coefs = np.array([])
    teta_vector = np.array([])
    for value in basis_indexes:
        dynamic_coefs = np.append(dynamic_coefs, static_coefs[value])

    delta_zero = np.dot(dynamic_coefs, solution_vector)
    delta_vector = np.dot(dynamic_coefs, input_matrix)

    for index, value in enumerate(static_coefs):
        temp_val = delta_vector[index]
        np.put(delta_vector, index, (temp_val - value))
    print('Delta:', delta_vector)

    min_column_index = np.where(delta_vector == np.amin(delta_vector))[0][0]
    min_column = input_matrix[ : , min_column_index]

    for index, value in enumerate(min_column):
        teta_vector = np.append(teta_vector, (solution_vector[index]/value))
    
    min_row_index = np.where(teta_vector == np.amin(teta_vector))[0][0]
    min_row = input_matrix[min_row_index]

    pivot_el = input_matrix[min_row_index, min_column_index]
    np.put(basis_indexes, min_row_index, min_column_index)

    updated_matrix = np.array([])
    updated_solution_vector = np.array([])
    indexes_to_be_calc = np.array([])    
    for index, val in enumerate(static_coefs):
        if index in basis_indexes:
            insert_column_index = np.where(basis_indexes == index)
            insertion_identity_column = np.array([])
            for i in range(len(min_column)):
                if i == insert_column_index[0][0]:
                    insertion_identity_column = np.append(insertion_identity_column, 1)
                else:
                    insertion_identity_column = np.append(insertion_identity_column, 0)
            updated_matrix = np.concatenate((updated_matrix, insertion_identity_column))
        else:
            updated_matrix = np.concatenate((updated_matrix, np.zeros(len(min_column))))
            indexes_to_be_calc = np.append(indexes_to_be_calc, index)
    
    updated_matrix = updated_matrix.reshape(len(input_matrix), len(input_matrix[0]),  order='F')

    for index, val in enumerate(min_column):
        b_pre_value = solution_vector[index]
        if min_row_index == index:
            updated_solution_vector = np.append(updated_solution_vector, (b_pre_value/pivot_el))
            for ind_j, val_j in enumerate(min_row):
                if ind_j in indexes_to_be_calc:
                    el_pre_value = input_matrix[min_row_index, ind_j]
                    updated_matrix[min_row_index, ind_j] = el_pre_value/pivot_el
        else:
            el_by_min_row_index_b = solution_vector[min_row_index]
            updated_solution_vector = np.append(updated_solution_vector, (b_pre_value - (val*el_by_min_row_index_b)/pivot_el))
            for ind_j, val_j in enumerate(min_row):
                if ind_j in indexes_to_be_calc:
                    el_pre_value = input_matrix[index, ind_j]
                    side_el_pre_value = input_matrix[min_row_index, ind_j]
                    updated_matrix[index, ind_j] = el_pre_value - (val*side_el_pre_value)/pivot_el

    if all(i >= 0 for i in delta_vector):
        return solution_vector
    else:
        return simplex_run(static_coefs, basis_indexes, updated_solution_vector, updated_matrix, delta_vector)


static = np.array([5,4,0,0])
indexes = np.array([2,3])
solutions = np.array([4,5])
matrix = np.array(([2,1,1,0],[1,2,0,1]))
deltas = np.array([-1.,-1,-1,-1])

result = simplex_run(static,indexes,solutions, matrix, deltas)

print('Simplex-test result:', result)

                    
                



















