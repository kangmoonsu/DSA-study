// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120905

import java.util.*;

class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < numlist.length; i++){
            if(numlist[i] % n == 0){
                list.add(numlist[i]);
            }
        }
        
        int[] result = new int[list.size()];
        for(int i = 0; i < result.length; i++){
            result[i] = list.get(i);
        }
        
        
        return result;
    }
}