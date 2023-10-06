// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120891

class Solution {
    public int solution(int order) {
        int answer = 0;
        String num = Integer.toString(order);
        
        for (int i = 0; i < num.length(); i++) {
            char c = num.charAt(i);
            if (c == '3' || c == '6' || c == '9') {
                answer++;
            }
        }
        
        
        return answer;
    }
}