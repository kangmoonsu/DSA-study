// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12954

class Solution {
    public int[] solution(int x, int n) {
        int[] answer = new int[n];
        int a = x;
        for(int i = 0;i < n; i++){
            answer[i] = a;
            a += x;
        }
        return answer;
    }
}