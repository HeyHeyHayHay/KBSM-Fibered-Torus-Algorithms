
from dataStructures import LinearCombination
from dataStructures import Word
from basisClassification import isBasis
from comparingWords import testWord
import moves
import multiprocessing
import dataStructures
from dataStructures import XcFormToWord
import sympy
import basisClassification
import comparingWords
import algorithm0Plus
import algorithm1
from algorithmGeneral import algorithmGeneral
import polyPQ

A = sympy.symbols('A')
lambda_ = sympy.symbols('lambda')

def algorithmGeneralMP(c, basisNumber, algorithmFunction, linearCombination):
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)

    linearCombination_chunks = [[] for _ in range(num_processes)]
    for i, (word, value) in enumerate(linearCombination.wordDict.items()):
        linearCombination_chunks[i % num_processes].append((word, value))

    results = pool.starmap(worker, [(c, basisNumber, algorithmFunction, chunk) for chunk in linearCombination_chunks])
    print(results)
    
    basisCombination = LinearCombination({})
    newLinearCombination = LinearCombination({})

    for basis_part, new_part in results:
        basisCombination.addLinearCombination(basis_part)
        newLinearCombination.addLinearCombination(new_part)

    pool.close()
    pool.join()

    return basisCombination

def worker(c, basisNumber, algorithmFunction, chunk):
    basisCombination = LinearCombination({})
    combinationToSubtract = LinearCombination({})

    for word in chunk:
        if isinstance(word, Word):
            currentWord = word
        else:
            currentWord = Word(*word)  # Assuming word is a tuple (letterTuple, coefficient)

        if isBasis(currentWord, basisNumber, c):
            basisCombination.addWord(currentWord)  # Add to basisCombination directly
            combinationToSubtract.addWord(currentWord)

    linearCombination_chunk = LinearCombination({word.letterTuple: word.coefficient for word in chunk if isinstance(word, Word)})
    linearCombination_chunk.subtractLinearCombination(combinationToSubtract)

    newLinearCombination = LinearCombination({})

    for word in linearCombination_chunk:
        currentWord = word
        changes = algorithmFunction(c, currentWord)
        newLinearCombination.addLinearCombination(changes)

    return basisCombination, newLinearCombination

def main():
    A = sympy.symbols('A')
    word1 = Word((0, 4, 0, 4, 0, 4, 0, 2, 1, -1, 4, 0, 0, 0, 0, 0), A**2 - A**-1)
    testCombination = LinearCombination([word1])

    result = algorithmGeneralMP(4, 0, algorithm0Plus.algorithm0Plus, testCombination)
    print(result)

if __name__ == '__main__':
    main()
