
import dataStructures

def testWord(testXcForm, word):
    if (type(testXcForm[0]) == str):
        c = 0
    else:
        c = testXcForm[0]

    allPossibleXcForms = word.listAllXcCurveForms(c)

    for form in allPossibleXcForms:
        #print(form, testXcForm)
        if (testThisXcForm(testXcForm, form) == True):
            return form

    return False

def testThisXcForm(testXcForm, XcForm):

    match = True

    # w adjustment

    lastEntry = str(testXcForm[-1])

    if ( len(lastEntry) > 1 ):
        if ( "w" in lastEntry ):
            string = testXcForm.pop(-1)

            string = string.replace("w", '')

            numberOfX = int(string)

            numberOfW = 2*numberOfX + 1

            for i in range(numberOfW):
                testXcForm.append("w")


    # length Test

    match = match and lengthTest(testXcForm, XcForm)
    if (match == False):
        return False

    # string Test

    # pass c variable
    c = testXcForm[0]

    for index in range(len(testXcForm)):

        testEntry = testXcForm[index]
        trueEntry = XcForm[index]

        #print(index, testEntry, trueEntry, match)
        indexTest = individualTest(c, testEntry, trueEntry)

        match = indexTest and match

        #short circuit
        if (match == False):
            return False

    return match

def lengthTest(testXcForm, XcForm):
    match = True

    testLength = len(testXcForm)

    if testLength == 0:
        return False

    trueLength = len(XcForm)

    if (type(testXcForm[testLength - 1]) == str):
        if ( "w" in testXcForm[testLength - 1]):
            match = match and (testLength <= trueLength)
        else:
            match = match and (testLength == trueLength)
    else:
        match = match and (testLength == trueLength)

    return match

def individualTest(c, testEntry, trueEntry):

    indexTest = False

    if (type(testEntry) == int):
        indexTest = (testEntry == trueEntry);

    if (type(testEntry) == str):
        indexTest = stringTest(c, testEntry, trueEntry)

    return indexTest

def stringTest(c, testEntry, trueEntry):

    indexTest = False

    if (len(testEntry) == 1):
        indexTest = True
    else:
        indexTest = conditionTest(c, testEntry, trueEntry)

    return indexTest

def conditionTest(c, testEntry, trueEntry):

    indexTest = False

    if "n" in testEntry:
        testEntry = testEntry.replace("n", "trueEntry", 1)
        indexTest = indexTest or eval(testEntry)
    elif "k" in testEntry:
        testEntry = testEntry.replace("k", "trueEntry", 1)
        indexTest = indexTest or eval(testEntry)
    elif "m" in testEntry:
        testEntry = testEntry.replace("m", "trueEntry", 1)
        indexTest = indexTest or eval(testEntry)

    return indexTest
