#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    string truncateSentence(string s, int k) {
        string delimiters = " ";
        string::size_type lastPos = s.find_first_not_of(delimiters, 0);
        string::size_type pos = s.find_first_of(delimiters, lastPos);
        // cout << pos << " " << lastPos<<endl;
        while (--k and (string::npos != lastPos || string::npos != pos)) {
            lastPos = s.find_first_not_of(delimiters, pos);
            pos = s.find_first_of(delimiters, lastPos);
        }
        string ans = s.substr(0, pos);
        // cout<< ans <<" " << pos <<endl;
        return ans;
    }
};

void split(const string& s, vector<string>& tokens, const string& delimiters = " ") {
    string::size_type lastPos = s.find_first_not_of(delimiters, 0);
    string::size_type pos = s.find_first_of(delimiters, lastPos);
    while ( string::npos != pos || string::npos != lastPos) {
        cout << lastPos << " " << pos << " " << s<<endl;
        tokens.push_back(s.substr(lastPos, pos - lastPos));
        lastPos = s.find_first_not_of(delimiters, pos);
        pos = s.find_first_of(delimiters, lastPos);
    }
}

int main() {
    Solution so;
    string s = "I am super man hero";
    vector<string> ve = vector<string> ();
    string ans = so.truncateSentence(s, 2);
    // split(s,ve);
    cout << ans << endl;
    return 0;
}
