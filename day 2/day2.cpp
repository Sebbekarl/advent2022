
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
using namespace std;

unordered_map<string, int> lookup1 = {{"A X",3+1},{"A Y",6+2},{"A Z",0+3},{"B X",0+1},{"B Y",3+2},{"B Z",6+3},{"C X",6+1},{"C Y",0+2},{"C Z",3+3}};
unordered_map<string, int> lookup2 = {{"A X",0+3},{"A Y",3+1},{"A Z",6+2},{"B X",0+1},{"B Y",3+2},{"B Z",6+3},{"C X",0+2},{"C Y",3+3},{"C Z",6+1}};

int main() {
    int sum1 = 0;
    int sum2 = 0;
    fstream input("input.txt");
    string str_input;

    while (getline(input, str_input))
    {
        sum1 += lookup1[str_input];
        sum2 += lookup2[str_input];
    }
    cout << sum1 << " " << sum2 << endl;



    return 0;
}