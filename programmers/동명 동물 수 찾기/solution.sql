// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/59041

-- 코드를 입력하세요
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME;