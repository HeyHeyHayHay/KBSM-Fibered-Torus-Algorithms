
import sympy
import fancyPrinting as fp
from colorama import Fore, Style, init
import math


A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')

init(autoreset=True)

class Word:
    def __init__(self, letterTuple, coefficient):

        if ((type(letterTuple) != int) and len(letterTuple)%2 == 0):
            print("Word has even letters: 0 lambda will be added")
            letterList = list(letterTuple)
            letterList.append(0)
            letterTuple = tuple(letterList)

        self.letterTuple = letterTuple
        self.coefficient = sympy.expand(coefficient)

    def __str__(self):

        array = self.letterTuple

        wordString = ""

        if ( type(array) == int ):
            wordString = fp.lambda_unicode + fp.to_superscript(array) + wordString
        else:
            for i in range(len(array)):
                if (i%2 == 0):
                    if (array[i] != 0):
                        wordString = fp.lambda_unicode + fp.to_superscript(array[i]) + wordString
                if (i%2 == 1):
                    wordString = fp.fancy_x_unicode + fp.to_subscript(array[i]) + wordString

        #factor coefficient
        #self.coefficient = sympy.factor(self.coefficient)

        return f"{Fore.GREEN}({self.coefficient}) {Fore.BLACK}{wordString}"

    def strLatex(self):

        array = self.letterTuple

        wordString = ""

        if ( type(array) == int ):
            wordString = "\lambda^{" + str(array) + "}" + wordString
        else:
            for i in range(len(array)):
                if (i%2 == 0):
                    if (array[i] != 0):
                        wordString = "\lambda^{" + str(array[i]) + "}" + wordString
                if (i%2 == 1):
                    wordString = "x_{" + str(array[i]) + "}" + wordString

        coefficientLatex = sympy.latex(self.coefficient)

        if self.coefficient == 1:
            return wordString
            # Handle negative coefficients
        elif self.coefficient == -1:
            return f"-{wordString}"
        else:
            return f"{coefficientLatex} {wordString}"

    def numOfXCurves(self):
        return math.floor( len(self.letterTuple) / 2 )

    def numOfStartingXcCurves(self, c):
        numOfStartingXcCurves = 0
        i = 0

        # only lambda case
        if (type(self.letterTuple) == int):
            return 0

        while ( i < len(self.letterTuple) ):
            if (i%2 == 0):
                # lambda curve
                if ( self.letterTuple[i] != 0 ):
                    return numOfStartingXcCurves
            else:
                # x curve
                if ( self.letterTuple[i] == c):
                    numOfStartingXcCurves += 1
                else:
                    return numOfStartingXcCurves
            i += 1

        return numOfStartingXcCurves

    def indexAfterXcCurves(self, c):
        numOfStartingXcCurves = self.numOfStartingXcCurves(c)
        return 2*numOfStartingXcCurves

    def XcCurveForm(self, c):
        # [ c value , numOfStartingXcCurves, continue normally]
        XcCurveList = [c]
        letterTuple = self.letterTuple

        if (type(letterTuple) == int):
            XcCurveList.append(0)
            XcCurveList.append(letterTuple)
            return XcCurveList
        else:
            XcCurveList.append( self.numOfStartingXcCurves(c) )
            i = self.indexAfterXcCurves(c)
            while i < len(letterTuple):
                XcCurveList.append( letterTuple[i] )
                i += 1
            return XcCurveList

    def listAllXcCurveForms(self, c):
        list = []
        numOfStartingXcCurves = self.numOfStartingXcCurves(c)

        for k in range(numOfStartingXcCurves, -1, -1):
                XcCurveList = [c]
                letterTuple = self.letterTuple

                if (type(letterTuple) == int):
                    XcCurveList.append(0)
                    XcCurveList.append(letterTuple)
                    list.append(XcCurveList)
                else:
                    XcCurveList.append( k )
                    i = 2*k
                    while i < len(letterTuple):
                        XcCurveList.append( letterTuple[i] )
                        i += 1
                    list.append(XcCurveList)
        return list

    def multiplyCoefficient(self, coefficient):
        self.coefficient = sympy.expand(self.coefficient * coefficient)
        return self

