
from dataStructures import Word
from dataStructures import LinearCombination
from dataStructures import XcFormToWord
import sympy
import basisClassification
import comparingWords
import algorithm0
from algorithmGeneral import algorithmGeneral

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')

# Testing Values

word1 = Word((0, 4, 0, 4, 0, 4, 0, 222, 14, -1, 4, 0, 0, 0, 0, 0), A**2 - A**-1)
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

word20 = Word((10, 5, 0, 4, 0), 4*A)
word21 = Word((10, 5, 0, 5, 0), 4*A)



combo = LinearCombination([word1, word2, word4, word5, word6, word7, word8, word9, word19, word20, word21, word22, word24, word25, word26])
#print(combo)

i = 0
for word in combo:
    currentWord = Word(word, combo.wordDict[word])
    print(currentWord)
    basis = basisClassification.isBasis(currentWord, 2, 4)

    """exampleC = False
    for possibleXForm in currentWord.listAllXcCurveForms(4):
        CForm = [4, "k", "n", "m < 4", 0]
        exampleC = exampleC or comparingWords.testXcForm(CForm, currentWord.XcCurveForm(4))
        print(possibleXForm)
    print(exampleC)"""
    print(basis)

print(word4)
#basis = basisClassification.isBasis(word4, 0, 4)

c = 4
testXcForm1 = [c, "k", "m >= -4", 4, 0, 5, 0]
testXcForm2 = [c, "k", "w"]

word99 = Word((0, 4, 0, 4, 0, 4, 0, 4, 1, 2), 1)

print(word99)
print(algorithm0.part7(c, word99))

print(algorithmGeneral(c, 0, algorithm0.part7, LinearCombination([word99])))
