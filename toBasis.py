
from basisPlusConversionAlgorithm import createBasisPlusAlgorithm
from basisMinusConversionAlgorithm import createBasisMinusAlgorithm
from algorithm0Plus import algorithm0Plus
from algorithm0Minus import algorithm0Minus
from algorithmGeneral import algorithmGeneral

import dataStructures


def toBasis(basisInformation, linearCombination):
    c = basisInformation.c
    basisNumber = basisInformation.basisNumber
    plusOrMinus = basisInformation.plusOrMinus

    #print(dataStructures.basisInformation(0, c, plusOrMinus))

    if (plusOrMinus == 1):
        basisCombination = algorithmGeneral(dataStructures.basisInformation(0, c, plusOrMinus), algorithm0Plus, linearCombination)

    if (plusOrMinus == -1):
        basisCombination = algorithmGeneral(dataStructures.basisInformation(0, c, plusOrMinus), algorithm0Minus, linearCombination)

    #print(basisCombination)

    for step in range(basisNumber):
        nextBasisNumber = step + 1
        nextBasisInformation = dataStructures.basisInformation(nextBasisNumber, c, plusOrMinus)
        #print(nextBasisInformation)

        if (plusOrMinus == 1):
            transferAlgorithm = createBasisPlusAlgorithm(nextBasisNumber)
        if (plusOrMinus == -1):
            transferAlgorithm = createBasisMinusAlgorithm(nextBasisNumber)

        basisCombination = algorithmGeneral(nextBasisInformation, transferAlgorithm, basisCombination)

        #print(basisCombination)

    finalBasisCombination = basisCombination

    return finalBasisCombination
