void nextPermutation(vector<int>& nums) 
    {
        if(nums.size()==0 || nums.size()==1)return;
        int i=0,j=0;
        for(i=nums.size()-2;i>=0;i--)
        {
            if(nums[i]<nums[i+1])
                break;
        }
        if(i<0)
        {
            reverse(nums.begin(),nums.end());
        }
        else
        {
            for(j=nums.size()-1;j>i;j--)
            {
                if(nums[i]<nums[j])
                    break;
            }
            int temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
            reverse(nums.begin()+i+1,nums.end());
            return;
        }
    }
