// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120812

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(int[] array) {
        if (array.length == 0) {
            return -1; 
        }
        
        Map<Integer, Integer> countMap = new HashMap<>();
        int maxCount = 0;
        int mode = -1;
        
        for (int num : array) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            int count = countMap.get(num);
            
            if (count > maxCount) {
                maxCount = count;
                mode = num;
            } else if (count == maxCount) {
                mode = -1; 
            }
        }
        
        return mode;
    }
}