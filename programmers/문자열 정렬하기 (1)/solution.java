// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120850

import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
    	my_string = my_string.replaceAll("[a-z]", ""); 
        
        String[] arr = my_string.split("");
        int[]answer = new int[arr.length];
        
        for (int i = 0; i < arr.length; i++) {
        	answer[i] = Integer.parseInt(arr[i]);
		}
        Arrays.sort(answer);
        
    	return answer;
    }
}