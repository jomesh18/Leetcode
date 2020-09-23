#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
    	// string res_s;
        string temp;
        vector<string> res;
        int start = 0;
        for(int i=0; i<s.size(); i++){
            if (s[i] == ' ' and s[i-1] != ' '){
                // temp.push_back(s[start: i]);
                for(int j=start; j<i; j++)
                    temp.push_back(s[j]);
                cout<<temp;
                start = i+1;
                res.push_back(temp);
                temp.clear();
            }
            else if (s[i] == ' ')
                start = i+1;
        }
        // for(int i=0; i<res.size(); i++)
        //     cout<<res[i];
        // for(int i=temp.size()-1; i>=0; i--){
        //     res.push_back(temp[i]);
        //     res.push_back(" ");
        // }
        // res.pop_back();
        // return res;
        return 0;
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
