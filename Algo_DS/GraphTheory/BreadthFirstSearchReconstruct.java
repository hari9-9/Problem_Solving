/**
 * An implementation of BFS with an adjacency list.
 * 
 * implemented on undirected / unweighted  Graph.
 * Reconstruct path function to find shortest path between two nodes.
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class BreadthFirstSearchReconstruct {
    // No of vertices
    private int vertices;

    // array for Adjacency list representation.
    private LinkedList<Integer> adj[];

    private Integer[] prev;

    public BreadthFirstSearchReconstruct(int v){
        vertices = v;
        
        adj = new LinkedList[v];
        for(int i=0;i<vertices;i++){
            adj[i] = new LinkedList<>();
        }

    }

    void addEdge(int v, int w){
        adj[v].add(w);
        adj[w].add(v);
    }

    public List<Integer> reconstructPath(int start, int end){
        BFS(start);
        List<Integer> path = new ArrayList<>();
        for(Integer at =end; at != null; at = prev[at]){
            path.add(at);
        }

        Collections.reverse(path);
        if(path.get(0) == start) return path;
        path.clear();
        return path;
    }


    void BFS(int s){

        prev = new Integer[vertices];
        boolean visited[] = new boolean[vertices];

        LinkedList<Integer> queue = new LinkedList<Integer>();

        visited[s] = true;
        queue.add(s);

        while(queue.size() !=0){
            // Dequeue a vertex from queue and print it
            s = queue.poll();
            //System.out.print(s+" ");
 
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
                    prev[n] = s;
                    System.out.println("node "+n+" prev Array: " + Arrays.toString(prev));
                    queue.add(n);
                }
            }
        }
        System.out.println("prev Array: " + Arrays.toString(prev));
    }

    public static void main(String[] args) throws Exception {
        int vertices = 6;
        BreadthFirstSearchReconstruct g = new BreadthFirstSearchReconstruct(vertices);
 
        g.addEdge(0, 4);
        g.addEdge(0, 2);
        g.addEdge(2, 4);
        g.addEdge(4, 1);
        g.addEdge(4, 3);
        g.addEdge(3, 1);
        g.addEdge(1, 5);

        boolean visited[] = new boolean[vertices];        
        //g.BFS(2);
        int start = 2, end = 5;
        List<Integer> path = g.reconstructPath(start,end);
        System.out.printf("The shortest path from %d to %d is: [%s]\n", start, end, formatPath(path));

    }

    private static String formatPath(List<Integer> path) {
        return String.join(
            " -> ", path.stream().map(Object::toString).collect(java.util.stream.Collectors.toList()));
      }
}
