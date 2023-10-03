// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120893

class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        char[] a = my_string.toCharArray();
        for (int i = 0; i < a.length; i++) {
            char c = a[i];
            if (Character.isUpperCase(c)) {
                c = Character.toLowerCase(c);
            } else if (Character.isLowerCase(c)) {
                c = Character.toUpperCase(c);
            }
            answer.append(c);
        }
        return answer.toString();
    }
}
