// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12948

class Solution {
    public String solution(String phone_number) {
        int len = phone_number.length();
        
        // 뒤 4자리를 제외한 부분을 '*'로 채운 문자열 생성
        String masked = "*".repeat(len - 4);
        
        // 뒤 4자리를 기존 전화번호에서 가져와서 덧붙임
        masked += phone_number.substring(len - 4);
        
        return masked;
    }
}