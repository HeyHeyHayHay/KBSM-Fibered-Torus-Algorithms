
#tests to classify words


#any Basis
#original basis is designated with Basis Number 0
def isBasis(word, basisNumber, c):

    print(1, lambdaOnly(word))
    print(2, isBasisZeroXcCurve(word, basisNumber, c))
    print(3, isBasiskXcCurve(word, basisNumber, c))
    isBasis = lambdaOnly(word) or isBasisZeroXcCurve(word, basisNumber, c) or isBasiskXcCurve(word, basisNumber, c)

    return isBasis

def lambdaOnly(word):
    isBasis = False
    letterTuple = word.letterTuple

    if (type(letterTuple) == int):
        isBasis = True

    return isBasis

def testAfterLambda(letterTuple, c, lambdaIndex, numberOfXCurvesAfterLambda):
    possibleBasis = True

    if (numberOfXCurvesAfterLambda == 0):
        return False

    trueAfterLambdaLength = len(letterTuple) - (lambdaIndex + 1)
    expectedLength = numberOfXCurvesAfterLambda * 2

    if (trueAfterLambdaLength != expectedLength):
        return False

    indexToCheck = lambdaIndex + 1
    if ( (letterTuple[indexToCheck] != c) and (letterTuple[indexToCheck] != c+1) ):
        return False

    indexToCheck = indexToCheck + 1

    while (indexToCheck < lambdaIndex + numberOfXCurvesAfterLambda*2 + 1):

        if ( indexToCheck%2 == 0 ):
            if (letterTuple[indexToCheck] != 0):
                return False
        else:
            if (letterTuple[indexToCheck] != c+1):
                return False

        indexToCheck += 1

    return possibleBasis

def isBasisZeroXcCurve(word, basisNumber, c):
    isBasis = True
    letterTuple = word.letterTuple

    XcCurveForm = word.XcCurveForm(c)

    if (XcCurveForm[1] != 0):
        return False

    maxLengthOfXcForm = 2 + 1 + 2*basisNumber

    if (len(XcCurveForm) > maxLengthOfXcForm):
        return False

    # index 2 can be anything: lambda n
    startIndex = 2

    XcCurvesAfterLambda = int(len(XcCurveForm) / 2) - 1

    isBasis = testAfterLambda(letterTuple, c, 2, XcCurvesAfterLambda)
    """    for index in range(startIndex, len(XcCurveForm)):
        if (index == 3):
            if (XcCurveForm[index] != c and (XcCurveForm[index] != c+1) ):
                return False
        elif (index%2 == 1):
            if (XcCurveForm[index] != c+1):
                return False
        else:
            if (XcCurveForm[index] != 0 ):
                return False"""

    return isBasis

def isBasiskXcCurve(word, basisNumber, c):
    isBasis = False
    letterTuple = word.letterTuple

    maxXcCurve = word.numOfStartingXcCurves(c)

    if ( type(letterTuple) == int):
        lengthOfWord = 1
    else:
        lengthOfWord = len(letterTuple)

    for k in range(0, maxXcCurve + 1):
        # index k*2 can be any lambda n
        startIndex = k*2
        restOfXCurves = int( (lengthOfWord-1) / 2) - k

        passAfterLambdaTest = False
        if (restOfXCurves == basisNumber + 1):
            passAfterLambdaTest = testAfterLambda(letterTuple, c, startIndex, restOfXCurves)

        isBasis = isBasis or passAfterLambdaTest

    return isBasis
