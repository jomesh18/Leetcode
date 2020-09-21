#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
    	// string res_s;
        for(int i=0; i<s.size(); i++){
        	// if (s[i] != " ")
            cout<<"Hi";
        	cout<<s[i];
        }
    }
};

int main(){
	Solution obj;
	string s = "the sky is blue";
    cout<<"Hello";
	cout<<s;
	// string res = obj.reverseWords(s);
    obj.reverseWords(s);
	// count<<res;
	return 0;
}