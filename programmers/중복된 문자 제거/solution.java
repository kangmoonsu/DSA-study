// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120888

import java.util.*;

class Solution {
    public String solution(String my_string) {
        Set<Character> charSet = new LinkedHashSet<>();
        
        for (char c : my_string.toCharArray()) {
            charSet.add(c);
        }
        
        StringBuilder result = new StringBuilder();
        for (Character c : charSet) {
            result.append(c);
        }
        
        return result.toString();
    }
}