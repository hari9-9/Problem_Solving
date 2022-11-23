/**
 * An implementation of BFS with a Grid.
 * 
 * We find the minimum moves required to reach Destination.
 */
import java.util.LinkedList;

public class BfsGridShortestPath {

    private int R,C;
    private char [][] m;
    private int sr,sc;
    private int move_count;
    private int nodes_left_in_layer = 1;
    private int nodes_in_next_layer = 0;
    private boolean reached_end = false;
    private int [] dr = {-1, 1, 0, 0};
    private int [] dc = {0, 0, 1, -1};
    private boolean [][] visited;
    private LinkedList<Integer> rq = new LinkedList<Integer>();
    private LinkedList<Integer> cq = new LinkedList<Integer>();

    public BfsGridShortestPath(char [][] grid, int startR, int startC){
        m = grid;
        sr = startR;
        sc = startC;
        move_count = 0;
        R = m.length-1;
        C = m[0].length-1;
        visited = new boolean[R+1][C+1];

    }

    void explore_neighbours(int r, int c){
        for(int i=0;i<4;i++){
            int rr = r+dr[i];
            int cc = c+dc[i];

            if (rr < 0 || cc < 0){
                continue;
            }

            if(rr> R || cc>C){
                continue;
            }

            if(visited[rr][cc]){
                continue;
            }

            if(m[rr][cc]=='#'){
                continue;
            }

            rq.add(rr);
            cq.add(cc);
            visited[rr][cc] = true;
            nodes_in_next_layer++;
        }
    }

    int solve(){
        rq.add(sr);
        cq.add(sc);
        visited[sr][sc] = true;
        while(rq.size() != 0){
            int r = rq.poll();
            int c = cq.poll();
            if(m[r][c] == 'e'){
                reached_end = true;
                break;
            }
            explore_neighbours(r,c);

            nodes_left_in_layer--;
            if(nodes_left_in_layer==0){
                nodes_left_in_layer = nodes_in_next_layer;
                nodes_in_next_layer = 0;
                move_count++;
            }
        }
        if(reached_end){
            return move_count;
        }
        return -1;
    }


    public static void main(String[] args) throws Exception {
        char[][] grid = { { '#', '.', '#', 's' },
        { '.', '#', '.', '.' },
        { '#', '.', '.', '.' },
        { 'e', '.', '.', '.' } };
        int sr = 0;
        int sc = 3;
        BfsGridShortestPath g = new BfsGridShortestPath(grid, sr, sc);
        int res = g.solve();
        System.out.println("moves= " +res);


    }
}
