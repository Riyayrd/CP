#include <iostream>
using namespace std;
void mergearray(int arr1[],int arr2[],int m,int n)
{
    int gap=(m+n)/2;
            while(gap>0)
            {
                int i=0;
                for(i=0;i+gap<m+n;i++)
                {
                    if(i+gap<m)
                    {
                        if(arr1[i]>arr1[i+gap])
                            swap(arr1[i],arr1[i+gap]);
                    }
                    else if(i+gap>=m &&i<m)
                    {   
                        if(arr1[i]>arr2[i+gap-m-1])
                            swap(arr1[i],arr2[i+gap-m-1]);
                    }
                    else if(i+gap>m && i>=m)
                    {  
                        if(arr2[i-m-1]>arr2[i+gap-m-1])
                            swap(arr2[i-m-1],arr2[i+gap-m-1]);                        
                    }
                }
                gap=gap/2;
            }
            // code here 
        }
int main() {
    int arr1[4]={1,2,5,7};
    int arr2[5]={2,3,4,6,8};
    mergearray(&arr1[0],&arr2[0],4,5);
    for(int i=0;i<4;i++)
        cout<<arr1[i]<<" ";
    for(int i=0;i<5;i++)
        cout<<arr2[i]<<" ";
	return 0;
}
