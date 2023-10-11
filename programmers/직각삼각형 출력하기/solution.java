// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120823

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String str = "";
        for(int i = 0; i < n; i++){
            str+="*";
            System.out.println(str);
        }
    }
}