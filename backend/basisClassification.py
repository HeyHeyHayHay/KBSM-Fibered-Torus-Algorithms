
from .comparingWords import testThisXcForm

def isBasis(word, basisInformation):

    #print(1, lambdaOnly(word))
    #print(2, isBasisZeroXcCurve(word, basisNumber, c))
    #print(3, isBasiskXcCurve(word, basisNumber, c))
    isBasis = lambdaOnly(word) or isBasisZeroXcCurve(word, basisInformation) or isBasiskXcCurve(word, basisInformation)

    return isBasis

def lambdaOnly(word):
    isBasis = False

    XcCurveForm = word.XcCurveForm(0)
    isBasis = testThisXcForm(["c", 0, "n"], XcCurveForm)

    return isBasis

def isBasisZeroXcCurve(word, basisInformation):
    c = basisInformation.c
    basisNumber = basisInformation.basisNumber

    isBasis = False

    testList = listAfterLambdaZeroXcCurveForms(basisInformation)
    allXcForms = word.listAllXcCurveForms(c)

    for testForm in testList:
        for XcForm in allXcForms:
            isBasis = isBasis or testThisXcForm(testForm, XcForm)
            # short circuit
            if (isBasis == True):
                return True

    return isBasis

def listAfterLambdaZeroXcCurveForms(basisInformation):
    c = basisInformation.c
    basisNumber = basisInformation.basisNumber
    plusOrMinus = basisInformation.plusOrMinus

    listOfForms = []

    if (plusOrMinus == 1):
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

    if (plusOrMinus == -1):
        for i in range(basisNumber):
            afterLambdaLength = (i)*2

            baseFormC = [c, 0, "n", c, 0]
            baseFormCMinus = [c, 0, "n", c-1, 0]

            for k in range(afterLambdaLength):
                if (k%2 == 0):
                    baseFormC = baseFormC + [c-1]
                    baseFormCMinus = baseFormCMinus + [c-1]
                else:
                    baseFormC = baseFormC + [0]
                    baseFormCMinus = baseFormCMinus + [0]

            listOfForms.append(baseFormC)
            listOfForms.append(baseFormCMinus)

    return listOfForms

def isBasiskXcCurve(word, basisInformation):
    c = basisInformation.c
    isBasis = False

    testList = listAfterLambdaXcCurveForms(basisInformation)
    allXcForms = word.listAllXcCurveForms(c)

    for testForm in testList:
        for XcForm in allXcForms:
            isBasis = isBasis or testThisXcForm(testForm, XcForm)
            # short circuit
            if (isBasis == True):
                return True

    return isBasis

def listAfterLambdaXcCurveForms(basisInformation):
    c = basisInformation.c
    basisNumber = basisInformation.basisNumber
    plusOrMinus = basisInformation.plusOrMinus

    listOfForms = []

    if (plusOrMinus == 1):
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

    if (plusOrMinus == -1):
        baseFormC = [c, "k", "n", c, 0]
        baseFormCMinus = [c, "k", "n", c-1, 0]

        afterLambdaLength = (basisNumber)*2
        for k in range(afterLambdaLength):
            if (k%2 == 0):
                baseFormC = baseFormC + [c-1]
                baseFormCMinus = baseFormCMinus + [c-1]
            else:
                baseFormC = baseFormC + [0]
                baseFormCMinus = baseFormCMinus + [0]

        listOfForms.append(baseFormC)
        listOfForms.append(baseFormCMinus)

    return listOfForms
#testing
#print(listAfterLambdaXcForms(4, 0))
