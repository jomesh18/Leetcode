#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
    	// string res_s;
        vector<char> c;
        vector<string> str;
        for(int i=0; i<s.size(); i++){
        	if ((s[i] != " "))
        	   c.push_back(s[i]);
            else
                str.push_back(c);
        }
    }
};

int main(){
	Solution obj;
	string s = "the sky is blue";
	cout<<s;
	// string res = obj.reverseWords(s);
    obj.reverseWords(s);
	// count<<res;
	return 0;
}
