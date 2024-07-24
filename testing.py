
import dataStructures
from dataStructures import Word
from dataStructures import LinearCombination
from dataStructures import XcFormToWord
import sympy
import basisClassification
import comparingWords
import algorithm0
import algorithm1
import basisConversionAlgorithm
from basisClassification import isBasis
import basisClassification

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

#basis = basisClassification.isBasis(word4, 0, 4)

c = 4
testXcForm1 = [c, "k", "m >= -4", 4, 0, 5, 0]
testXcForm2 = [c, "k", "w"]

word99 = Word((0, 4, 0, 4, 0, 4, 0, 4, 1, 4, 2), 1)
word100 = Word((0, 4, 0, 4, 1, 4, 0), 1)
word101 = Word((0, 4, 0, 4, 2, 5, 0), 1)


t = LinearCombination([word100, word101])
testCombination = LinearCombination([word100, word101])
print("_________________")

print(testCombination)



basis0test = algorithmGeneral(c, 0, algorithm0.algorithm0, testCombination)
testCombination = LinearCombination([word100, word101])

basis1Direct = algorithmGeneral(c, 1, algorithm1.algorithm1, testCombination)

print("basis0", basis0test)
print("basis1", basis1Direct)

print("____TRANSFeR_____")

basisTransferAlgorithmTest = basisConversionAlgorithm.createBasisAlgorithm(1)

basis1Transfer = algorithmGeneral(c, 1, basisTransferAlgorithmTest, basis0test)

"""
print(basis0test)
print(basis1Direct)
print(basis1Transfer)
"""


print(basis1Transfer)

print("____TRANSFeR 2_____")

basisTransferAlgorithmTest2 = basisConversionAlgorithm.createBasisAlgorithm(2)

basis2Transfer = algorithmGeneral(c, 2, basisTransferAlgorithmTest2, basis1Transfer)

print(basis2Transfer)

print("____TRANSFeR 2_____")

basisTransferAlgorithmTest3 = basisConversionAlgorithm.createBasisAlgorithm(3)

basis3Transfer = algorithmGeneral(c, 3, basisTransferAlgorithmTest3, basis2Transfer)

print(basis3Transfer)
