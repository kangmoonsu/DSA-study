// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120815

class Solution {
	public int solution(int n) {
		int answer = 0;
		for (int i = 1; i <= 6 * n; i++) {
			if (6 * i % n == 0) {
				answer = i;
				break;
			}
		}
		return answer;
	}
}