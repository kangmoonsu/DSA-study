// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120904

class Solution {
    public int solution(int num, int k) {
        
        String str = Integer.toString(num);
        String[] arr = str.split("");
        for(int i = 0; i < arr.length; i++){
            if(arr[i].equals(Integer.toString(k))){
                return i + 1;
            } 
        }
        return -1;
    }
}