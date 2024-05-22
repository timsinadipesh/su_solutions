# strassen's matrix multiplication algorithm

import numpy as np

def add_mat(A, B):
    return A + B

def subtract_mat(A, B):
    return A - B

def strassen(A, B):
    if len(A) == 1:
        return A * B
    
    mid = len(A) // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]
    
    M1 = strassen(add_mat(A11, A22), add_mat(B11, B22))
    M2 = strassen(add_mat(A21, A22), B11)
    M3 = strassen(A11, subtract_mat(B12, B22))
    M4 = strassen(A22, subtract_mat(B21, B11))
    M5 = strassen(add_mat(A11, A12), B22)
    M6 = strassen(subtract_mat(A21, A11), add_mat(B11, B12))
    M7 = strassen(subtract_mat(A12, A22), add_mat(B21, B22))

    C11 = add_mat(subtract_mat(add_mat(M1, M4), M5), M7)
    C12 = add_mat(M3, M5)
    C21 = add_mat(M2, M4)
    C22 = add_mat(subtract_mat(add_mat(M1, M3), M2), M6)

    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))

# test
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

B = np.array([[16, 15, 14, 13],
              [12, 11, 10, 9],
              [8, 7, 6, 5],
              [4, 3, 2, 1]])

C = strassen(A, B)
print(C)