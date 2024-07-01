
from comparingWords import testWord
from dataStructures import XcFormToWord
from dataStructures import LinearCombination
import sympy
import moves

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')


#Lemma 3.3

def algorithm0(c, word):

    if (part1(c, word) != False):
        return part1(c, word)

    if (part2(c, word) != False):
        return part2(c, word)

    if (part3(c, word) != False):
        return part3(c, word)

    if (part4(c, word) != False):
        return part4(c, word)

    if (part5(c, word) != False):
        return part5(c, word)

    if (part6(c, word) != False):
        return part6(c, word)

    if (part7(c, word) != False):
        return part7(c, word)

    raise Exception("Word {} found no match".format(word))
    return False

# algorithm Lemma 3.3 basisNumber 0

def part1(c, word):

    if (testPart1(c, word) == False):
        return False

    wordStartCoefficient = word.coefficient

    part1XcForm = testPart1(c, word)

    linearCombination = moves.lambdaLeftMinus(part1XcForm, 2, wordStartCoefficient)

    return linearCombination

def testPart1(c, word):

    formPart1 = [c, "k", "n >= 1", "m", "w", "w"]

    return testWord(formPart1, word)

def part2(c, word):

    if (testPart2(c, word) == False):
        return False

    wordStartCoefficient = word.coefficient

    part2XcForm = testPart2(c, word)

    linearCombination = moves.xLeftMinus(part2XcForm, 3, wordStartCoefficient)

    return linearCombination

def testPart2(c, word):

    formPart2 = [c, "k", 0, "m > c + 1", "w", "w"]

    return testWord(formPart2, word)

def part3(c, word):

    if (testPart3(c, word) == False):
        return False

    wordStartCoefficient = word.coefficient

    part3XcForm = testPart3(c, word)

    linearCombination = moves.xLeftPlus(part3XcForm, 3, wordStartCoefficient)

    return linearCombination

def testPart3(c, word):

    formPart3 = [c, "k", 0, "m < c", "w", "w"]

    return testWord(formPart3, word)

def part4(c, word):

    if (testPart4(c, word) == False):
        return False

    wordStartCoefficient = word.coefficient

    part4XcForm = testPart4(c, word)

    linearCombination = moves.lambdaReduce3(part4XcForm, 4, wordStartCoefficient)

    return linearCombination

def testPart4(c, word):

    formPart4 = [c, "k", 0, c + 1, "n", "m", "w"]

    return testWord(formPart4, word)

def part5(c, word):

    if (testPart5(c, word) == False):
        return False

    wordStartCoefficient = word.coefficient

    part5XcForm = testPart5(c, word)

    linearCombination = moves.lambdaRightMinus(part5XcForm, 4, wordStartCoefficient)

    return linearCombination

def testPart5(c, word):

    formPart5 = [c, "k", "n", "m", "n >= 1"]

    return testWord(formPart5, word)

def part6(c, word):

    if (testPart6(c, word) == False):
        return False

    wordStartCoefficient = word.coefficient

    part6XcForm = testPart6(c, word)

    linearCombination = moves.xRightMinus(part6XcForm, 3, wordStartCoefficient)

    return linearCombination

def testPart6(c, word):

    formPart6 = [c, "k", "n", "m > c + 1", 0]

    return testWord(formPart6, word)

def part7(c, word):

    if (testPart7(c, word) == False):
        return False

    wordStartCoefficient = word.coefficient

    part7XcForm = testPart7(c, word)

    linearCombination = moves.xRightPlus(part7XcForm, 3, wordStartCoefficient)

    return linearCombination

def testPart7(c, word):

    formPart7 = [c, "k", "n", "m < c", 0]

    return testWord(formPart7, word)
