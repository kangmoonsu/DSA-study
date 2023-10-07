// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181919

import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        
        list.add(n); // 0번째 인덱스에 n을 미리 추가

        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
            list.add(n); // 홀수, 짝수에 따라 계산 이후에 리스트에 추가
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) { // 리스트를 배열로 변환
            answer[i] = list.get(i);
        }
        return answer;
    }
}