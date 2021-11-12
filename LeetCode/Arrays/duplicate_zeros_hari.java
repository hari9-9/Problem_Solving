class Solution {
    public void duplicateZeros(int[] arr) {
        int n = arr.length;
        int i,j;
        i=0;
        while(i<n)
        {
            if(arr[i]==0 && i!=n-1)
            {
                j=n-2;
                while(j>i)
                {
                    arr[j+1] = arr[j];
                    j--;
                }
                arr[i+1]=0;
                i++;
            }
            i++;
        }
        
        
    }
}
