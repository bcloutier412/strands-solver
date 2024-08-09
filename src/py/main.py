from MatrixWordFinderClass import MatrixWordFinder
from DictionaryAVLTree import dictionary_avl_tree
from utils import get_relative_file_path
import json


def main():
    # Open the runtime_data file and import the 2D matrix and the total_words
    # Loading JSON file
    with open(get_relative_file_path("../../data/runtime_data.json"), "r") as file:
        runtime_data = json.load(file)
    
    # Creating copy of runtime gameboard so that we can remove the letters for the spangram and replace with 'X'
    updated_gameboard = runtime_data["gameboard"].copy()

    # Reset the possible_words array in realtime_data
    runtime_data["possible_words"] = []

    # Run for loop to replace id's in the gameboard

    # Create the matrix word finder object and instanciate it with the runtime_data and the updated gameboard to remove the spangram
    matrix_word_finder = MatrixWordFinder(
        runtime_data["WIDTH"],
        runtime_data["HEIGHT"],
        runtime_data["MINIMUM_WL"],
        runtime_data["MAXIMUM_WL"],
        updated_gameboard,
        runtime_data["total_words_to_complete_matrix"],
        runtime_data["possible_words"],
        dictionary_avl_tree
    )

    # Finding all words in the 2D matrix
    matrix_word_finder.find_words()

    # Updating JSON files
    with open(get_relative_file_path("../../data/runtime_data.json"), "w") as file:
        json.dump(runtime_data, file, indent=4, separators=(",", ": "))

    return 0


main()
