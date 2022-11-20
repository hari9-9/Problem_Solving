import java.util.Iterator;
import java.util.LinkedList;

public class BreadthFirstSearch {

    // No of vertices
    private int vertices;

    // array for Adjacency list representation.
    private LinkedList<Integer> adj[];

    public BreadthFirstSearch(int v){
        vertices = v;
        
        adj = new LinkedList[v];
        for(int i=0;i<vertices;i++){
            adj[i] = new LinkedList<>();
        }

    }

    void addEdge(int v, int w){
        adj[v].add(w);
    }

    void BFS(int s){
        boolean visited[] = new boolean[vertices];

        LinkedList<Integer> queue = new LinkedList<Integer>();

        visited[s] = true;
        queue.add(s);

        while(queue.size() !=0){
            // Dequeue a vertex from queue and print it
            s = queue.poll();
            System.out.print(s+" ");
 
            // Get all adjacent vertices of the dequeued vertex s
            // If a adjacent has not been visited, then mark it
            // visited and enqueue it
            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext())
            {
                int n = i.next();
                if (!visited[n])
                {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
    



    public static void main(String[] args) throws Exception {
        int vertices = 4;
        BreadthFirstSearch g = new BreadthFirstSearch(vertices);
 
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);

        boolean visited[] = new boolean[vertices];
        System.out.println("Following is Breadth First Traversal "+
        "(starting from vertex 2)");
        
        g.BFS(2);

    }
}