
from . import dataStructures
from .dataStructures import Word
from .dataStructures import LinearCombination
from .dataStructures import XcFormToWord
from .dataStructures import basisInformation

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

w2 = XcFormToWord([2,5,4,5,2], A)
w4 = XcFormToWord([4,5,0,0,2], A + 4)

lc = LinearCombination([w2, w4])

print(lc)

print(LinearCombination.strLatex(lc))
