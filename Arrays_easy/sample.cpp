#include <iostream>
#include <vector>
#include <typeinfo>

using namespace std;

void test(){
	// vector<char> s = {'s', ' ', 't', 'd'};
	// vector<int> s = {1, 2, 3, 4};
	// s.push_back("the sky is blue");
	string s = "abcd efgh";
    string temp;
    int start = 0;
    for(int i=0; i<s.size(); i++){
        if (s[i] == ' ' and s[i-1] != ' '){
            // temp.push_back(s[start: i]);
            for(int j=start; j<i; j++)
                temp.push_back(s[j]);
            start = i+1;
            cout<<temp<<"\n";
            temp = "";
        }
        else if (s[i]==' ')
        	start = i+1;
	}
	if (s[s.size()-1])
}

int main(){	
	test();
	return 0;
}
