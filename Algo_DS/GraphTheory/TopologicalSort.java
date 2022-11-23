
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
;

public class TopologicalSort {
    private int vertices;

    // array for Adjacency list representation.
    private LinkedList<Integer> adj[];

    public TopologicalSort(int v){
        vertices = v;
        adj = new LinkedList[v];
        for(int i=0;i<vertices;i++){
            adj[i] = new LinkedList<>();
        }
    }

    void addEdge(int v, int w){
        adj[v].add(w);
    }

    private int dfs(int i, int at, boolean[] visited, int[] ordering){
        visited[at] = true;
        Iterator<Integer> edges = adj[at].listIterator();
        while(edges.hasNext()){
            int next = edges.next();
            if(visited[next]== false){
                i= dfs(i, next, visited, ordering);
            }
        }
        ordering[i] = at;
        return i-1;
    }

    public int [] topSort(){
        int N = vertices;
        boolean visited[] = new boolean[vertices];
        int ordering[] = new int[vertices];
        int i = vertices -1;

        for(int at = 0; at < vertices;at++){
            if(!visited[at]){
                i= dfs(i,at,visited,ordering);
            }
        }
        return ordering;
    }

    public static void main(String[] args) throws Exception {
        int vertices = 9;
        TopologicalSort g = new TopologicalSort(vertices);
        g.addEdge(0,2);
        g.addEdge(0,3);
        g.addEdge(1,3);
        g.addEdge(1,5);
        g.addEdge(2,6);
        g.addEdge(3,6);
        g.addEdge(3,7);
        g.addEdge(4,7);
        g.addEdge(5,8);

        int[] topsorted = g.topSort();
        System.out.println("Topological sorted order: "+Arrays.toString(topsorted));
    }
}
