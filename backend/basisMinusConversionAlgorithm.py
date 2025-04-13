
from .comparingWords import testWord
from .dataStructures import XcFormToWord
from .dataStructures import LinearCombination
import sympy
from . import moves
from .algorithmGeneral import algorithmMatchAndMove

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')


def createBasisMinusAlgorithm(destinationBasisNumber):

    #Lemma 3.3

    def basisMinusConversionAlgorithm(c, word):

        listOfPartFunctions = [part1, part2, part3, part4, part5, part6, part7, part8, part9, part10, part11, part12]

        for part in listOfPartFunctions:

            match = part(c, word)

            if (match != False):
                return match

        raise Exception("Word {} found no match".format(word))
        return False

    # algorithm Lemma 3.3 basisNumber 0



    def part1(c, word):
        #print(1)
        formPart1 = [c, "k", 0, "m", "n >= 1", c - 1, 0, f"{destinationBasisNumber - 1}w"]
        return algorithmMatchAndMove(c, word, moves.lambdaRightMinus, formPart1, 4)

    def part2(c, word):
        #print(2)

        formPart2 = [c, "k", "n", "m > c", 0, c - 1, 0, f"{destinationBasisNumber - 1}w"]
        return algorithmMatchAndMove(c, word, moves.xRightMinus, formPart2, 3)

    def part3(c, word):
        #print(3)

        formPart3 = [c, "k", "n", "m < c - 1", 0, c - 1, 0, f"{destinationBasisNumber - 1}w"]
        return algorithmMatchAndMove(c, word, moves.xRightPlus, formPart3, 3)

    def part4(c, word):
        #print(4)

        formPart4 = [c, "k", 0, c, "n", c, 0, f"{destinationBasisNumber - 1}w"]
        return algorithmMatchAndMove(c, word, moves.lambdaReduceMinus, formPart4, 4)

    # _____________________________________________________________

    def part5(c, word):
        #print(5)

        formPart5 = [c, "k", 0, "m", "n >= 1", c - 1, "w"]
        return algorithmMatchAndMove(c, word, moves.lambdaRightMinus, formPart5, 4)

    def part6(c, word):
        #print(6)

        formPart6 = [c, "k", "n", "m > c", 0, c - 1, "w"]
        return algorithmMatchAndMove(c, word, moves.xRightMinus, formPart6, 3)

    def part7(c, word):
        #print(7)

        formPart7 = [c, "k", "n", "m < c - 1", 0, c - 1, "w"]
        return algorithmMatchAndMove(c, word, moves.xRightPlus, formPart7, 3)

    def part8(c, word):
        #print(8)

        formPart8 = [c, "k", 0, "m", "n >= 1"]
        return algorithmMatchAndMove(c, word, moves.lambdaRightMinus, formPart8, 4)

    def part9(c, word):
        #print(9)

        formPart9 = [c, "k", "n", "m > c", 0]
        return algorithmMatchAndMove(c, word, moves.xRightMinus, formPart9, 3)

    def part10(c, word):
        #print(10)

        formPart10 = [c, "k", "n", "m < c - 1", 0]
        return algorithmMatchAndMove(c, word, moves.xRightPlus, formPart10, 3)

    def part11(c, word):
        #print(11)

        formPart11 = [c, 0, "n", "m > c", 0]
        return algorithmMatchAndMove(c, word, moves.xRightMinus, formPart11, 3)

    def part12(c, word):
        #print(12)

        formPart12 = [c, 0, "n", "m < c - 1", 0]
        return algorithmMatchAndMove(c, word, moves.xRightPlus, formPart12, 3)


    return basisMinusConversionAlgorithm
