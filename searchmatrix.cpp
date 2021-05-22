bool searchMatrix(vector<vector<int>>& matrix, int target) 
    {
        //common for both methods
        int i=0,j=matrix[0].size()-1;int m=matrix.size();int n=matrix[0].size();
        
        //method 1 
        // if(matrix[m-1][n-1]<target)return false;
        // for(i=0;i<m;i++)
        //     if(target<=matrix[i][n-1])
        //         break;
        // for(int j=0;j<n;j++)
        //     if(target==matrix[i][j])
        //         return true;
        // return false;
        
        
        //method 2
//         for(i=0;i<m && j>=0;)
//         {
//             if(matrix[i][j]==target)
//                 return true;
//             if(matrix[i][j]>target)
//                 j--;
//             else
//                 i++;
                
//         }
//         return false;
       
        
        //method 3 
        int l=0,hi=(m*n)-1;int mid;
        while(hi>=l)
        {
            mid=(l+(hi-l)/2);
            if(matrix[mid/n][mid%n]==target)
                return true;
            if(matrix[mid/n][mid%n]<target)
                l=mid+1;
            else
                hi=mid-1;     
        }
        return false;
    }
