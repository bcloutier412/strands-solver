#include <iostream>
#include <vector>
#include <set>

class DLX {
public:
    struct Node {
        Node* left;
        Node* right;
        Node* up;
        Node* down;
        Node* column;
        int rowID;
        int colID;
        int nodeCount;

        Node() : left(nullptr), right(nullptr), up(nullptr), down(nullptr), column(nullptr),
                 rowID(-1), colID(-1), nodeCount(0) {}
    };

    DLX(int nRow, int nCol, int totalWordsToCompleteMatrix) 
        : nRow(nRow + 1), nCol(nCol), totalWordsToCompleteMatrix(totalWordsToCompleteMatrix) {
        // Allocate memory for the header node
        header = new Node();

        // Initialize the Matrix using raw pointers
        Matrix.resize(this->nRow);
        for (int i = 0; i < this->nRow; ++i) {
            Matrix[i].resize(this->nCol);
            for (int j = 0; j < this->nCol; ++j) {
                Matrix[i][j] = new Node();
            }
        }

        // Initialize the Problem Matrix
        ProbMat.resize(this->nRow, std::vector<bool>(this->nCol, false));
        for (int j = 0; j < this->nCol; ++j) {
            ProbMat[0][j] = true; // Row 0 consists of column headers, so set them to true
        }
    }

    ~DLX() {
        // Destructor to free allocated memory
        for (int i = 0; i < nRow; ++i) {
            for (int j = 0; j < nCol; ++j) {
                delete Matrix[i][j];
            }
        }
        delete header;
    }

    void solve() {
        createToridolMatrix();
        search(0);
    }

    void setProblemMatrix(int row, int col, bool value) {
        if (row >= 0 && row < nRow && col >= 0 && col < nCol) {
            ProbMat[row][col] = value;
        } else {
            std::cerr << "Error: Index out of bounds in setProblemMatrix(" << row << ", " << col << ")\n";
        }
    }

    void insertToProbMat(int row, int col) {
        ProbMat[row + 1][col] = true;
    }

    void printSolutions() {
        std::cout << "Printing Solutions: ";
        for (Node* node : solutions) {
            std::cout << node->rowID << " ";
            solutionsSet.insert(node->rowID);
        }
        std::cout << "\n";
    }

    void printSolutionsSet() {
        std::cout << "Printing Solutions Set: ";
        for (auto index : solutionsSet) {
            std::cout << index << " ";
        }
    }

private:
    Node* header;
    std::vector<std::vector<Node*>> Matrix;
    std::vector<std::vector<bool>> ProbMat;
    std::vector<Node*> solutions;
    std::set<int> solutionsSet;
    int nRow;
    int nCol;
    int totalWordsToCompleteMatrix;

    inline int getRight(int i) const { return (i + 1) % nCol; }
    inline int getLeft(int i) const { return (i - 1 < 0) ? nCol - 1 : i - 1; }
    inline int getUp(int i) const { return (i - 1 < 0) ? nRow - 1 : i - 1; }
    inline int getDown(int i) const { return (i + 1) % nRow; }

    void createToridolMatrix() {
        for (int i = 0; i < nRow; i++) {
            for (int j = 0; j < nCol; j++) {
                if (ProbMat[i][j]) {
                    Node* currentNode = Matrix[i][j];
                    Node* colHeader = Matrix[0][j];

                    if (i > 0) colHeader->nodeCount++;

                    currentNode->column = colHeader;
                    currentNode->rowID = i;
                    currentNode->colID = j;

                    int leftIdx = j;
                    do { leftIdx = getLeft(leftIdx); } while (!ProbMat[i][leftIdx] && leftIdx != j);
                    currentNode->left = Matrix[i][leftIdx];

                    int rightIdx = j;
                    do { rightIdx = getRight(rightIdx); } while (!ProbMat[i][rightIdx] && rightIdx != j);
                    currentNode->right = Matrix[i][rightIdx];

                    int upIdx = i;
                    do { upIdx = getUp(upIdx); } while (!ProbMat[upIdx][j] && upIdx != i);
                    currentNode->up = Matrix[upIdx][j];

                    int downIdx = i;
                    do { downIdx = getDown(downIdx); } while (!ProbMat[downIdx][j] && downIdx != i);
                    currentNode->down = Matrix[downIdx][j];
                }
            }
        }

        header->right = Matrix[0][0];
        header->left = Matrix[0][nCol - 1];
        Matrix[0][0]->left = header;
        Matrix[0][nCol - 1]->right = header;
    }

    void cover(Node* targetNode) {
        Node* colNode = targetNode->column;
        Node* row;
        Node* rightNode;

        colNode->left->right = colNode->right;
        colNode->right->left = colNode->left;

        for (row = colNode->down; row != colNode; row = row->down) {
            for (rightNode = row->right; rightNode != row; rightNode = rightNode->right) {
                rightNode->up->down = rightNode->down;
                rightNode->down->up = rightNode->up;
                Matrix[0][rightNode->colID]->nodeCount--;
            }
        }
    }

    void uncover(Node* targetNode) {
        Node* colNode = targetNode->column;
        Node* rowNode;
        Node* leftNode;

        for (rowNode = colNode->up; rowNode != colNode; rowNode = rowNode->up) {
            for (leftNode = rowNode->left; leftNode != rowNode; leftNode = leftNode->left) {
                leftNode->up->down = leftNode;
                leftNode->down->up = leftNode;
                Matrix[0][leftNode->colID]->nodeCount++;
            }
        }

        colNode->left->right = colNode;
        colNode->right->left = colNode;
    }

    Node* getMinColumn() {
        Node* min_col = header->right;
        Node* h = min_col->right;

        while (h != header) {
            if (h->nodeCount < min_col->nodeCount) {
                min_col = h;
            }
            h = h->right;
        }

        return min_col;
    }

    void search(int k) {
        if (static_cast<int>(solutions.size()) > totalWordsToCompleteMatrix) {
            return;
        }

        if (header->right == header) {
            printSolutions();
            return;
        }

        Node* column = getMinColumn();
        cover(column);

        for (Node* rowNode = column->down; rowNode != column; rowNode = rowNode->down) {
            solutions.push_back(rowNode);

            for (Node* rightNode = rowNode->right; rightNode != rowNode; rightNode = rightNode->right) {
                cover(rightNode);
            }

            search(k + 1);

            solutions.pop_back();

            column = rowNode->column;
            for (Node* leftNode = rowNode->left; leftNode != rowNode; leftNode = leftNode->left) {
                uncover(leftNode);
            }
        }

        uncover(column);
    }
};
