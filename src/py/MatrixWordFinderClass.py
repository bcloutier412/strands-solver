# from py.DictionaryAVLTree import Node, AVLTree
from utils import convert_row_col_to_id, is_in_matrix_bound, get_relative_file_path, convert_id_to_row_col
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
        MINIMUM_SPANGRAM_LENGTH,
        MINIMUM_WL,
        MAXIMUM_WL,
        gameboard,
        total_words_to_complete_matrix,
        possible_words,
        possible_spangrams,
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
        self.MINIMUM_SPANGRAM_LENGTH = MINIMUM_SPANGRAM_LENGTH
        self.MINIMUM_WL = MINIMUM_WL
        self.MAXIMUM_WL = MAXIMUM_WL
        self.gameboard = gameboard
        self.total_words_to_complete_matrix = total_words_to_complete_matrix
        self.dictionary_avl_tree = dictionary_avl_tree
        self.possible_words = possible_words
        self.possible_spangrams = possible_spangrams
        self.return_char = "0"
        self.outputFile = open(get_relative_file_path("../text_files/strands_words.txt"), "w")
        self.word_list_break_points = {}

    def __del__(self):
        """
        Destructor to close the output file when the MatrixWordFinder object is destroyed.
        """
        self.outputFile.close()
    
    def search_letter_for_word(self, currentString, row, col, usedLettersSet, usedLettersArray):
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
        if len(currentString) >= self.MINIMUM_SPANGRAM_LENGTH:
            searchResults = self.dictionary_avl_tree.search_value(currentString)

            if not searchResults['isSubString']:
                return
            elif searchResults['isWord']:
                # If it's a valid word, add it to the possible words and write it to the output file
                self.possible_words.append([currentString, usedLettersArray.copy()])

        def search_next_letter_for_word(currentString, row, col, usedLettersSet, usedLettersArray):
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
                self.search_letter_for_word(currentString + self.gameboard[row][col], row, col, usedLettersSet, usedLettersArray)

                # Backtrack to explore other possibilities
                usedLettersSet.remove(convert_row_col_to_id(row, col))
                usedLettersArray.remove(convert_row_col_to_id(row, col))

        # Directions to search: up, right, down, left, and the four diagonals
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        
        # Explore all directions for the next letter
        for direction in directions:
            newRow, newCol = row + direction[0], col + direction[1]
            search_next_letter_for_word(currentString, newRow, newCol, usedLettersSet, usedLettersArray)

    def find_words(self):
        """
        Initiates the search for all valid words in the gameboard.
        """
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                row_col_id = convert_row_col_to_id(row, col)
                self.word_list_break_points[row_col_id] = len(self.possible_words)
                # Start searching for words beginning with each letter in the gameboard
                self.search_letter_for_word(self.gameboard[row][col], row, col, {row_col_id}, [row_col_id])
        # for word in self.possible_words:
        #     print(word)
        # for key, value in self.word_list_break_points.items():
        #     print(key, value)
        print(len(self.possible_words))
        return

    def remove_possible_words_duplicates(self):
        seen = set()

        write_index = 0  # Pointer to place unique elements

        for read_index in range(len(self.possible_words)):
            if self.possible_words[read_index][0] not in seen:
                seen.add(self.possible_words[read_index][0])
                self.possible_words[write_index] = self.possible_words[read_index]
                write_index += 1

        # Trim the list to remove the remaining duplicates
        del self.possible_words[write_index:]
        print(len(self.possible_words))
        return
    
    def write_possible_words_to_txt(self):
        for [word,_] in self.possible_words:
            self.outputFile.write(word + '\n')

    # def search_letter_for_spangram(self, currentString, row, col, usedLettersSet, usedLettersArray, usedWordsArray, potentialEndingCells):
    #     # Check if the current position is within the bounds of the gameboard
    #     if not is_in_matrix_bound(row, col, self.HEIGHT, self.WIDTH):
    #         return
        
    #     # If the current string length exceeds the maximum word length, stop searching
    #     if len(currentString) + 1 >= self.MAXIMUM_WL:
    #         return
    
    # def search_next_letter_for_spangram():
    #     return

    def find_spangrams(self):
        left_cells = {0, 6, 12, 18, 24, 30, 36, 42}
        right_cells = {5, 11, 17, 23, 29, 35, 41, 47}
        top_cells = {0, 1, 2, 3, 4, 5}
        bottom_cells = {42, 43, 44, 45, 46, 47}

        def check_for_spangram(currentWordIndex, usedLettersSet, usedLettersArray, ending_cells, num_of_words):
            current_word = self.possible_words[currentWordIndex][1]
            last_letter_cell = current_word[-1]

            '''
                First we want to see if the length of the total words that we have checked isnt over 2. If it is then we will just revert back
                because we know that a spangram is only going to be 2 words. So lets say we recursively get to this point then we know that we have 
                looked at two. Well actually is there a way for me to stop the program if we have 2 words because we dont have to do anything after that.
                Second we want to check if the last letter in the currentWord is in ending_cells. We dont have to do bounds checking
                because it should already be a found word so we just need to see if it is in ending. If it is then we know that we found a
                spangram.
            '''
            if len(usedLettersArray) > self.MAXIMUM_WL:
                return 
            
            # Check if last letter of the currentWordIndex is in the ending_cells
            if last_letter_cell in ending_cells:
                stringLetters = ""
                for letterCell in usedLettersArray:
                    [row, col] = convert_id_to_row_col(letterCell)

                    stringLetters += self.gameboard[row][col]
                self.outputFile.write(stringLetters + '\n')
                self.possible_spangrams.append([stringLetters, usedLettersArray])
                return 
            
            # If we know that the word doesnt end in the ending_cells so its not a spangram and we have exhausted 2 words then we will revert back
            if num_of_words >= 2:
                return

            # Directions to search: up, right, down, left, and the four diagonals
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
            
            for direction in directions:
                [row, col] = convert_id_to_row_col(last_letter_cell)
                newRow, newCol = row + direction[0], col + direction[1]

                # We want to make sure the newRow, newCol are in matrix bound. 
                # We want to make sure the letters havent been used before 
                # if it hasnt then we want to iterate through all the possible_words that start on that cell and call check_for_spangram

                if is_in_matrix_bound(newRow, newCol, self.HEIGHT, self.WIDTH) and convert_row_col_to_id(newRow, newCol) not in usedLettersSet:
                    cell_id = convert_row_col_to_id(newRow, newCol)
                    start_index = self.word_list_break_points[cell_id]
                    end_index = self.word_list_break_points[cell_id + 1] if cell_id + 1 < self.HEIGHT * self.WIDTH else len(self.possible_words)

                    for currentWordIndex in range(start_index, end_index):
                        new_usedLettersSet = usedLettersSet.copy()
                        new_usedLettersArray = usedLettersArray.copy()
                        
                        new_usedLettersSet.update(self.possible_words[currentWordIndex][1])
                        new_usedLettersArray.extend(self.possible_words[currentWordIndex][1])

                        check_for_spangram(currentWordIndex, new_usedLettersSet, new_usedLettersArray, ending_cells, num_of_words + 1)

            return
    
        for cell_id in left_cells:
            start_index = self.word_list_break_points[cell_id]
            end_index = self.word_list_break_points[cell_id + 1] if cell_id + 1 < self.HEIGHT * self.WIDTH else len(self.possible_words)

            for currentWordIndex in range(start_index, end_index):
                check_for_spangram(currentWordIndex, set(self.possible_words[currentWordIndex][1]), self.possible_words[currentWordIndex][1].copy(), right_cells, 1)
            
        print(len(self.possible_spangrams))

        # for cell_id in left_cells:
        #     start_index = self.word_list_break_points[cell_id]
        #     end_index = self.word_list_break_points[cell_id + 1] if cell_id + 1 < len(self.word_list_break_points) else len(self.possible_words)

        #     for index in range(start_index, end_index):
        #         single_word_IDs = self.possible_words[index][1]
        #         last_letter_ID = single_word_IDs[len(single_word_IDs) - 1]

        #         if last_letter_ID in right_cells:
        #             print(self.possible_words[index])
        #         else:
        #             # We want to iterate through all the letters that surround it and that is the start index.
        #             # Iterate through those and see if the last element in the word is in the ending cells
        #             directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        #             [row, col] = convert_id_to_row_col(last_letter_ID)

        #             for direction in directions:
        #                 if is_in_matrix_bound(row + direction[0], col + direction[1], self.HEIGHT, self.WIDTH) and convert_row_col_to_id(row + direction[0], col + direction[1]) not in self.possible_words[index][1]:
        #                     adjacent_cell_id = convert_row_col_to_id(row + direction[0], col + direction[1])
        #                     adjacent_start_index = self.word_list_break_points[adjacent_cell_id]
        #                     adjacent_end_index = self.word_list_break_points[adjacent_cell_id + 1] if adjacent_cell_id + 1 < len(self.word_list_break_points) else len(self.possible_words)

        #                     for index_second in range(adjacent_start_index, adjacent_end_index):
        #                         adjacent_single_word_IDs = self.possible_words[index_second][1]
        #                         adjacent_last_letter_ID = single_word_IDs[len(adjacent_single_word_IDs) - 1]
                                
        #                         if adjacent_last_letter_ID in right_cells:
        #                             print("here", self.possible_words[index], self.possible_words[index_second])



        # for ID in right_cells:
        #     print(convert_id_to_row_col(ID))
        
        # for ID in top_cells:
        #     print(convert_id_to_row_col(ID))
        
        # for ID in bottom_cells:
        #     print(convert_id_to_row_col(ID))

        # In this algorithm we to start at every edge in the board and the try to search for a word that spans across
        return