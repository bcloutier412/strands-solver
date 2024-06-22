#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main(int argc, char *argv[]){

    ifstream wordFile;
    wordFile.open("words_alpha.txt");

    ofstream output;
    output.open("newWords.txt");

    const int SMALLEST_LENGTH = 3;

    string temp;

    while(getline(wordFile, temp)){
        int count = temp.size();
        
        if(count > 3 && count <= 15){
            output << temp << endl;
        }
    }

    wordFile.close();
    output.close();

    return 0;
}