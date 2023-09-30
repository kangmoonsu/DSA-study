// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181938

class Solution {
    public int solution(int a, int b) {
        String abStr = Integer.toString(a) + Integer.toString(b);
        int a_b = Integer.valueOf(abStr);
        
        return a_b >= 2 * a * b ? a_b : 2 * a * b;
    }
}