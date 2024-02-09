class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans= new LinkedList<>();
        for(int i=0;i<numRows;i++){
            Integer[] data = new Integer[i+1];
            Arrays.fill(data,1);
            List<Integer> list = Arrays.asList(data);
            for(int j=1;j<i;j++){
                list.set(j, ans.get(i-1).get(j) + ans.get(i-1).get(j-1));
                //list[j] = ans[i-1][j]+ans[i-1][j-1];
            }
            ans.add(list);
        }
        return ans;
    }
}