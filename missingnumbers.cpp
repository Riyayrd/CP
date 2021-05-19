int missingNumber(vector<int>& nums) 
    {
        //This method one but time complexity is O(nlogn)
        // sort(nums.begin(),nums.end());int i=0;
        // for(i=0;i<nums.size();i++)
        // {
        //     if(i!=nums[i])
        //         break;
        // }
        // if(nums[nums.size()-1]!=nums.size()) return nums.size();
        // return i;
        //----------------------------------------------------------------------------
        //This is method 2 time complexity O(n)
        int sum=0;long n=nums.size();n=(n*(n+1))/2;
        for(int i=0;i<nums.size();i++)
            sum+=nums[i];
        return n-sum;
    }
