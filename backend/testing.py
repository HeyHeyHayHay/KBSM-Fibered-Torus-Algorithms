
from . import dataStructures
from .dataStructures import Word
from .dataStructures import LinearCombination
from .dataStructures import XcFormToWord
from .dataStructures import basisInformation

import sympy
from . import basisClassification
from . import comparingWords
from . import algorithm0Plus
from. import algorithm0Minus
from. import basisPlusConversionAlgorithm
from . import basisMinusConversionAlgorithm
from .basisClassification import isBasis
from . import basisClassification
from .toBasis import toBasis

from .algorithmGeneral import algorithmGeneral
from . import moves
from . import polyPQ

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')

w2 = XcFormToWord([0,0,0,5,1,4], A)
w4 = XcFormToWord([2,4], A**-1)

lc = LinearCombination([w2, w4])

print(lc)

print(LinearCombination.strLatex(lc))

print(toBasis(basisInformation(0,2,-1), lc))
