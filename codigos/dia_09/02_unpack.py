# vamos supor que eu quero que A vire B e B vire A

A = 1
B = 5
print(A)
print(B)

# maneira tradicional de fazer isso:
A, B = B, A
print(A)
print(B)

B, A = A, B

# isto é um exemplo de unpack.
a, b, *resto = 1, 2, 3, 4, 5, 6, 7,8, 9
print(a, b, resto)

*resto, a, b = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a, b, resto)

a, *resto, b = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a, b, resto)

def soma_quatro(a, b, c, d):
    return a+b+c+d

values = [1,2,3,4]

soma_quatro(*values)