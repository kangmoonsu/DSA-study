// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120845

class Solution {
    public int solution(int[] box, int n) {
        int answer = 1;
        for(int i = 0; i < box.length; i++){
            answer *= box[i] / n;
        }
        return answer;
    }
}