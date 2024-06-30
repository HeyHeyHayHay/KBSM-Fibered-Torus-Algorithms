
from dataStructures import LinearCombination
from dataStructures import Word
from basisClassification import isBasis

def algorithmGeneral(c, basisNumber, algorithmFunction, linearCombination):

    basisCombination = LinearCombination([])

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
            newLinearCombination.addLinearCombination(changes)

        linearCombination = LinearCombination([])
        linearCombination.addLinearCombination(newLinearCombination)

    return basisCombination

    # loop through linearCombination until it is completely gone
    # or recurssively call algorithm on linear LinearCombination

        # if basis add to new linearcombination of basis
        # if not basis add back into linearCombination
