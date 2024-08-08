from AVLTree import Node, AVLTree
from utils import convert_row_col_to_id, is_in_matrix_bound, get_relative_file_path
import sys

class MatrixWordFinder:
    def __init__(
        self,
        WIDTH,
        HEIGHT,
        MINIMUM_WL,
        MAXIMUM_WL,
        gameboard,
        total_words_to_complete_matrix,
        possible_words,
        dictionary_avl_tree
    ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.MINIMUM_WL = MINIMUM_WL
        self.MAXIMUM_WL = MAXIMUM_WL
        self.gameboard = gameboard
        self.total_words_to_complete_matrix = total_words_to_complete_matrix
        self.dictionary_avl_tree = dictionary_avl_tree
        self.possible_words = possible_words
        self.return_char = "0"
        self.outputFile = open(get_relative_file_path("../text_files/strands_words.txt"), "w")

    def __del__(self):
        self.outputFile.close()
    
    def search_letter(self, currentString, row, col, usedLettersSet, usedLettersArray):
        # Check if the row and col is in bounds if its not then return false
        if not is_in_matrix_bound(row, col, self.HEIGHT, self.WIDTH):
            return
        
        # if the string is too long then just return
        if len(currentString) + 1 >= self.MAXIMUM_WL:
            return
        
        # If the word is less than the minimum then dont check and just process the next possible letter
        if len(currentString) >= self.MINIMUM_WL:
            searchResults = self.dictionary_avl_tree.search_value(currentString)

            if searchResults['isSubString'] == False:
                return
            elif searchResults['isWord'] == True:
                self.possible_words.append(usedLettersArray.copy())
                self.outputFile.write(currentString + '\n')

        def search_next_letter(currentString, row, col, usedLettersSet, usedLettersArray):
            # Makes sure it is a valid element in the 2D matrix and also it hasnt been used yet
            if is_in_matrix_bound(row, col, self.HEIGHT, self.WIDTH) and convert_row_col_to_id(row, col) not in usedLettersSet:
                usedLettersSet.add(convert_row_col_to_id(row, col))
                usedLettersArray.append(convert_row_col_to_id(row, col))

                self.search_letter(currentString + self.gameboard[row][col], row, col, usedLettersSet, usedLettersArray)

                usedLettersSet.remove(convert_row_col_to_id(row, col))
                usedLettersArray.remove(convert_row_col_to_id(row, col))

        # all possible directions to check
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        
        for direction in directions:
            newRow, newCol = row + direction[0], col + direction[1]
            search_next_letter(currentString, newRow, newCol, usedLettersSet, usedLettersArray)

    def find_words(self):
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                row_col_id = convert_row_col_to_id(row, col)
                self.search_letter(self.gameboard[row][col], row, col, {row_col_id}, [row_col_id])

        print(len(self.possible_words))
        return