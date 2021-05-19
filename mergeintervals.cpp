vector<vector<int>> merge(vector<vector<int>>& in) 
    {
        vector<vector<int>>ans;
        if(in.size()==0)return ans;
        sort(in.begin(),in.end());
        vector<int>temp=in[0];
        int a=in[0][0],b=in[0][1];
        for(int i=0;i<in.size();i++)
        {
            if(in[i][0]<temp[1])
            {
                temp[1]=max(in[i][1],temp[1]);
            }
            else
            {
                ans.push_back(temp);
                temp=in[i];
            }
        }
        ans.push_back(temp);
        return ans;
    }
