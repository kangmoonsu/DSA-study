// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181912

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        int[] a = new int[intStrs.length];
        int count = 0;

        for (int i = 0; i < intStrs.length; i++) {
            a[i] = Integer.parseInt(intStrs[i].substring(s, s + l));
            if (a[i] > k) {
                count++;
            }
        }

        int[] result = new int[count];
        int index = 0;

        for (int i = 0; i < intStrs.length; i++) {
            if (a[i] > k) {
                result[index++] = a[i];
            }
        }

        return result;
    }
}