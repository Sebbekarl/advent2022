
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
using namespace std;
enum points
{
    loss = 0, draw = 3, win = 6,
    rock = 1, paper = 2, scissor = 3
};

unordered_map<string, int> lookup1 = {{"A X", draw + rock}, {"A Y", win + paper}, {"A Z", loss + scissor}, 
                                      {"B X", loss + rock}, {"B Y", draw + paper}, {"B Z", win + scissor}, 
                                      {"C X", win + rock}, {"C Y", loss + paper}, {"C Z", draw + scissor}};

unordered_map<string, int> lookup2 = {{"A X", loss + scissor}, {"A Y", draw + rock}, {"A Z", win + paper},
                                      {"B X", loss + rock}, {"B Y", draw + paper}, {"B Z", win + scissor}, 
                                      {"C X", loss + paper}, {"C Y", draw + scissor}, {"C Z", win + rock}};

int main()
{
    int sum1 = 0, sum2 = 0;
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