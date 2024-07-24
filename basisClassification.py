
from comparingWords import testThisXcForm

def isBasis(word, basisNumber, c):

    #print(1, lambdaOnly(word))
    #print(2, isBasisZeroXcCurve(word, basisNumber, c))
    #print(3, isBasiskXcCurve(word, basisNumber, c))
    isBasis = lambdaOnly(word) or isBasisZeroXcCurve(word, basisNumber, c) or isBasiskXcCurve(word, basisNumber, c)

    return isBasis

def lambdaOnly(word):
    isBasis = False

    XcCurveForm = word.XcCurveForm(0)
    isBasis = testThisXcForm(["c", 0, "n"], XcCurveForm)

    return isBasis

def isBasisZeroXcCurve(word, basisNumber, c):
    isBasis = False

    testList = listAfterLambdaZeroXcCurveForms(basisNumber, c)
    allXcForms = word.listAllXcCurveForms(c)

    for testForm in testList:
        for XcForm in allXcForms:
            isBasis = isBasis or testThisXcForm(testForm, XcForm)
            # short circuit
            if (isBasis == True):
                return True

    return isBasis

def listAfterLambdaZeroXcCurveForms(basisNumber, c):
    listOfForms = []

    for i in range(basisNumber):
        afterLambdaLength = (i)*2

        baseFormC = [c, 0, "n", c, 0]
        baseFormCPlus = [c, 0, "n", c+1, 0]

        for k in range(afterLambdaLength):
            if (k%2 == 0):
                baseFormC = baseFormC + [c+1]
                baseFormCPlus = baseFormCPlus + [c+1]
            else:
                baseFormC = baseFormC + [0]
                baseFormCPlus = baseFormCPlus + [0]

        listOfForms.append(baseFormC)
        listOfForms.append(baseFormCPlus)

    return listOfForms

def isBasiskXcCurve(word, basisNumber, c):
    isBasis = False

    testList = listAfterLambdaXcCurveForms(basisNumber, c)
    allXcForms = word.listAllXcCurveForms(c)

    for testForm in testList:
        for XcForm in allXcForms:
            isBasis = isBasis or testThisXcForm(testForm, XcForm)
            # short circuit
            if (isBasis == True):
                return True

    return isBasis

def listAfterLambdaXcCurveForms(basisNumber, c):
    listOfForms = []

    baseFormC = [c, "k", "n", c, 0]
    baseFormCPlus = [c, "k", "n", c+1, 0]

    afterLambdaLength = (basisNumber)*2
    for k in range(afterLambdaLength):
        if (k%2 == 0):
            baseFormC = baseFormC + [c+1]
            baseFormCPlus = baseFormCPlus + [c+1]
        else:
            baseFormC = baseFormC + [0]
            baseFormCPlus = baseFormCPlus + [0]

    listOfForms.append(baseFormC)
    listOfForms.append(baseFormCPlus)

    return listOfForms
#testing
#print(listAfterLambdaXcForms(4, 0))
