#include <iostream>
#include <vector>

using namespace std;

void test(){
	vector<int> a(5,1);
	int n = a.size();
	cout<<"vector size = "<<n<<"\n";
	for(int i=0; i<n; i++)
		cout<<a[i]<<" ";
}

int main(){	
	test();
	return 0;
}