class LinearCombination:
    def __init__(self, listOfWords):

        wordDict = {}
        for word in listOfWords:
            wordDict[word.letterTuple] = sympy.expand(wordDict.get(word.letterTuple, 0) + word.coefficient)
        self.wordDict = wordDict
        self.removeZeros()

    def __iter__(self):
        return iter(self.wordDict)

    def __next__(self):
        return next(self.wordDict)

    def __str__(self):

        linearCombinationString = ""
        wordList = (self.wordDict).items()

        i = 0
        for word in self.wordDict:
            currentWord = Word(word, self.wordDict[word])
            if (i == 0):
                linearCombinationString = linearCombinationString + "   " + str(currentWord)
            else:
                linearCombinationString = linearCombinationString + " + " + str(currentWord)
            linearCombinationString += "\n"
            i += 1

        return linearCombinationString

    def __len__(self):
        return len(self.wordDict)

    def strLatex(self):

        linearCombinationString = ""
        wordList = (self.wordDict).items()

        i = 0
        for word in self.wordDict:
            currentWord = Word(word, self.wordDict[word])
            if (i == 0):
                linearCombinationString = linearCombinationString + "   " + Word.strLatex(currentWord)
            else:
                linearCombinationString = linearCombinationString + " + " + Word.strLatex(currentWord)
            linearCombinationString += "\n"
            i += 1

        return linearCombinationString


    def removeZeros(self):
        wordsWithZeroCoefficient = []
        for word in self.wordDict:
            if (self.wordDict[word] == 0):
                wordsWithZeroCoefficient.append(word)
        for word in wordsWithZeroCoefficient:
            self.wordDict.pop(word)

        pass

    def addWord(self, word):
        self.wordDict[word.letterTuple] = sympy.expand(self.wordDict.get(word.letterTuple, 0) + word.coefficient)
        self.removeZeros()
        return self

    def subtractWord(self, word):
        self.wordDict[word.letterTuple] = sympy.expand(self.wordDict.get(word.letterTuple, 0) - word.coefficient)
        self.removeZeros()
        return self

    def addLinearCombination(self, linearCombinationAddend):
        if (len(linearCombinationAddend) == 0):
            return self
        for word in linearCombinationAddend:
            currentWord = Word(word, linearCombinationAddend.wordDict[word])
            self.addWord(currentWord)
        return self

    def subtractLinearCombination(self, linearCombinationSubtrahend):
        for word in linearCombinationSubtrahend:
            currentWord = Word(word, linearCombinationSubtrahend.wordDict[word])
            self.subtractWord(currentWord)
        return self

    def popWord(self, word):
        return self.wordDict.pop(word.letterTuple)

    def multiplyCoefficient(self, coefficient):
        for word in self.wordDict:
            self.wordDict[word] = sympy.expand(self.wordDict[word] * coefficient)
        self.removeZeros()
        return self

class basisInformation:
    def __init__(self, basisNumber, c, plusOrMinus):

        self.basisNumber = basisNumber
        self.c = c
        self.plusOrMinus = plusOrMinus

    def __str__(self):

        stats = "basisNumber:" + str(self.basisNumber) + " c:" + str(self.c) + " plusOrMinus:" + str(self.plusOrMinus)
        return stats
#
def XcFormToWord(XcForm, coefficient):

    letterList = []
    c = XcForm[0]
    k = XcForm[1]

    for i in range(k*2):
        if (i%2 == 1):
            letterList.append(c)
        else:
            letterList.append(0)

    for i in range(2, len(XcForm)):
        letterList.append(XcForm[i])

    if (len(letterList)%2 == 0):
        letterList.append(0)

    letterTuple = tuple(letterList)

    word = Word(letterTuple, coefficient)
    return word
