from src.DictionaryAVLTree import dictionaryAVLTree, MINIMUM_WL, MAXIMUM_WL
from DLX import nRow, nCol, createToridolMatrix, search, ProbMat, fillProbMat, printProbMat

WIDTH, HEIGHT = 6, 8
outputFile = open("strands_words.txt", "w")

# strandsArray = [[0 for x in range(w)] for y in range(h)]
strandsArray = [['r', 'o' ,'u', 's', 'l', 'u'],
                ['e', 'p', 'f', 'f', 'n', 'e'],
                ['o', 's', 'a', 't', 'c', 'h'],
                ['r', 't', 's', 'r', 'i', 'w'],
                ['p', 'a', 'o', 'y', 'a', 'e'],
                ['t', 'h', 'p', 'h', 't', 'l'],
                ['e', 'l', 'u', 'm', 'd', 'e'],
                ['n', 't', 'o', 'n', 'e', 'y']]
totalWords = 7
# strandsArray = [
#     ['t', 'h', 'i', 's'],
#     ['w', 'a', 't', 's'],
#     ['o', 'a', 'h', 'g'],
#     ['f', 'g', 'd', 't']
# ]

# Backtracking recursive function to find words in 2D Matrix
# @Params
def searchLetter(currentString, row, col, usedLettersSet, usedLettersArray, possibleWords):
    # Check if the row and col is in bounds if its not then return false
    if not isInBounds(row, col):
        return

    # if the string is too long then just return
    if len(currentString) + 1 >= MAXIMUM_WL:
        return
    
    # 3 Possible conditions:
    #   1. Got to end of tree
    #   2. Found a sub string
    #   3. Found a word

    # If the word is less than the minimum then dont check and just process the next possible letter
    if len(currentString) >= MINIMUM_WL:
        searchResults = dictionaryAVLTree.search_value(currentString)
    
        if searchResults['isSubString'] == False:
            return
        elif searchResults['isWord'] == True:
            possibleWords.append(usedLettersArray.copy())
            outputFile.write(currentString + '\n')

    # all possible directions to check
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

    for direction in directions:
        newRow, newCol = row + direction[0], col + direction[1]
        searchNextLetter(currentString, newRow, newCol, usedLettersSet, usedLettersArray, possibleWords)

def searchNextLetter(currentString, row, col, usedLettersSet, usedLettersArray, possibleWords):
    # Makes sure it is a valid element in the 2D matrix and also it hasnt been used yet
    if isInBounds(row, col) and getId(row, col) not in usedLettersSet:
        usedLettersSet.add(getId(row, col))
        usedLettersArray.append(getId(row, col))

        searchLetter(currentString + strandsArray[row][col], row, col, usedLettersSet, usedLettersArray, possibleWords)

        usedLettersSet.remove(getId(row, col))
        usedLettersArray.remove(getId(row, col))

# Backtracking recursive function to complete the 2D matrix with words
def completeMatrix(start, usedLettersSet, usedWords, completedMatrixWords, possibleWords, matrixArea, totalWords, currentTotalWords):
    print(usedWords)
    if len(usedLettersSet) == matrixArea:
        completedMatrixWords.append(usedWords.copy())
        return
    
    if currentTotalWords >= totalWords:
        return
    
    if len(usedWords) >= totalWords:
        return
    
    if len(usedLettersSet) > matrixArea:
        return
    
    for index in range(start, len(possibleWords)):
        # Check that non of the letters in this word are in the usedLettersSet
        word = possibleWords[index]
        if all(letter not in usedLettersSet for letter in word):
            for letter in word:
                usedLettersSet.add(letter)
            usedWords.append(word)
            
            if completeMatrix(index + 1, usedLettersSet, usedWords, completedMatrixWords, possibleWords, matrixArea, totalWords, currentTotalWords + 1):
                return True  # Early termination if one solution is sufficient
            
            usedWords.pop()
            for letter in word:
                usedLettersSet.remove(letter)
                


# Helper Functions
def isInBounds(row, col):
    if (row < 0 or row >= len(strandsArray)) or (col < 0 or col >= len(strandsArray[0])):
        return False
    
    return True

def getId(row, col):
    return f"{row}#{col}"

# Main
def main():
    # For loop to iterate through strandsArray. Each element we do the algorithm
    possibleWords = []
    for row in range(len(strandsArray)):
        for col in range(len(strandsArray[0])):
            searchLetter(strandsArray[row][col], row, col, {getId(row, col)}, [getId(row, col)], possibleWords)

    fillProbMat(possibleWords)
    # printProbMat()

    # Create 4-way linked matrix
    createToridolMatrix()

    # Search starting at level 0
    search(0)

main()
outputFile.close()

