nRow = 1417
nCol = 48

class Node:
  def __init__(self):
    self.left = None
    self.right = None
    self.up = None
    self.down = None
    self.column = None
    self.rowID = None
    self.colID = None
    self.nodeCount = 0

header = Node()

Matrix = [[Node() for _ in range(nCol)] for _ in range(nRow)]

ProbMat = [[False for _ in range(nCol)] for _ in range(nRow)]

solutions = []

def getRight(i):
    return (i + 1) % nCol

def getLeft(i):
    return nCol - 1 if i - 1 < 0 else i - 1

def getUp(i):
    return nRow if i - 1 < 0 else i - 1

def getDown(i):
    return (i + 1) % (nRow + 1)

def createToridolMatrix():
    for i in range(nRow + 1):
       for j in range(nCol):
          if ProbMat[i][j]:
            a, b = None, None


            if i:
               Matrix[0][j].nodeCount += 1

            Matrix[i][j].column = Matrix[0][j]

            Matrix[i][j].rowID = i
            Matrix[i][j].colID = j

            # Left pointer
            a = i
            b = j
            while True:
                b = getLeft(b)
                if not ProbMat[a][b] and b != j:
                    continue
                break
        
            Matrix[i][j].left = Matrix[i][b]

            # Right pointer
            a = i
            b = j
            while True:
                b = getRight(b)
                if not ProbMat[a][b] and b != j:
                    continue
                break

            Matrix[i][j].right = Matrix[i][b]

            # Up pointer
            a = i
            b = j
            while True:
                a = getUp(a)
                if not ProbMat[a][b] and a != i:
                    continue
                break
            Matrix[i][j].up = Matrix[a][j]

            # Down pointer
            a = i
            b = j
            while True:
                a = getDown(a)
                if not ProbMat[a][b] and a != i:
                    continue
                break
            Matrix[i][j].down = Matrix[a][j]

    header.right = Matrix[0][0]

    header.left = Matrix[0][nCol - 1]

    Matrix[0][0].left = header
    Matrix[0][nCol - 1].right = header
    return header

def cover(targetNode):
    colNode = targetNode.column

    colNode.left.right = colNode.right
    colNode.right.left = colNode.left

    row = colNode.down
    while row != colNode:
        rightNode = row.right
        while rightNode != row:
            rightNode.up.down = rightNode.down
            rightNode.down.up = rightNode.up

            # after unlinking row node, decrement the node count in column header
            Matrix[0][rightNode.colID].nodeCount -= 1

            rightNode = rightNode.right
        row = row.down

def uncover(targetNode):
    colNode = targetNode.column

    rowNode = colNode.up
    while rowNode != colNode:
        leftNode = rowNode.left
        while leftNode != rowNode:
            leftNode.up.down = leftNode
            leftNode.down.up = leftNode

            # after linking row node, increment the node count in column header
            Matrix[0][leftNode.colID].nodeCount += 1

            leftNode = leftNode.left
        rowNode = rowNode.up

    # link the column header from its neighbors
    colNode.left.right = colNode
    colNode.right.left = colNode

def getMinColumn():
    h = header
    min_col = h.right

    h = h.right.right

    while True:
        if h.nodeCount < min_col.nodeCount:
            min_col = h
        h = h.right
        if h == header:
            break
    
    return min_col

def printSolutions():
    print("Printing Solutions:", end=" ")
    for node in solutions:
        print(node.rowID, end=" ")
    print()  # To move to a new line after printing all rowIDs

def search(k):
    if len(solutions) > 7:
        return
    
    if header.right == header:
        printSolutions()
        return
    
    column = getMinColumn()

    cover(column)

    rowNode = column.down
    while rowNode != column:
        solutions.append(rowNode)

        rightNode = rowNode.right
        while rightNode != rowNode:
            cover(rightNode)

            rightNode = rightNode.right

        search(k + 1)

        solutions.pop()

        column = rowNode.column

        leftNode = rowNode.left
        while leftNode != rowNode:
            uncover(leftNode)

            leftNode = leftNode.left
        rowNode = rowNode.down

    uncover(column)

def convertIDToIntegerMatrixPosition(ID):
    nums = ID.split("#")
    
    return (int(nums[0]) * 6) + int(nums[1])

def fillProbMat(possible_words):
    # Fill the Prob mat with all the words
    for index, word in enumerate(possible_words):
        for letterID in word:
            ProbMat[index + 1][convertIDToIntegerMatrixPosition(letterID)] = True
    
    return

def printProbMat():
    for i in range(nRow):
        for j in range(nCol):
            print(int(ProbMat[i][j]), end='')
        print()

# Initialize the problem matrix (2D list) with False (equivalent to 0)
ProbMat = [[False for _ in range(nCol)] for _ in range(nRow + 1)]

# Set the first row to True (equivalent to 1) for column headers
for j in range(nCol):
    ProbMat[0][j] = True


# # Manually filling up 1's (True values)
# # Maraca
# ProbMat[1][21] = True
# ProbMat[1][15] = True
# ProbMat[1][8] = True
# ProbMat[1][2] = True
# ProbMat[1][1] = True
# ProbMat[1][0] = True

# # Hairspray
# ProbMat[2][9] = True
# ProbMat[2][3] = True
# ProbMat[2][4] = True
# ProbMat[2][5] = True
# ProbMat[2][11] = True
# ProbMat[2][10] = True
# ProbMat[2][16] = True
# ProbMat[2][17] = True
# ProbMat[2][23] = True

# # Rattle
# ProbMat[3][19] = True
# ProbMat[3][12] = True
# ProbMat[3][6] = True
# ProbMat[3][7] = True
# ProbMat[3][14] = True
# ProbMat[3][13] = True

# # Shaken
# ProbMat[4][18] = True
# ProbMat[4][25] = True
# ProbMat[4][20] = True
# ProbMat[4][27] = True
# ProbMat[4][22] = True
# ProbMat[4][29] = True

# # Booty
# ProbMat[5][26] = True
# ProbMat[5][32] = True
# ProbMat[5][31] = True
# ProbMat[5][30] = True
# ProbMat[5][24] = True

# # Hands
# ProbMat[6][44] = True
# ProbMat[6][43] = True
# ProbMat[6][42] = True
# ProbMat[6][37] = True
# ProbMat[6][36] = True

# # Martini
# ProbMat[7][28] = True
# ProbMat[7][33] = True
# ProbMat[7][40] = True
# ProbMat[7][39] = True
# ProbMat[7][38] = True
# ProbMat[7][45] = True
# ProbMat[7][46] = True

# # Boat
# ProbMat[8][26] = True
# ProbMat[8][32] = True
# ProbMat[8][33] = True
# ProbMat[8][34] = True

# # Salt
# ProbMat[9][47] = True
# ProbMat[9][41] = True
# ProbMat[9][35] = True
# ProbMat[9][34] = True