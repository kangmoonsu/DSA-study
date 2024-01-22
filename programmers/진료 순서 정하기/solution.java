// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120835

import java.util.*;

class Solution {
    public int[] solution(int[] emergency) {
    	
        int[] copy = new int[emergency.length];
        int[] answer = new int[emergency.length];
        
        for(int i = 0; i < emergency.length; i++) {
            copy[i] = emergency[i];
        }
        
        Arrays.sort(copy);
        
        for(int i = 0; i < emergency.length; i++) {
            for(int j = 0; j < emergency.length; j++) {
                if(copy[i] == emergency[j]) {
                    answer[j] = emergency.length - i;
                }
            }
        }
        return answer;
    }
}