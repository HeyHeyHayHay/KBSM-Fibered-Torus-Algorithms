
import sympy
from dataStructures import XcFormToWord
from dataStructures import LinearCombination

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')

def Pnk_Recursion(n, k, XcForm, lambdaIndexPosition, startCoefficient):
    # n integer, k natural number

    if (k == 0):
        return PnWithQ(n, XcForm, lambdaIndexPosition, startCoefficient)
    else:

        firstCombination = Pnk_Recursion(n + 1, k - 1, XcForm, lambdaIndexPosition, startCoefficient)
        secondCombination = Pnk_Recursion(n - 1, k - 1, XcForm, lambdaIndexPosition, startCoefficient)

        firstCombination.multiplyCoefficient(A)
        secondCombination.multiplyCoefficient(A**-1)

        PnkRecursionCombination = firstCombination.addLinearCombination(secondCombination)
        return PnkRecursionCombination

def Qn_Recursion(n, XcForm, lambdaIndexPosition, startCoefficient):
    # n integer

    if (n < 0):
        antisymmetricCombination = Qn_Recursion(-n, XcForm, lambdaIndexPosition, startCoefficient)
        antisymmetricCombination.multiplyCoefficient(-1)
        return antisymmetricCombination

    if (n == 0):

        return LinearCombination([])
    elif (n == 1):
        word = XcFormToWord(XcForm, startCoefficient)
        combo = LinearCombination([word])
        return combo
    else:

        firstXcForm = list(XcForm)
        secondXcForm = list(XcForm)

        firstXcForm[lambdaIndexPosition] = firstXcForm[lambdaIndexPosition] + 1

        firstCombination = Qn_Recursion(n - 1, firstXcForm, lambdaIndexPosition, startCoefficient)
        secondCombination = Qn_Recursion(n - 2, secondXcForm, lambdaIndexPosition, startCoefficient)

        secondCombination.multiplyCoefficient(-1)

        QnrecursionCombination = firstCombination.addLinearCombination(secondCombination)

        return QnrecursionCombination

def PnWithQ(n, XcForm, lambdaIndexPosition, startCoefficient):
    # n integer


    firstCombination = Qn_Recursion(n + 1, XcForm, lambdaIndexPosition, startCoefficient)
    secondCombination = Qn_Recursion(n - 1, XcForm, lambdaIndexPosition, startCoefficient)

    firstCombination.multiplyCoefficient(-A**(n+2))
    secondCombination.multiplyCoefficient(A**(n-2))

    PQrecursionCombination = firstCombination.addLinearCombination(secondCombination)
    #PQrecursionCombination = secondCombination.addLinearCombination(firstCombination)

    return PQrecursionCombination
