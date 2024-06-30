
from comparingWords import testWord
from dataStructures import XcFormToWord
from dataStructures import LinearCombination
import sympy


A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')


#Lemma 3.3



def part7(c, word):

    if (testPart7(c, word) == False):
        return False

    wordStartCoefficient = word.coefficient

    part7XcForm = testPart7(c, word)

    firstXcForm = list(part7XcForm)
    secondXcForm = list(part7XcForm)

    firstXcForm[2] = firstXcForm[2] + 1
    firstXcForm[3] = firstXcForm[3] + 1

    firstCoefficient = sympy.expand(A**-1*wordStartCoefficient)

    secondXcForm[3] = secondXcForm[3] + 2

    secondCoefficient = sympy.expand((-A**-2)*(wordStartCoefficient))


    firstWord = XcFormToWord(firstXcForm, firstCoefficient)
    secondWord = XcFormToWord(secondXcForm, secondCoefficient)

    linearCombination = LinearCombination([firstWord, secondWord])

    return linearCombination

def testPart7(c, word):

    formPart7 = [c, "k", "n", "m < c", 0]

    return testWord(formPart7, word)
