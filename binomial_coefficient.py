# Computing binomial coefficients - dynamic programming
def binomial_coefficient(n, k):
    c =[[0 for i in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i-1][j-1] + c[i-1][j]
    return c[n][k]

n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))

print(f"The value of C[{n}][{k}] is "+ str(binomial_coefficient(n,k)))