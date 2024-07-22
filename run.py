from DictionaryAVLTree import dictionaryAVLTree, MINIMUM_WL, MAXIMUM_WL

WIDTH, HEIGHT = 6, 8
outputFile = open("strands_words.txt", "w")

# strandsArray = [[0 for x in range(w)] for y in range(h)]
strandsArray = [['a', 'w' ,'a', 'b', 'o', 'a'],
                ['l', 'd', 'n', 't', 'e', 'r'],
                ['o', 'o', 'g', 'e', 'l', 'd'],
                ['i', 'd', 'c', 'r', 'd', 'k'],
                ['n', 'r', 'p', 'a', 'd', 'a'],
                ['g', 'y', 'a', 'k', 'a', 'y'],
                ['h', 'd', 'f', 'n', 'o', 'e'],
                ['o', 'r', 'y', 't', 'a', 'c']]

# recursive function
# @Params
def searchLetter(currentString, row, col, usedLetters):
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
            outputFile.write(currentString + '\n')

    # all possible directions to check
    cardinalDirections = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    diagonalDirections = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    checkDiagonalDirections = [((-1, 0), (0, 1)), ((0, 1), (1, 0)), ((1, 0), (0, -1)), ((0, -1), (-1, 0))]

    for direction in cardinalDirections:
        newRow, newCol = row + direction[0], col + direction[1]
        searchNextCardinalLetter(currentString, newRow, newCol, usedLetters)
    
    for index, direction in enumerate(diagonalDirections):
        newRow, newCol = row + direction[0], col + direction[1]
        checkRow1, checkCol1 = row + checkDiagonalDirections[index][0][0], col + checkDiagonalDirections[index][0][1]
        checkRow2, checkCol2 = row + checkDiagonalDirections[index][1][0], col + checkDiagonalDirections[index][1][1]
        searchNextDiagonalLetter(currentString, newRow, newCol, usedLetters, checkRow1, checkCol1, checkRow2, checkCol2)


def searchNextCardinalLetter(currentString, row, col, usedLetters):
    # Makes sure it is a valid element in the 2D matrix and also it hasnt been used yet
    if isInBounds(row, col) and getId(row, col) not in usedLetters:
        usedLetters.add(getId(row, col))
        searchLetter(currentString + strandsArray[row][col], row, col, usedLetters)
        usedLetters.remove(getId(row, col))

def searchNextDiagonalLetter(currentString, row, col, usedLetters, checkRow1, checkCol1, checkRow2, checkCol2):
    # Makes sure it is a valid element in the 2D matrix and also hasnt been used yet and also makes sure that it wont be searching a letter that goes diagonal between two picked letters
    if isInBounds(row, col) and getId(row, col) not in usedLetters and not (getId(checkRow1, checkCol1) in usedLetters and getId(checkRow2, checkCol2) in usedLetters):
        usedLetters.add(getId(row, col))
        searchLetter(currentString + strandsArray[row][col], row, col, usedLetters)
        usedLetters.remove(getId(row, col))
    
def isInBounds(row, col):
    if (row < 0 or row >= len(strandsArray)) or (col < 0 or col >= len(strandsArray[0])):
        return False
    
    return True

def getId(row, col):
    return f"{strandsArray[row]}#{strandsArray[col]}"

def main():
    # For loop to iterate through strandsArray. Each element we do the algorithm
    for row in range(len(strandsArray)):
        for col in range(len(strandsArray[0])):
            searchLetter(strandsArray[row][col], row, col, {getId(row, col)})

main()
outputFile.close()

