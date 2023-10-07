// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/181945

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String[] str = a.split("");
        for(String s : str){
            System.out.println(s);
        }
    }
}