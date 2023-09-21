// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12931

import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        while (n > 0) {
            // N을 10으로 나누면 가장 오른쪽 자릿수를 얻을 수 있습니다.
            int digit = n % 10;
            answer += digit;
            
            // 다음 자릿수를 확인하기 위해 N을 10으로 나눕니다.
            n /= 10;
        }
    

        return answer;
    }
}