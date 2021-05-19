///This is other approach to Q2
void merge(vector<int>num1,int m,vector<int>num2,int n)
{
  int i=m-1,j=n-1,t=m+n-1;
  while(j>=0)
    num1[t--] = i>=0 && num1[i]>num2[j] ? num1[i--] : num2[j--];
}
