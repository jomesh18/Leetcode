#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string res;
        int last_index = s.size()-1;
        int stop = last_index;
        for(int i=last_index; i>=0; i--){
            if (s[i] == ' ')
                stop = i-1;
            else if (s[i] != ' '){
                stop = i;
                break;
            }
        }
        if (stop<0)
            return "";
        for(int i=last_index-1; i>=0; i--){
            if (s[i] == ' ' and s[i+1] != ' '){
                for(int j=i+1; j<=stop; j++)
                    res.push_back(s[j]);
                res.push_back(' ');
                stop = i-1;
            }
            else if(s[i] == ' ')
                stop = i-1;
        }
        if (s[0] != ' ' and stop>=0){
            for(int j=0;j<=stop;j++)
                res.push_back(s[j]);
            res.push_back(' ');
        }
        res.pop_back();
        return res;
    }
};

int main(){
	Solution obj;
	// string s = "the sky is blue";
    string s = "";
    // string s = " ";
	cout<<s<<endl;
	cout<<obj.reverseWords(s)<<endl;
	return 0;
}
