// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120907

class Solution {
    public String[] solution(String[] quiz) {
        int len = quiz.length;
        String[] answer = new String[len];
        String[] split = new String [len];
        for(int i = 0; i < len; i++){
            split = quiz[i].split(" ");
            int num1 = Integer.parseInt(split[0]);
            int num2 = Integer.parseInt(split[2]);
            int num3 = Integer.parseInt(split[4]);
            if(split[1].equals("-")){
                if(num1 - num2 == num3){
                    answer[i] = "O";
                } else{
                    answer[i] = "X";
                }
            }
            if(split[1].equals("+")){
                if(num1 + num2 == num3){
                    answer[i] = "O";
                } else{
                    answer[i] = "X";
                }
            }
        }
        return answer;
    }
}