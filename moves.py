
from dataStructures import XcFormToWord
from dataStructures import LinearCombination

import polyPQ
import sympy


A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')



# Naming convention: name of object you want to change | direction of accidental changes | change want add or subtract
# ex lambda | right | plus

# Input: XcForm and index to change in XcForm and coefficient

def lambdaLeftMinus(XcForm, indexToChange, startCoefficient):

    firstXcForm = list(XcForm)
    secondXcForm = list(XcForm)

    firstXcForm[indexToChange] = firstXcForm[indexToChange] - 1
    firstXcForm[indexToChange + 1] = firstXcForm[indexToChange + 1] - 1

    firstCoefficient = sympy.expand(A*startCoefficient)

    secondXcForm[indexToChange] = secondXcForm[indexToChange] - 1
    secondXcForm[indexToChange + 1] = secondXcForm[indexToChange + 1] + 1

    secondCoefficient = sympy.expand((A**-1)*(startCoefficient))

    firstWord = XcFormToWord(firstXcForm, firstCoefficient)
    secondWord = XcFormToWord(secondXcForm, secondCoefficient)

    linearCombination = LinearCombination([firstWord, secondWord])

    return linearCombination

def lambdaRightMinus(XcForm, indexToChange, startCoefficient):

    firstXcForm = list(XcForm)
    secondXcForm = list(XcForm)

    firstXcForm[indexToChange] = firstXcForm[indexToChange] - 1
    firstXcForm[indexToChange - 1] = firstXcForm[indexToChange - 1] + 1

    firstCoefficient = sympy.expand(A*startCoefficient)

    secondXcForm[indexToChange] = secondXcForm[indexToChange] - 1
    secondXcForm[indexToChange - 1] = secondXcForm[indexToChange - 1] - 1

    secondCoefficient = sympy.expand((A**-1)*(startCoefficient))

    firstWord = XcFormToWord(firstXcForm, firstCoefficient)
    secondWord = XcFormToWord(secondXcForm, secondCoefficient)

    linearCombination = LinearCombination([firstWord, secondWord])

    return linearCombination

def xRightPlus(XcForm, indexToChange, startCoefficient):

    firstXcForm = list(XcForm)
    secondXcForm = list(XcForm)

    firstXcForm[indexToChange - 1] = firstXcForm[indexToChange - 1] + 1
    firstXcForm[indexToChange] = firstXcForm[indexToChange] + 1

    firstCoefficient = sympy.expand(A**-1*startCoefficient)

    secondXcForm[indexToChange] = secondXcForm[indexToChange] + 2

    secondCoefficient = sympy.expand((-A**-2)*(startCoefficient))


    firstWord = XcFormToWord(firstXcForm, firstCoefficient)
    secondWord = XcFormToWord(secondXcForm, secondCoefficient)

    linearCombination = LinearCombination([firstWord, secondWord])

    return linearCombination

def xRightMinus(XcForm, indexToChange, startCoefficient):

    firstXcForm = list(XcForm)
    secondXcForm = list(XcForm)

    firstXcForm[indexToChange - 1] = firstXcForm[indexToChange - 1] + 1
    firstXcForm[indexToChange] = firstXcForm[indexToChange] - 1

    firstCoefficient = sympy.expand(A*startCoefficient)

    secondXcForm[indexToChange] = secondXcForm[indexToChange] - 2

    secondCoefficient = sympy.expand((-A**2)*(startCoefficient))


    firstWord = XcFormToWord(firstXcForm, firstCoefficient)
    secondWord = XcFormToWord(secondXcForm, secondCoefficient)

    linearCombination = LinearCombination([firstWord, secondWord])

    return linearCombination

def xLeftPlus(XcForm, indexToChange, startCoefficient):

    firstXcForm = list(XcForm)
    secondXcForm = list(XcForm)

    firstXcForm[indexToChange + 1] = firstXcForm[indexToChange + 1] + 1
    firstXcForm[indexToChange] = firstXcForm[indexToChange] + 1

    firstCoefficient = sympy.expand(A*startCoefficient)

    secondXcForm[indexToChange] = secondXcForm[indexToChange] + 2

    secondCoefficient = sympy.expand((-A**2)*(startCoefficient))


    firstWord = XcFormToWord(firstXcForm, firstCoefficient)
    secondWord = XcFormToWord(secondXcForm, secondCoefficient)

    linearCombination = LinearCombination([firstWord, secondWord])

    return linearCombination

def xLeftMinus(XcForm, indexToChange, startCoefficient):

    firstXcForm = list(XcForm)
    secondXcForm = list(XcForm)

    firstXcForm[indexToChange + 1] = firstXcForm[indexToChange + 1] + 1
    firstXcForm[indexToChange] = firstXcForm[indexToChange] - 1

    firstCoefficient = sympy.expand((A**-1)*startCoefficient)

    secondXcForm[indexToChange] = secondXcForm[indexToChange] - 2

    secondCoefficient = sympy.expand((-A**-2)*(startCoefficient))


    firstWord = XcFormToWord(firstXcForm, firstCoefficient)
    secondWord = XcFormToWord(secondXcForm, secondCoefficient)

    linearCombination = LinearCombination([firstWord, secondWord])

    return linearCombination

def lambdaReduce3(XcForm, indexToChange, startCoefficient):

    n = XcForm[indexToChange]
    mPlus = XcForm[indexToChange + 1]
    mMinus = XcForm[indexToChange - 1]

    firstXcForm = list(XcForm)
    secondXcForm = list(XcForm)
    thirdXcForm = list(XcForm)

    # First Word

    firstXcForm.pop(indexToChange + 1)
    centerLambda = firstXcForm.pop(indexToChange)
    rightLambda = firstXcForm.pop(indexToChange - 2)

    newLambda = centerLambda + rightLambda + 1
    firstXcForm[indexToChange - 2] = newLambda

    firstCoefficient = sympy.expand((-A**-1)*startCoefficient)

    firstLinearCombination = polyPQ.Pnk_Recursion(mMinus - 1 - mPlus, n, firstXcForm, indexToChange - 2, firstCoefficient)

    # Second Word

    secondXcForm.pop(indexToChange + 1)
    centerLambda = secondXcForm.pop(indexToChange)
    rightLambda = secondXcForm.pop(indexToChange - 2)

    newLambda = centerLambda + rightLambda
    secondXcForm[indexToChange - 2] = newLambda

    secondCoefficient = sympy.expand(2*startCoefficient)

    secondLinearCombination = polyPQ.Pnk_Recursion(mMinus - 2 - mPlus, n, secondXcForm, indexToChange - 2, secondCoefficient)

    # Third Word

    thirdXcForm[indexToChange + 1] = thirdXcForm[indexToChange + 1] + 1
    thirdXcForm[indexToChange - 1] = thirdXcForm[indexToChange - 1] - 1

    thirdCoefficient = sympy.expand((A**-2)*startCoefficient)

    thirdWord = XcFormToWord(thirdXcForm, thirdCoefficient)

    linearCombination = firstLinearCombination.addLinearCombination(secondLinearCombination.addWord(thirdWord))

    return linearCombination
