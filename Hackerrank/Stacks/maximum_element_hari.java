import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'getMax' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts STRING_ARRAY operations as parameter.
     */

    public static List<Integer> getMax(List<String> operations) {
    // Write your code here
    int n = operations.size();
    int temp;
    Stack<Integer> stack = new Stack<Integer>();
    Stack<Integer> maxstack = new Stack<Integer>();
    List<Integer> ans = new ArrayList<Integer>();
    
    for(int i=0; i<n;i++)
    {
        String query[] = operations.get(i).split(" ");
        switch(query[0])
        {
            case "1":
                temp = Integer.parseInt(query[1]);
                stack.push(temp);
                if(maxstack.isEmpty() || maxstack.peek() <= temp)
                {
                    maxstack.push(temp);
                }
                break;
            case "2":
                temp = stack.pop();
                if(temp == maxstack.peek())
                    maxstack.pop();
                break;
            case "3":
                //System.out.println(onlyMaxs.peek());
                ans.add(maxstack.peek());
        }
    }
    return ans;
    

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> ops = IntStream.range(0, n).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        List<Integer> res = Result.getMax(ops);

        bufferedWriter.write(
            res.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}
