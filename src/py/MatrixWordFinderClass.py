from AVLTree import Node, AVLTree
from utils import convert_row_col_to_id, is_in_matrix_bound, get_relative_file_path
import sys

class MatrixWordFinder:
    """
    A class to find all possible words within a 2D character matrix (gameboard) based on certain constraints.

    Attributes:
    -----------
    WIDTH : int
        The width of the gameboard (number of columns).
    HEIGHT : int
        The height of the gameboard (number of rows).
    MINIMUM_WL : int
        The minimum word length to consider a valid word.
    MAXIMUM_WL : int
        The maximum word length to consider.
    gameboard : list of list of str
        The 2D matrix of characters representing the gameboard.
    total_words_to_complete_matrix : int
        The total number of words needed to complete the matrix (though not directly used in methods).
    possible_words : list of list of int
        A list to store all valid words found, represented as lists of indices corresponding to their positions in the gameboard.
    dictionary_avl_tree : AVLTree
        An AVL tree containing the dictionary of valid words and their substrings for efficient searching.
    return_char : str
        A character used to separate output (default is "0").
    outputFile : file object
        A file object to write the valid words found during the search.
    """

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
        """
        Initializes the MatrixWordFinder with the specified attributes.

        Parameters:
        -----------
        WIDTH : int
            The width of the gameboard.
        HEIGHT : int
            The height of the gameboard.
        MINIMUM_WL : int
            The minimum word length to consider.
        MAXIMUM_WL : int
            The maximum word length to consider.
        gameboard : list of list of str
            The 2D matrix of characters.
        total_words_to_complete_matrix : int
            The total number of words needed to complete the matrix.
        possible_words : list of list of int
            A list to store all valid words found.
        dictionary_avl_tree : AVLTree
            An AVL tree with the dictionary of words and substrings.
        """
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
        """
        Destructor to close the output file when the MatrixWordFinder object is destroyed.
        """
        self.outputFile.close()
    
    def search_letter(self, currentString, row, col, usedLettersSet, usedLettersArray):
        """
        Recursive method to search for valid words starting from a given letter in the gameboard.

        Parameters:
        -----------
        currentString : str
            The current string being built as part of the search.
        row : int
            The current row position in the gameboard.
        col : int
            The current column position in the gameboard.
        usedLettersSet : set of int
            A set of used letter indices to avoid reusing the same letter in a word.
        usedLettersArray : list of int
            A list of used letter indices, representing the path of the current word being formed.
        """
        # Check if the current position is within the bounds of the gameboard
        if not is_in_matrix_bound(row, col, self.HEIGHT, self.WIDTH):
            return
        
        # If the current string length exceeds the maximum word length, stop searching
        if len(currentString) + 1 >= self.MAXIMUM_WL:
            return
        
        # Check if the current string is a valid word or substring
        if len(currentString) >= self.MINIMUM_WL:
            searchResults = self.dictionary_avl_tree.search_value(currentString)

            if not searchResults['isSubString']:
                return
            elif searchResults['isWord']:
                # If it's a valid word, add it to the possible words and write it to the output file
                self.possible_words.append(usedLettersArray.copy())
                self.outputFile.write(currentString + '\n')

        def search_next_letter(currentString, row, col, usedLettersSet, usedLettersArray):
            """
            Internal helper function to search for the next letter in all possible directions.

            Parameters:
            -----------
            currentString : str
                The current string being built as part of the search.
            row : int
                The row position to search next in the gameboard.
            col : int
                The column position to search next in the gameboard.
            usedLettersSet : set of int
                A set of used letter indices to avoid reusing the same letter in a word.
            usedLettersArray : list of int
                A list of used letter indices, representing the path of the current word being formed.
            """
            if is_in_matrix_bound(row, col, self.HEIGHT, self.WIDTH) and convert_row_col_to_id(row, col) not in usedLettersSet:
                usedLettersSet.add(convert_row_col_to_id(row, col))
                usedLettersArray.append(convert_row_col_to_id(row, col))

                # Recursively search for the next letter
                self.search_letter(currentString + self.gameboard[row][col], row, col, usedLettersSet, usedLettersArray)

                # Backtrack to explore other possibilities
                usedLettersSet.remove(convert_row_col_to_id(row, col))
                usedLettersArray.remove(convert_row_col_to_id(row, col))

        # Directions to search: up, right, down, left, and the four diagonals
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        
        # Explore all directions for the next letter
        for direction in directions:
            newRow, newCol = row + direction[0], col + direction[1]
            search_next_letter(currentString, newRow, newCol, usedLettersSet, usedLettersArray)

    def find_words(self):
        """
        Initiates the search for all valid words in the gameboard.
        """
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                row_col_id = convert_row_col_to_id(row, col)
                # Start searching for words beginning with each letter in the gameboard
                self.search_letter(self.gameboard[row][col], row, col, {row_col_id}, [row_col_id])

        print(len(self.possible_words))
        return
