
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0) return false;
        int temp = x, y = 0;
        while(temp>0) {
            if (y<0x7fffffff/10)
            {
                y = y*10+temp%10;
            } else {

                return false;
            }
            
            temp /= 10;
        }
        return x==y?true:false;
    }
};