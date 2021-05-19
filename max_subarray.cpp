int maxSubArray(vector<int>& nums) 
{
        int maxa=INT_MIN,sum=0;
        for(int i=0;i<nums.size();i++)
        {
            sum=sum+nums[i];
            maxa=max(sum,maxa);
            if(sum<0)
                sum=0;
        }
        return maxa;
}
