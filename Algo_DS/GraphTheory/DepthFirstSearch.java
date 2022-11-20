import java.util.Iterator;
import java.util.LinkedList;

public class DepthFirstSearch {

    // No of vertices
    private int vertices;

    // array for Adjacency list representation.
    private LinkedList<Integer> adj[];

    public DepthFirstSearch(int v){
        vertices = v;
        
        adj = new LinkedList[v];
        for(int i=0;i<vertices;i++){
            adj[i] = new LinkedList<>();
        }

    }

    void addEdge(int v, int w){
        adj[v].add(w);
    }

    void DFS(int v , boolean visited[]){
         // Mark the current node as visited and print it
         visited[v] = true;
         System.out.print(v + " ");
  
         // Recur for all the vertices adjacent to this
         // vertex
         Iterator<Integer> i = adj[v].listIterator();
         while (i.hasNext()) {
             int n = i.next();
             if (!visited[n])
                 DFS(n, visited);
         }

    }


    public static void main(String[] args) throws Exception {
        int vertices = 4;
        DepthFirstSearch g = new DepthFirstSearch(vertices);
 
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        boolean visited[] = new boolean[vertices];
        System.out.println(
        "Following is Depth First Traversal "
        + "(starting from vertex 2)"); 
                // Function call
                g.DFS(2,visited);

    }
}