// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181838

class Solution {
    public int solution(int[] date1, int[] date2) {
        // 먼저 연도(year)를 비교합니다.
        if (date1[0] < date2[0]) {
            return 1; // date1이 date2보다 앞선 연도
        } else if (date1[0] > date2[0]) {
            return 0; // date1이 date2보다 뒤에 있는 연도
        } else {
            // 연도가 같은 경우 월(month)를 비교합니다.
            if (date1[1] < date2[1]) {
                return 1; // date1이 date2보다 앞선 월
            } else if (date1[1] > date2[1]) {
                return 0; // date1이 date2보다 뒤에 있는 월
            } else {
                // 연도와 월이 같은 경우 일(day)를 비교합니다.
                if (date1[2] < date2[2]) {
                    return 1; // date1이 date2보다 앞선 날짜
                } else {
                    return 0; // date1이 date2와 같거나 뒤에 있는 날짜
                }
            }
        }
    }
}