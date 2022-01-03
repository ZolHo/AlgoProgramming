#include<iostream>
#include<string>
#include<cstring>
using namespace std;


class Solution {
public:
    string longestPalindrome(string s) {
        int l = s.length();
        string* ansString = &s;
        int ansLen = 1;
        bool **map = new bool*[l+2];
        for (int i = 0; i < l+2; i++) {
            map[i] = new bool[l+2];
        }

        // for (int i = 0; i < l+2; i++) {
        //     for (int j = 0; j < l+2; j++) map[i][j] = false;
        // }
        for (int i = 0 ; i < l+2; i++) {
            memset(map[i], false, l+2);
        }
        for ( int k = 0; k < l+1; k++ ) {
            for (int i = 1,j=i+k; i<l+1 && j<l+1; i++) {
                if (i==j) {
                    map[i][j] = true;
                } else if(j-i==1) {
                    map[i][j] = s[i-1]==s[j-1]?true:false;
                } else {
                    map[i][j] = map[i+1][j-1] && (s[i-1]==s[j-1]);
                }
                if (map[i][j] && (j-i+1 > ansLen)) {
                    ansLen = j-i+1;
                    ansString = &s + i-1;
                }
            }
        }
        for (int i = 1; i < l+1; i++) {
            for (int j = i; j < l+1; j++) {
                if (i==j) {
                    map[i][j] = true;
                } else if(j-i==1) {
                    map[i][j] = s[i-1]==s[j-1]?true:false;
                } else {
                    map[i][j] = map[i+1][j-1] && (s[i-1]==s[j-1]);
                }
                if (map[i][j] && (j-i+1 > ansLen)) {
                    ansLen = j-i+1;
                    ansString = &s + i-1;
                }
            }
        }
        return string(s.substr(ansString-&s, ansLen));
    }
};

int main() {
    Solution s;
    cout<<s.longestPalindrome("babad");
    return 0;
}