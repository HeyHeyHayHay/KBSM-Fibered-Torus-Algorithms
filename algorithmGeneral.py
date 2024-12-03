
from dataStructures import LinearCombination
from dataStructures import Word
from basisClassification import isBasis
from comparingWords import testWord
import sympy
import moves


def algorithmGeneral(c, basisNumber, algorithmFunction, linearCombination):

    basisCombination = LinearCombination([])

    i = 1

    while (len(linearCombination) > 0):

        combinationToSubract = LinearCombination([])
        for word in linearCombination:
            currentWord = Word(word, linearCombination.wordDict[word])

            if (isBasis(currentWord, basisNumber, c) == True):
                basisCombination.addWord(currentWord)
                combinationToSubract.addWord(currentWord)

        linearCombination.subtractLinearCombination(combinationToSubract)

        newLinearCombination = LinearCombination([])

        for word in linearCombination:
            currentWord = Word(word, linearCombination.wordDict[word])

            changes = algorithmFunction(c, currentWord)
            #print("start:", currentWord, "\n", "change:", changes)
            newLinearCombination.addLinearCombination(changes)

        length = len(linearCombination)
        basisWords = len(basisCombination)

        linearCombination = LinearCombination([])
        linearCombination.addLinearCombination(newLinearCombination)

        #print("Next Step")
        if (i%100 == 0):
            print(" Step {} Length {} Basis Words {} \n{} Step {} Length {} Basis Words {} \n".format(i, length, basisWords, linearCombination, i, length, basisWords))

        i += 1

    # factor polynomials

    for word in basisCombination:
        basisCombination.wordDict[word] = sympy.factor(basisCombination.wordDict[word])

    return basisCombination

    # loop through linearCombination until it is completely gone
    # or recurssively call algorithm on linear LinearCombination

        # if basis add to new linearcombination of basis
        # if not basis add back into linearCombination


def algorithmMatchAndMove(c, word, moveFunction, formMatch, position):

    XcForm = testWord(formMatch, word)

    if (XcForm == False):
        return False

    wordStartCoefficient = word.coefficient

    linearCombination = moveFunction(XcForm, position, wordStartCoefficient)

    return linearCombination
