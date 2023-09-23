// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12903

class Solution {
    public String solution(String s) {
        int length = s.length();
        int middleIndex = length / 2;
        if (length % 2 == 0) {
            // 짝수 길이인 경우
            return s.substring(middleIndex - 1, middleIndex + 1);
        } else {
            // 홀수 길이인 경우
            return s.substring(middleIndex, middleIndex + 1);
        }
    }
}