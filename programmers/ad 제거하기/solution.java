// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181870

import java.util.*;

class Solution {
    public String[] solution(String[] strArr) {
        List<String> list = new ArrayList<>();
        for(int i = 0; i < strArr.length; i++){
            if(!strArr[i].contains("ad")){
                list.add(strArr[i]);
            }
        }
        String[] answer = new String[list.size()];
        
        for (int i = 0 ; i < list.size() ; i++){
            answer[i] = list.get(i);
        } 
        return answer;
    }
}