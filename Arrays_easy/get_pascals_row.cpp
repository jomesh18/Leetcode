// #include <iostream>
// #include <vector>
// using namespace std;
// class Solution {
// public:
//     vector<int> getRow(int rowIndex) {
//         vector<int> previous = {1};
//     	if (rowIndex == 0)
//     		return previous;
//         previous.push_back(1);
//     	if (rowIndex == 1)
//     		return previous;
//     	for(int i=2; i<=rowIndex; i++){
//     		vector<int> current;
//     		current.push_back(1);
//     		for(int j=0; j<previous.size()-1; j++)
//     			current.push_back(previous[j]+previous[j+1]);
//     		current.push_back(1);
//     		previous = current;
//     	}
//     	return previous;
//     }
// };

// int main(){
// 	Solution obj;
// 	int rowIndex = 4;
// 	vector<int> row = obj.getRow(rowIndex);
// 	for(int i=0; i<row.size(); i++)
// 		cout<<row[i]<<" ";
//     return 0;
// }

// from leetcode, using recursion
#include <iostream>
#include <vector>

using namespace std;

class Solution{
public:
    vector<int> getRow(int rowIndex){
        if (rowIndex == 0)
            return vector<int>(1,1);
        else{
            vector<int> prev = getRow(rowIndex-1);
            vector<int> res(1,1);
            for(int i=0; i<prev.size()-1; i++)
                res.push_back(prev[i]+prev[i+1]);
            res.push_back(1);
            return res;
        }
    }

};

int main(){
    Solution obj;
    int rowIndex = 3;
    vector<int> r = obj.getRow(rowIndex);
    for(int i=0; i<r.size(); i++)
        cout<<r[i]<<" ";
    return 0;
}
