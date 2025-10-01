# NYT Strands Puzzle Solver

## 📖 Project Overview
The **New York Times Strands Puzzle Solver** is an algorithmic tool designed to solve the *Strands* word puzzle. This puzzle challenges players to identify themed words from a scrambled grid of letters.

The solver automates this process by interpreting the game board and generating valid solutions that adhere to the rules of the puzzle. It combines **recursive backtracking** with **Donald Knuth’s Dancing Links (DLX)** algorithm to tackle the underlying *exact cover* problem with both accuracy and efficiency.

---

## ✨ Key Features
- **Automated Puzzle Solving**  
  Given a Strands puzzle grid, the solver outputs one or more valid sets of words that satisfy all puzzle constraints.

- **Efficient Word Discovery**  
  Uses recursive backtracking to explore valid word paths on the board.

- **DLX Optimization**  
  Implements Knuth’s DLX algorithm to optimize the search for exact word combinations that cover all required letters without overlap.

- **Dictionary Validation**  
  Validates discovered word paths against a preloaded dictionary to ensure correctness.

---

## ⚙️ Technical Implementation
- **Python**
  - Grid parser to interpret puzzle boards.  
  - Recursive backtracking algorithms for traversing the 2D matrix and identifying valid word paths.  
  - A custom **AVL Tree** for efficient dictionary validation and prefix pruning. This structure was tailored to handle subword relationships, enabling the solver to quickly discard invalid paths and minimize unnecessary computation.

- **C++**  
  - Implementation of Knuth’s **Dancing Links (DLX)** algorithm.  
  - DLX efficiently searches for non-overlapping word groupings that cover the board exactly once, dramatically improving runtime.

---

## 🚧 Challenges & Solutions
One major challenge was designing an efficient approach to the *exact cover* problem:

- **Initial Approach**: A pure backtracking algorithm with basic pruning. While functional, pruning required iterating through all branches, leading to high computational cost.  
- **Optimized Solution**: Adoption of Knuth’s **Dancing Links (DLX)** technique. DLX allows pruned branches to be cut in a single operation, removing the need for costly iteration.

**Result:** This optimization improved solver performance by **100×**, reducing runtime from several minutes to just seconds.

---

## 📂 Repository Structure
```
├── data/
│   └── runtime_data.json         # Stores runtime execution data

├── src/
│   ├── cpp/                      # C++ implementation of DLX
│   │   ├── DLX.hpp
│   │   ├── json.hpp
│   │   ├── main.cpp
│   │   └── my_program            # Compiled C++ binary
│   │
│   ├── js/                       # Placeholder for JS components (future use)
│   │
│   └── py/                       # Python solver implementation
│       ├── DictionaryAVLTree.py  # Custom AVL Tree for dictionary validation & prefix pruning
│       ├── MatrixWordFinder.py   # Backtracking solver for word discovery
│       ├── utils.py              # Helper utilities
│       └── main.py               # Entry point for Python solver

├── text_files/
│   ├── strands_words.txt         # Themed words for Strands puzzles
│   └── words_alpha.txt           # Dictionary word list

├── README.md
```

---

## 🚀 Getting Started
### Prerequisites
- Python 3.9+  

### Setup
```bash
git clone git@github.com:brandoncloutier/strands-solver.git
cd strands-solver/src/py
```

### Usage

1. **Prepare the Puzzle Input**  
   You must provide the puzzle grid as a **2D matrix of lowercase letters** inside `data/runtime_data.json` as the gameboard key/value. Also set the total_words_to_complete_matrix equal to the total words provided by strands.  
   Example:
   ```json
   {
       "WIDTH": 6,
       "HEIGHT": 8,
       "MINIMUM_SPANGRAM_LENGTH": 4,
       "MINIMUM_WL": 4,
       "MAXIMUM_WL": 15,
       "total_words_to_complete_matrix": 6,
       "gameboard": [
          ["r", "s", "p", "e", "y", "t"],
          ["e", "t", "c", "n", "e", "s"],
          ["h", "y", "m", "e", "o", "h"],
          ["t", "a", "p", "l", "a", "v"],
          ["s", "e", "u", "o", "n", "i"],
          ["c", "o", "i", "p", "d", "s"],
          ["p", "o", "t", "l", "i", "c"],
          ["e", "r", "a", "i", "n", "e"]
        ],
   }
   ```

2. **Run the Solver**  
   Once your grid is set in `runtime_data.json`, run:
   ```bash
   python3 main.py
   ```

3. **💡 Quick Tip for Inputting Grids**  
   If you have a screenshot of a Strands puzzle grid, you can paste it into ChatGPT with the following prompt:  
   > *"Generate me a 2D matrix of lower case letters in JSON format from this grid of letters."*  
   
   Then simply copy the generated JSON matrix into `runtime_data.json` under `"gameboard"`.

---

## 📈 Future Improvements
- Implement GUI for visualizing solutions on the puzzle grid.  
- Expand dictionary integration with external APIs.  
- Add multi-threaded support for even faster solving.

---

## 📚 Resources
- Knuth, D. E. (2000). *Dancing Links*.  
  [PDF](https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf) — Knuth’s paper describing the DLX algorithm and how it is used for exact cover problems.  

---

## 📜 License
MIT License – feel free to use, modify, and distribute this project with attribution.
