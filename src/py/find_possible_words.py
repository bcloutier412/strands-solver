from MatrixWordFinderClass import MatrixWordFinder
from DictionaryAVLTree import dictionary_avl_tree
import json


def main():
    # Open the runtime_data file and import the 2D matrix and the total_words
    # Loading JSON file
    with open("data/runtime_data.json", "r") as file:
        runtime_data = json.load(file)

    matrix_word_finder = MatrixWordFinder(
        runtime_data["WIDTH"],
        runtime_data["HEIGHT"],
        runtime_data["MINIMUM_WL"],
        runtime_data["MAXIMUM_WL"],
        runtime_data["gameboard"],
        runtime_data["total_words_to_complete_matrix"],
        runtime_data["possible_words"],
        dictionary_avl_tree
    )

    # Updating JSON file
    with open("data/runtime_data.json", "w") as file:
        json.dump(runtime_data, file, indent=4, separators=(",", ": "))

    return 0


main()
