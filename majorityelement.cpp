 int majorityElement(vector<int>& nums) 
    {
//         map<int,int>p;
        
//         for(int i =0;i<nums.size();i++ )
//         {
//             p[nums[i]]+=1;
//         }
//         for(auto i=p.begin();i!=p.end();i++)
//             if(i->second>nums.size()/2)
//                 return i->first;
           
//         return 0;
        
        int count=0,el=nums[0];
        for(int i=0;i<nums.size();i++)
        {   if(count==0)
            {
                 el=nums[i];count++;
            }
            else
            {
                if(el==nums[i])count++;
                else count--;         
            }
        }
        return el;
    }
