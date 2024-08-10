from AVLTree import Node, AVLTree
from utils import get_relative_file_path
import sys
import json

with open(get_relative_file_path("../../data/runtime_data.json"), "r") as file:
        runtime_data = json.load(file)

# Function to simulate a dynamic print
def dynamic_print(text):
    sys.stdout.write('\r' + text)
    sys.stdout.flush()

dictionary_avl_tree = AVLTree()

print("[Creating Dict AVL Tree]")

with open(get_relative_file_path("../text_files/words_alpha.txt"), "r") as file:
  counter = 0
  for word in file:
    curr_word = word.strip()
    if len(curr_word) >= runtime_data["MINIMUM_WL"] and len(curr_word) <= runtime_data["MAXIMUM_WL"]:
      dictionary_avl_tree.insert_value(curr_word)
      counter += 1
      dynamic_print(f"{counter} words added")

print()
print("[Finished Dict AVL Tree]")