def read_matrix(rows, cols):
    return [list(map(int, input().split())) for _ in range(rows)]

def multiply_matrices(A, B):
    n, m = len(A), len(A[0])
    m2, k = len(B), len(B[0])
    assert m == m2, "Matrix dimensions do not match for multiplication."
    
    C = [[0] * k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for l in range(m):
                C[i][j] += A[i][l] * B[l][j]
    return C

def transpose_matrix(M):
    rows, cols = len(M), len(M[0])
    return [[M[j][i] for j in range(rows)] for i in range(cols)]

def main():
    n, m, k = map(int, input().split())

    A = read_matrix(n, m)
    B = read_matrix(m, k)

    
    product = multiply_matrices(A, B)
    result = transpose_matrix(product)
    
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
