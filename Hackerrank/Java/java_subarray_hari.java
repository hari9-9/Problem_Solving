import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a = new int[n];
        for(int i=0; i<n;i++)
        {
            a[i] = scan.nextInt();
            
        }
        scan.close();
        int count = 0;
        for(int j=0; j<n;j++)
        {
            int sum=0;
            for(int k=j; k<n;k++)
            {
                sum = a[k]+sum;
                if(sum<0)
                {
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}
