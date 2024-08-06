from AVLTree import Node, AVLTree
import sys

# Constants
MINIMUM_WL = 4
MAXIMUM_WL = 15

# Function to simulate a dynamic print
def dynamic_print(text):
    sys.stdout.write('\r' + text)
    sys.stdout.flush()

dictionary_avl_tree = AVLTree()

print("[Creating Dict AVL Tree]")

with open("text_files/words_alpha.txt", "r") as file:
  counter = 0
  for word in file:
    curr_word = word.strip()
    if len(curr_word) >= MINIMUM_WL and len(curr_word) <= MAXIMUM_WL:
      dictionary_avl_tree.insert_value(curr_word)
      counter += 1
      dynamic_print(f"{counter} words added")

print()
print("[Finished Dict AVL Tree]")