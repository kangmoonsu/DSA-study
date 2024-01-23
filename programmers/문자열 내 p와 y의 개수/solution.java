// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/12916

class Solution {
	boolean solution(String s) {
		int pCnt = 0;
        int yCnt = 0;
		String[] array = s.toLowerCase().split(""); 
		
		for (int i = 0; i < array.length; i++) {
			if ("p".equals(array[i])) { 
				pCnt++;
			} else if ("y".equals(array[i])) {
				yCnt++;
			}
		}
		if (pCnt != yCnt) {
			 return false;
		}
			 return true;
	}
}