#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size()-1;
        while(k-->0){
            int temp = nums[n];
            for(int i = n-1; i>=0; i--)
                nums[i] = nums[i-1];
            nums[0] = temp;
        }
    }
};

int main()
{
    Solution obj;
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;
    for(int i=0;i<nums.size();i++)
        cout<<nums[i]<<" ";
    cout<<"\n";
    obj.rotate(nums, k);
    for(int i=0;i<nums.size();i++)
        cout<<nums[i]<<" ";
    return 0;
}
