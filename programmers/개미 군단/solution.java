// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/120837

class Solution {
    public int solution(int hp) {
        int generalsAttack = 5; // 장군개미의 공격력
        int soldiersAttack = 3; // 병정개미의 공격력
        int antsNeeded = 0;

        // 장군개미를 최대한 사용하기 위해 장군개미의 수를 최대한 늘림
        antsNeeded += (hp / generalsAttack);
        hp %= generalsAttack;

        // 남은 체력이 0보다 크면 병정개미를 사용하여 체력을 맞춤
        if (hp > 0) {
            antsNeeded += (hp / soldiersAttack);
            hp %= soldiersAttack;
        }

        // 남은 체력이 0보다 크면 일개미를 사용하여 체력을 맞춤
        if (hp > 0) {
            antsNeeded += hp;
        }

        return antsNeeded;
    }
}