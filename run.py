from DictionaryAVLTree import dictionaryAVLTree, MINIMUM_WL, MAXIMUM_WL

WIDTH, HEIGHT = 6, 8
outputFile = open("strands_words.txt", "w")

# strandsArray = [[0 for x in range(w)] for y in range(h)]
strandsArray = [['e', 'e' ,'e', 'o', 'l', 'e'],
                ['t', 'l', 'd', 'r', 't', 'r'],
                ['c', 'n', 't', 'n', 'e', 'd'],
                ['o', 'e', 'b', 'a', 'r', 'e'],
                ['k', 's', 'y', 'o', 'c', 's'],
                ['e', 'r', 'p', 'a', 'i', 'h'],
                ['t', 'u', 'r', 'n', 'e', 'f'],
                ['e', 'p', 'a', 'c', 's', 't']]

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
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for direction in directions:
        newRow, newCol = row + direction[0], col + direction[1]
        searchNextLetter(currentString, newRow, newCol, usedLetters)

def searchNextLetter(currentString, row, col, usedLetters):
    # Makes sure it is a valid element in the 2D matrix and also it hasnt been used yet
    if isInBounds(row, col) and getId(row, col) not in usedLetters:
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

