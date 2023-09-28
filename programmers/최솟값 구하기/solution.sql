// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/59038?language=oracle

SELECT DATETIME
FROM (
    SELECT DATETIME
    FROM ANIMAL_INS
    ORDER BY DATETIME ASC
)
WHERE ROWNUM = 1;