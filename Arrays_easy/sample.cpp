#include <iostream>
#include <vector>
#include <typeinfo>
#include <string>
#include <algorithm>

using std::cout;
using std::string;
using std::endl;

void test(string &s){
    reverse(s.begin(), s.end());
}

int main(){	
    // int a[5] = {1, 2, 3, 4, 5};
    // cout<<a<<endl;
    // cout<<*a<<endl;
    int p[3][4] = {{4, 8, 13, 9}, {1, 6, 9, 3}, {5, 2, 7, 10}};
    // cout<<p[2][3]<<endl;
    cout<<((p+2))<<endl;
    cout<<*(*(p+2))<<endl;
	return 0;
}
