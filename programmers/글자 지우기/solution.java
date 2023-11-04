// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181900

import java.util.*;

class Solution {
    public String solution(String my_string, int[] indices) {
        StringBuilder result = new StringBuilder(my_string);

        // indices 배열을 역순으로 정렬합니다.
        Arrays.sort(indices);
        for (int i = indices.length - 1; i >= 0; i--) {
            int indexToRemove = indices[i];
            if (indexToRemove < result.length()) {
                // 해당 인덱스의 글자를 제거합니다.
                result.deleteCharAt(indexToRemove);
            }
        }

        return result.toString();
    }
}