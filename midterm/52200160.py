import numpy as np
import math as m


A = np.random.randint(1,101, size=(10,10))
B = np.random.randint(1,21, size=(2,10))
C = np.random.randint(1,21, size=(10,2))


def Ex_a():
    print("Ex_a: ")
    res = A + A.T + C @ B + B.T @ C.T
    print(res)


def Ex_b():
    print("Ex_b: ")
    res = 0
    exp = 1
    for i in range(10, 20):
        res += (A/i)**exp
        exp += 1
    
    print(res)


def Ex_c():
    print("Ex_c: ")
    new_vector = A[A % 2 != 0]
    print(new_vector)


def isPrime(n: int) -> bool:
    for i in range(2, m.isqrt(n) + 1):
        if n % i == 0:
            return False

    return n > 1


def Ex_d():
    print("Ex_d: ")
    vectorized_isPrime = np.vectorize(isPrime)
    new_vector = vectorized_isPrime(A)

    res = A[new_vector]

    print(res)


def getMaxRowIndices(arr) -> list:
    max_row_length = 0
    indices = []

    for i, row in enumerate(arr):
        count_row = len(row)
        if count_row > max_row_length:
            max_row_length = count_row
            indices = [i]  # Reset indices since we found a new max
        elif count_row == max_row_length:
            indices.append(i)  # Append index if the row length matches the max

    return indices


def Ex_e():
    print("Ex_e: ")
    res = []
    for row in A:
        temp = []
        for num in row:
            if isPrime(num):
                temp.append(int(num))
        res.append(temp)

    maxRowIndex = getMaxRowIndices(res)

    answer = np.array([A[i] for i in maxRowIndex])

    print(answer)
    

def Ex_f():
    print("Ex_f: ")
    res = []
    for row in A:
        temp = []
        i = 0
        while i < len(row) - 1:
            if row[i] % 2 != 0 and row[i+1] % 2 != 0:
                if row[i] not in temp:
                    temp.append(int(row[i]))
                temp.append(int(row[i+1]))
            i += 1
        res.append(temp)
    
    maxRowIndex = getMaxRowIndices(res)

    answer = np.array([A[i] for i in maxRowIndex])

    print(answer)


def main():
    print("Matrix A:",A, sep="\n")
    print("Matrix B:",B, sep="\n")
    print("Matrix C:",C, sep="\n")
    Ex_a()
    Ex_b()
    Ex_c()
    Ex_d()
    Ex_e()
    Ex_f()


if __name__ == "__main__":
    main()

