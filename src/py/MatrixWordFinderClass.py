from AVLTree import Node, AVLTree
import sys

# Constants
MINIMUM_WL = 4
MAXIMUM_WL = 15

# Function to simulate a dynamic print
def dynamic_print(text):
    sys.stdout.write('\r' + text)
    sys.stdout.flush()

class MatrixWordFinder:
  def __init__(self, gameboard, total_words_to_complete_matrix, dictionary_avl_tree):
    self.WIDTH = 6
    self.HEIGHT = 8
    self.gameboard = gameboard
    self.total_words_to_complete_matrix = total_words_to_complete_matrix
    self.dictionary_avl_tree = dictionary_avl_tree
    
  def search_letter():
     return