
from dataStructures import LinearCombination
from dataStructures import Word
from basisClassification import isBasis
from comparingWords import testWord
import moves


def algorithmGeneral(c, basisNumber, algorithmFunction, linearCombination):

    basisCombination = LinearCombination([])

    i = -1

    while (len(linearCombination) > 0):

        i += 1
        if (i%4 == 0):
            print(" Step {} Length {} \n{} Step {} Length {}\n".format(i, len(linearCombination), linearCombination, i, len(linearCombination)))

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
            newLinearCombination.addLinearCombination(changes)

        linearCombination = LinearCombination([])
        linearCombination.addLinearCombination(newLinearCombination)

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
