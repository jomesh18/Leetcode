#include <iostream>
#include <vector>
#include <typeinfo>

using namespace std;

auto test(string s){
    return s.size();
}

int main(){	
    // string s = "the  sky is  blue";
    string s = "";
    // string s = " ";
	cout<<test(s);
	return 0;
}
