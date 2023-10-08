// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181914

class Solution {
    public int solution(String number) {
        // 문자열을 숫자로 변환하고 각 자리 숫자를 합산
        int sum = 0;
        for (int i = 0; i < number.length(); i++) {
            char digitChar = number.charAt(i);
            int digit = Character.getNumericValue(digitChar);
            sum += digit;
        }
        
        // 합을 9로 나눈 나머지 반환
        int remainder = sum % 9;
        return remainder;
    }
}
