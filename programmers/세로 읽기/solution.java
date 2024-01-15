// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181904

class Solution {
    public String solution(String my_string, int m, int c) {
        char[] arr = my_string.toCharArray();
        String answer = "";
        for(int i = c-1; i < arr.length; i+=m){
            answer+=arr[i];
        }
        return answer;
    }
}