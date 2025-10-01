#include <fstream> 
#include <iostream> 
#include <typeinfo>

#include "DLX.hpp"
#include "json.hpp"
#include <vector>

int main() {
  std::ifstream file("../../data/runtime_data.json");

  // Check if the file was opened successfully
  if (!file.is_open()) {
      std::cerr << "Failed to open file!" << std::endl;
      return 1;
  }
  
  // Parse the JSON file into a JSON object
  nlohmann::json runtime_data;
  file >> runtime_data;

  // std::cout << runtime_data["possible_words"].size() << std::endl;

  int AREA = static_cast<int>(runtime_data["WIDTH"]) * static_cast<int>(runtime_data["HEIGHT"]);
  // 1. Create DLX
  DLX dlx{static_cast<int>(runtime_data["possible_words"].size()), AREA, runtime_data["total_words_to_complete_matrix"]};

  // 2. Fill the problem mat
  for (int wordIndex = 0; wordIndex < runtime_data["possible_words"].size(); ++wordIndex)
  {
    for (auto cellID : runtime_data["possible_words"][wordIndex][1])
    {
      dlx.insertToProbMat(wordIndex, cellID);
    }
  }

  // Execute dlx solve
  dlx.solve();
  dlx.printSolutionsSet(runtime_data);

  // Close the file
  file.close();

  return 0;
}
 