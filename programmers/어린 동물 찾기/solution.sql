// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/59037?language=oracle

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID;