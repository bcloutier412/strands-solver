from src.AVLTree import Node, AVLTree
import sys

# Constants
MINIMUM_WL = 4
MAXIMUM_WL = 15

# Function to simulate a dynamic print
def dynamic_print(text):
    sys.stdout.write('\r' + text)
    sys.stdout.flush()

dictionaryAVLTree = AVLTree()

print("[Creating Dict AVL Tree]")

with open("words_alpha.txt", "r") as file:
  counter = 0
  for word in file:
    currWord = word.strip()
    if len(currWord) >= MINIMUM_WL and len(currWord) <= MAXIMUM_WL:
      dictionaryAVLTree.insert_value(currWord)
      counter += 1
      dynamic_print(f"{counter} words added")

print()
print("[Finished Dict AVL Tree]")