
import re
from . import dataStructures
from collections import defaultdict
import sympy

def laTeXToLinearCombination(latexText):
    # Step 1: Split into individual terms (handling parentheses)
    terms = []
    current_term = ""
    paren_level = 0
    for char in latexText:
        if char == '(':
            paren_level += 1
        elif char == ')':
            paren_level -= 1
        elif char == '+' and paren_level == 0:
            terms.append(current_term.strip())
            current_term = ""
            continue
        current_term += char
    if current_term:
        terms.append(current_term.strip())

    # Step 2: Process each term
    words = []
    for t in terms:
        # Handle coefficient
        if t.startswith('('):
            # Complex coefficient case
            coeff_end = t.find(')') + 1
            coeff = t[:coeff_end]
            word_part = t[coeff_end:].strip()
        else:
            # Simple coefficient case
            match = re.match(r'^([A-Z0-9^+-]+)', t)
            if match:
                coeff = match.group(1)
                word_part = t[len(coeff):].strip()
            else:
                coeff = '1'  # Default coefficient
                word_part = t

        # Normalize the word part
        normalized_word = normalizeLatex(word_part)
        numbers = extractNumbers(normalized_word)
        xc_form = digitStringToArray(numbers)

        words.append((xc_form, coeff))

    # Step 3: Combine like terms
    word_dict = defaultdict(lambda: sympy.sympify(0))
    for xc_form, coeff in words:
        word_dict[tuple(xc_form)] += sympy.sympify(coeff)

    # Step 4: Create LinearCombination
    return dataStructures.LinearCombination([
        dataStructures.XcFormToWord(list(xc_form), str(coeff_expr))
        for xc_form, coeff_expr in word_dict.items()
        if coeff_expr != 0
    ])

def normalizeLatex(word):
    # Rule 3: Convert bare \lambda to \lambda^{1}
    word = re.sub(r'\\lambda(?!\^)', r'\\lambda^{1}', word)

    # Rule 1: Insert \lambda^{0} between x_{m} terms
    word = re.sub(r'(x_\{\-?\d+\})(?![^}]*\^)(?!\\lambda)', r'\1\\lambda^{0}', word)

    # Rule 2: Add (x_0)^0 if missing
    if not re.search(r'\(x_\{\d+\}\)\^', word):
        word += '(x_{0})^{0}'

    return word

def extractNumbers(normalizedStr):
    # Matches both positive and negative multi-digit numbers
    numbers = re.findall(r'-?\d+', normalizedStr)
    return numbers  # Returns list of strings (to preserve negatives)

def digitStringToArray(numberList):
    numbers = [int(num) for num in numberList]
    if len(numbers) >= 2:
        numbers[-2], numbers[-1] = numbers[-1], numbers[-2]
    return numbers[::-1]
