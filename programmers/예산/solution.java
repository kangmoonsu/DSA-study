// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12982

import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        for (int i = 0; i < d.length; i++) {
            if (budget >= d[i]) { // 예산 초과하지 않는 부서에만 지원
                budget -= d[i];
                answer++;
            } else {
                break; // 예산을 초과한 경우 지원 종료
            }
        }
        return answer;
    }
}
