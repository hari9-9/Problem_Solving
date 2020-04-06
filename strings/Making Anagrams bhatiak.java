import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    public static int count(String a, char letter){
        int count=0;
        for(int i=0; i<a.length(); i++){
            if (a.charAt(i) == letter)
                count += 1;
        }
        return count;
    }


    // Complete the makeAnagram function below.
    static int makeAnagram(String a, String b, int i) {
        return (i==-1)?(0):(Math.abs(count(a, (char)(97+i)) - count(b, (char)(97+i)))) + makeAnagram(a, b, i-1);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String a = scanner.nextLine();

        String b = scanner.nextLine();

        int res = makeAnagram(a, b, 25);

        bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
