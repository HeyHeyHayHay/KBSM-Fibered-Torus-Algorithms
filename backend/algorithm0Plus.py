
from .comparingWords import testWord
from .dataStructures import XcFormToWord
from .dataStructures import LinearCombination
import sympy
from . import moves
from .algorithmGeneral import algorithmMatchAndMove

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')


#Lemma 3.3

def algorithm0Plus(c, word):

    listOfPartFunctions = [part1, part2, part3, part4, part5, part6, part7]

    for part in listOfPartFunctions:

        match = part(c, word)

        if (match != False):
            return match

    raise Exception("Word {} found no match".format(word))
    return False

# algorithm Lemma 3.3 basisNumber 0

def part1(c, word):

    formPart1 = [c, "k", "n >= 1", "m", "w", "w"]
    return algorithmMatchAndMove(c, word, moves.lambdaLeftMinus, formPart1, 2)

def part2(c, word):

    formPart2 = [c, "k", 0, "m > c + 1", "w", "w"]
    return algorithmMatchAndMove(c, word, moves.xLeftMinus, formPart2, 3)

def part3(c, word):

    formPart3 = [c, "k", 0, "m < c", "w", "w"]
    return algorithmMatchAndMove(c, word, moves.xLeftPlus, formPart3, 3)

def part4(c, word):

    formPart4 = [c, "k", 0, c + 1, "n", "m", "w"]
    return algorithmMatchAndMove(c, word, moves.lambdaReducePlus, formPart4, 4)

def part5(c, word):

    formPart5 = [c, "k", "n", "m", "n >= 1"]
    return algorithmMatchAndMove(c, word, moves.lambdaRightMinus, formPart5, 4)

def part6(c, word):

    formPart6 = [c, "k", "n", "m > c + 1", 0]
    return algorithmMatchAndMove(c, word, moves.xRightMinus, formPart6, 3)

def part7(c, word):

    formPart7 = [c, "k", "n", "m < c", 0]
    return algorithmMatchAndMove(c, word, moves.xRightPlus, formPart7, 3)
