// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/1845

import java.util.HashSet;

public class Solution {
  public int solution(int[] nums) {
    int max = nums.length / 2;

    HashSet<Integer> numsSet = new HashSet<>();

    for (int num : nums) {
      numsSet.add(num);
    }
      
    if (numsSet.size() > max) {
      return max;
    } else {
      return numsSet.size();
    }
  }

}