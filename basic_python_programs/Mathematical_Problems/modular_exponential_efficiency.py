'''
C=(A^B) mod M
A^B can be impractical for large B
1 convert B to binary
    eg. 13 --> 1101
2 if current bit is 1 multiply the current result with base modulo M
   square the base modulo M for each step reducing intermediate values
'''


def modular_exponentiation(A, B, M):
    result = 1
    base = A % M
    while (B > 0):
        if B % 2 == 1:
            result = (result * base) % M
        base = (base * base) % M
        B =B// 2
    return result
print(modular_exponentiation(3, 13, 7))
