// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/59410

-- 코드를 입력하세요
SELECT ANIMAL_TYPE, NVL(NAME,'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;