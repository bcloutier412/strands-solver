from AVLTree import Node, AVLTree
import sys


# Function to simulate a dynamic print
def dynamic_print(text):
    sys.stdout.write("\r" + text)
    sys.stdout.flush()


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
        dictionary_avl_tree,
    ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.MINIMUM_WL = MINIMUM_WL
        self.MAXIMUM_WL = MAXIMUM_WL
        self.gameboard = gameboard
        self.total_words_to_complete_matrix = total_words_to_complete_matrix
        self.dictionary_avl_tree = dictionary_avl_tree
        self.possible_words = possible_words

    def search_letter():
        return
