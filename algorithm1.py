
from comparingWords import testWord
from dataStructures import XcFormToWord
from dataStructures import LinearCombination
import sympy
import moves
from algorithmGeneral import algorithmMatchAndMove

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')


#Lemma 3.3 for basis 1

def algorithm1(c, word):

    listOfPartFunctions = [part1, part2, part3, part4, part5, part6, part7, part8, part9, part10, part11, part12, part13, part14]

    for part in listOfPartFunctions:

        match = part(c, word)

        if (match != False):
            return match

    raise Exception("Word {} found no match".format(word))
    return False

# algorithm Lemma 3.3 but for basisNumber 1

def part1(c, word):

    formPart1 = [c, "k", "n >= 1", "m", "w", "w", "w", "w"]

    return algorithmMatchAndMove(c, word, moves.lambdaLeftMinus, formPart1, 2)

def part2(c, word):

    formPart2 = [c, "k", 0, "m > c + 1", "w", "w", "w", "w"]

    return algorithmMatchAndMove(c, word, moves.xLeftMinus, formPart2, 3)

def part3(c, word):

    formPart3 = [c, "k", 0, "m < c", "w", "w", "w", "w"]

    return algorithmMatchAndMove(c, word, moves.xLeftPlus, formPart3, 3)

def part4(c, word):

    formPart4 = [c, "k", 0, c + 1, "n", "m", "w", "w", "w"]

    return algorithmMatchAndMove(c, word, moves.lambdaReducePlus, formPart4, 4)

"______________________________________________________________"

def part5(c, word):

    formPart5 = [c, "k", "n", "m", "n", "m", "n >= 1"]

    return algorithmMatchAndMove(c, word, moves.lambdaRightMinus, formPart5, 6)

def part6(c, word):

    formPart6 = [c, "k", "n", "m", "n", "m > c + 1", 0]

    return algorithmMatchAndMove(c, word, moves.xRightMinus, formPart6, 5)

def part7(c, word):

    formPart7 = [c, "k", "n", "m", "n", "m < c", 0]

    return algorithmMatchAndMove(c, word, moves.xRightPlus, formPart7, 5)

"______________________________________________________________"

def part8(c, word):

    formPart8 = [c, "k", "n", "m", "n", c, 0]

    return algorithmMatchAndMove(c, word, moves.lambdaReducePlus, formPart8, 4)

"______________________________________________________________"

def part9(c, word):

    formPart9 = [c, "k", "n", "m", "n >= 1", c + 1, 0]

    return algorithmMatchAndMove(c, word, moves.lambdaRightMinus, formPart9, 4)

def part10(c, word):

    formPart10 = [c, "k", "n", "m > c + 1", 0, c + 1, 0]

    return algorithmMatchAndMove(c, word, moves.xRightMinus, formPart10, 3)

def part11(c, word):

    formPart11 = [c, "k", "n", "m < c", 0, c + 1, 0]

    return algorithmMatchAndMove(c, word, moves.xRightPlus, formPart11, 3)

"______________________________________________________________"

def part12(c, word):

    formPart12 = [c, 0, "n", "m", "n >= 1"]

    return algorithmMatchAndMove(c, word, moves.lambdaRightMinus, formPart12, 4)

def part13(c, word):

    formPart13 = [c, 0, "n", "m > c + 1", 0]

    return algorithmMatchAndMove(c, word, moves.xRightMinus, formPart13, 3)

def part14(c, word):

    formPart14 = [c, 0, "n", "m < c", 0]

    return algorithmMatchAndMove(c, word, moves.xRightPlus, formPart14, 3)
