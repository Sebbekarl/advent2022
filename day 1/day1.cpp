#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;



int main(int, char**) {
    int sum = 0;
    vector<int> sums;
    fstream input("input.txt");
    string temp;
    while (getline(input, temp))
    {
        if(temp == ""){
            sums.push_back(sum);
            sum = 0;
        }else{
            sum += stoi(temp);
        }
    }
    input.close();
    sort(sums.begin(), sums.end());
    
    cout << sums.back() << endl;

    sum = 0;
    for (size_t i = 0; i < 3; i++)
    {
        sum += sums.back();
        sums.pop_back();
    }
    cout << sum << endl;

    return 0;
}