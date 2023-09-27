// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/132267

class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        
        int emptyCount = n;
        
        while(a <= emptyCount){
            int changeCount = emptyCount / a * b;
            int remainCount = emptyCount % a;
            
            answer += changeCount;
            emptyCount = changeCount + remainCount;
        }
        
        return answer;
    }
}