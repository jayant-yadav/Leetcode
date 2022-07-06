//https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int l = sizeof(nums)/sizeof(nums[0]);
        
        for(int i=1;i<l;i++)
        {
            if(nums[i]==nums[i-1])
            {
                for(int j=i;j<l-1;j++)
                {
                    nums[j]=nums[j+1];
                }
            }
        }
        
        int k=0;
        
        for(int i=1;i<l;i++)
        {
            if(nums[i]>nums[i-1])
            {
                k++;
            }
        }
        
    return k;
    }
};
