// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181832

class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int num = 1; 
        int x = 0;
        int y = 0;
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        int direction = 0;
        
        while(num <= n * n){
            answer[x][y] = num++;
            int nextY = y + dy[direction];
            int nextX = x + dx[direction];
            
            if(nextY < 0 || nextY >= n || nextX < 0 || nextX >= n || answer[nextX][nextY] != 0){
                direction = (direction + 1) % 4;
                nextY = y + dy[direction];
                nextX = x + dx[direction];
            }
            y = nextY;
            x = nextX;
        }
        
        
        return answer;
    }
}