#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> previous = {1};
    	if (rowIndex == 0)
    		return previous;
        previous.push_back(1);
    	if (rowIndex == 1)
    		return previous;
    	for(int i=2; i<=rowIndex; i++){
    		vector<int> current;
    		current.push_back(1);
    		for(int j=0; j<previous.size()-1; j++)
    			current.push_back(previous[j]+previous[j+1]);
    		current.push_back(1);
    		previous = current;
    	}
    	return previous;
    }
};

int main(){
	Solution obj;
	int rowIndex = 4;
	vector<int> row = obj.getRow(rowIndex);
	for(int i=0; i<row.size(); i++)
		cout<<row[i]<<" ";
    return 0;
}
