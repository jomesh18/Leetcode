#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
    	int stop = 0;
    	string res = "";
    	int n = s.size()-1;
        for(int i=0; i<=n;i++){
        	if (s[i] == ' '){
        		for(int j=i-1; j>=stop; j--)
        			res.push_back(s[j]);
        		stop = i+1;
        		res.push_back(' ');
        	}
        }
        for(int i=n;i>=stop; i--)
        	res.push_back(s[i]);
        cout<<res.size()<<endl;
        return res;
    }
};

int main(){
	Solution obj;
	string s = " Lets  talk football! ";
	cout<<s<<endl;
    cout<<s.size()<<endl;
	cout<<obj.reverseWords(s)<<endl;
	return 0;
}

// In place try

// #include <iostream>
// #include <string>

// using std::cout;
// using std::endl;
// using std::string;

// class Solution {
// public:
//     string reverseWords(string s) {
//         int stop = 0;
//         string res = "";
//         int n = s.size()-1;
//         for(int i=0; i<=n;i++){
//             if (s[i] == ' '){
//                 for(int j=i-1; j>=stop; j--)
//                     res.push_back(s[j]);
//                 stop = i+1;
//                 res.push_back(' ');
//             }
//         }
//         for(int i=n;i>=stop; i--)
//             res.push_back(s[i]);
//         return res;
//     }
// };

// int main(){
//     Solution obj;
//     string s = "Let's talk football!";
//     cout<<s<<endl;
//     cout<<obj.reverseWords(s)<<endl;
//     return 0;
// }
