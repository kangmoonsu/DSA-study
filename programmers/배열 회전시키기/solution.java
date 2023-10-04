// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120844?language=java

class Solution {
    public int[] solution(int[] numbers, String direction) {
        int[] answer = new int[numbers.length];
        
        if (direction.equals("right")) {
            for (int i = 0; i < numbers.length; i++) {
                int newIndex = (i + 1) % numbers.length;
                answer[newIndex] = numbers[i];
            }
        } else {
            for (int i = 0; i < numbers.length; i++) {
                int newIndex = (i - 1 + numbers.length) % numbers.length;
                answer[newIndex] = numbers[i];
            }
        }
        
        return answer;
    }
}
