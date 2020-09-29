// #include <iostream>
// #include <string>
// #include <vector>

// using namespace std;

// class Solution {
// public:
//     string reverseWords(string s) {
//         string res;
//         int last_index = s.size()-1;
//         int stop = -1;
//         for(int i=last_index; i>=0; i--){
//             if (s[i] != ' '){
//                 stop = i;
//                 break;
//             }
//         }
//         if (stop<0)
//             return "";
//         for(int i=last_index-1; i>=0; i--){
//             if (s[i] == ' ' and s[i+1] != ' '){
//                 for(int j=i+1; j<=stop; j++)
//                     res.push_back(s[j]);
//                 res.push_back(' ');
//                 stop = i-1;
//             }
//             else if(s[i] == ' ')
//                 stop = i-1;
//         }
//         if (s[0] != ' ' and stop>=0){
//             for(int j=0;j<=stop;j++)
//                 res.push_back(s[j]);
//             res.push_back(' ');
//         }
//         res.pop_back();
//         return res;
//     }
// };

// int main(){
// 	Solution obj;
// 	string s = "the sky is blue";
//     // string s = "";
//     // string s = " ";
// 	cout<<s<<endl;
// 	cout<<obj.reverseWords(s)<<endl;
// 	return 0;
// }

// from leetcode inplace solution

// #include <iostream>
// #include <string>
// #include <algorithm>

// using std::cout;
// using std::endl;
// using std::string;

// class Solution {
// public:
//     void reverseWords(string &s) {
//         reverse(s.begin(), s.end());
//         // cout<<s<<endl;
//         int storeIndex = 0;
//         for(int i=0; i<s.size(); i++){
//             if (s[i] != ' '){
//                 if (storeIndex != 0) s[storeIndex++] = ' ';
//                 int j = i;
//                 while (j<s.size() && s[j]!= ' ') s[storeIndex++] = s[j++];
//                 // cout<<s<<endl;
//                 reverse(s.begin()+storeIndex-(j-i), s.begin()+storeIndex);
//                 // cout<<s<<endl;
//                 i = j;
//             }
//         }
//         s.erase(s.begin()+storeIndex, s.end());
//     }
// };

// int main(){
//     Solution obj;
//     string s = "  the    sky is  blue";
//     // string s = "  the  ";
//     // string s = "";
//     // string s = " ";
//     cout<<s<<endl;
//     obj.reverseWords(s);
//     cout<<s<<endl;
//     return 0;
// }

// O(n) space based on the above code
#include <iostream>
#include <string>
#include <algorithm>

using std::cout;
using std::endl;
using std::string;

class Solution {
public:
    string reverseWords(string &s) {
        string res;
        for(int i=s.size()-1; i>=0; i--){
            if (s[i] != ' '){
                int j = i;
                while (j>=0 && s[j] != ' ') j--;
                res.append(s.substr(j+1, i-j));
                res.push_back(' ');
                i = j;
            }
        }
        res.pop_back();
        return res;
    }
};

int main(){
    Solution obj;
    string s = "the    sky is  blue ";
    cout<<s<<endl;
    cout<<obj.reverseWords(s)<<endl;
    return 0;
}