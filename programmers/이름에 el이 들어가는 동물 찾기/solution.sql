// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/59047?language=oracle

-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME
FROM ANIMAL_INS
WHERE LOWER(NAME) LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME;