// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181943

class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        char[] c = my_string.toCharArray();
        int a = 0;
        for(int i = s; i < s + overwrite_string.length() && a < overwrite_string.length(); i++){
            c[i] = overwrite_string.charAt(a++);
        }
        String answer = String.valueOf(c);
        return answer;
    }
}