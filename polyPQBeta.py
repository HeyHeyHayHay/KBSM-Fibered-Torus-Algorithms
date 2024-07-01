
import sympy

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')

def Pnk_Recursion(n, k):
    # n integer, k natural number

    if (k == 0):
        return PnWithQ(n)
    else:
        PnkRecursionEquation = sympy.expand(A*Pnk_Recursion(n+1, k-1) + (A**-1)*Pnk_Recursion(n-1, k-1))
        return PnkRecursionEquation

def Qn_Recursion(n):
    # n integer
    if (n < 0):
        antisymmetricEquation = sympy.expand(-1*Qn_Recursion(-n))
        return antisymmetricEquation

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        recursionEquation = sympy.expand(lambda_*Qn_Recursion(n-1) - Qn_Recursion(n-2))
        return recursionEquation

def PnWithQ(n):
    # n integer
    PQrecursionEquation = sympy.expand(-A**(n+2)*Qn_Recursion(n+1) + A**(n-2)*Qn_Recursion(n-1))
    return PQrecursionEquation

print(PnWithQ(-2))
print(Pnk_Recursion(1, 2))
