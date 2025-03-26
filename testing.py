
import dataStructures
from dataStructures import Word
from dataStructures import LinearCombination
from dataStructures import XcFormToWord
from dataStructures import basisInformation

import sympy
import basisClassification
import comparingWords
import algorithm0Plus
import algorithm0Minus
import basisPlusConversionAlgorithm
import basisMinusConversionAlgorithm
from basisClassification import isBasis
import basisClassification
from toBasis import toBasis

from algorithmGeneral import algorithmGeneral
import moves
import polyPQ

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')

# Testing Values

word1 = Word((0, 4, 0, 4, 1, 4, 0, 2, 1, -1, 4, 0, 0), 1)
word2 = Word((0, 4, 0), 2*A)
word4 = Word((0, 4, 1), 4*A)
word5 = Word((10), 2*A)
word6 = Word((10, 2, 0), 4*A)
word7 = Word((10, 4, 1), 4*A)
word8 = Word((10, 5, 0), 4*A)
word9 = Word((0, 4, 0, 4, 0, 4, 0, 5, 0, 5, 0), 4*A)
word19 = Word((0, 4, 0, 4, 0, 4, 0, 4, 0, 5), 4*A)
word22 = Word((0, 4, 0, 4, 0, 4, 0, 5, 1, 5, 0), 4*A)
word24 = Word((0, 4, 0, 4, 0, 4, 0, 4, 1, 5), 4*A)
word25 = Word((0, 4, 0, 4, 0, 4, 1, 4, 1, 5), 4*A)
word26 = Word((0, 4, 0, 4, 0, 4, 1, 4, 0, 5), 4*A)
word27 = Word((0, 4, 0, 4, 0, 4, 0, 5, 0, 5, 1), 4*A)
word28 = Word((0, 4, 0, 5, 1, 4, 1), 1)

word20 = Word((10, 5, 0, 4, 0), 4*A)
word21 = Word((0, 4, 0, 3, 2, 5), 4*A)



combo = LinearCombination([word1, word2, word4, word5, word6, word7, word8, word9, word19, word20, word21, word22, word24, word25, word26])

word99 = Word((0, 4, 0, 4, 0, 4, 0, 4, 1, 4, 2), 1)
word100 = Word((0, 4, 1, 4, 0, 5, 0, 5, 0, 5, 0), A)
word101 = Word((0, 4, 0, 4, 2, 5, 0), 1)
word102 = Word((0, 4, 1, 4, 0, 3, 0, 3, 0), A)


t = LinearCombination([word101])
testCombination = LinearCombination([word102])
print("_________________")

print(testCombination)

c = 1
sigmaZeroOneNegative = basisInformation(0, 1, -1)
sigmaThreeFourPositive = basisInformation(3, 4, 1)
sigmaThreeFourNegative = basisInformation(3, 4, -1)

print(sigmaThreeFourPositive)

print(basisClassification.isBasis(word100, sigmaThreeFourPositive))
print(basisClassification.isBasis(word102, sigmaThreeFourNegative))

basis0test = algorithmGeneral(basisInformation(0, 4, -1), algorithm0Minus.algorithm0Minus, testCombination)

matchTst = toBasis(basisInformation(2, 4, -1), testCombination)
