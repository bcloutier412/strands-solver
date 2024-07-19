from DictionaryAVLTree import dictionaryAVLTree, MAXIMUM_WL

WIDTH, HEIGHT = 6, 8

# strandsArray = [[0 for x in range(w)] for y in range(h)]
strandsArray = [['e', 'h' ,'t', 'o', 'n', 'e'],
                ['s', 'w', 'r', 't', 's', 'c'],
                ['t', 'r', 'r', 'f', 'u', 'i'],
                ['e', 'n', 's', 'e', 't', 'r'],
                ['s', 'e', 'i', 'v', 'n', 'u'],
                ['t', 'i', 't', 'i', 'b', 'd'],
                ['e', 'n', 'w', 'o', 'r', 'u'],
                ['m', 'p', 'l', 'e', 'e', 'k']]

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
    


def isInBounds(row, col):
    if (row < 0 or row >= len(strandsArray)) or (col < 0 or col >= len(strandsArray[0])):
        return False
    
    return True

def main():
    # For loop to iterate through strandsArray. Each element we do the algorithm
    # for row in range(len(strandsArray)):
    #     for col in range(len(strandsArray[0])):
    #         searchLetter(strandsArray[row][col], row, col, {strandsArray[row][col]})
    
    print("searching: animal")
    print(dictionaryAVLTree.search_value("animal"))

    print("searching: ajdajdkaldk")
    print(dictionaryAVLTree.search_value("ajdajdkaldk"))

    print("searching: mert")
    print(dictionaryAVLTree.search_value("mert"))
    
# Check functions
# def checkRight(x, y):
#     return True or False

# def checkLeft(x, y):
#     return True or False

# def checkUp(x, y):
#     return True or False

# def checkDown(x, y):
#     return True or False

# def checkRightDiag(x,y):
#     return True or False

# def checkLeftDiag(x, y):
#     return True or False

main()

