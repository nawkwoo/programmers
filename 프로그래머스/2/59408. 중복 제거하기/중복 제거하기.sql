-- 코드를 입력하세요
SELECT COUNT(DISTINCT NAME) AS count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;

# SELECT COUNT(*) AS count
# FROM (
#   SELECT NAME
#   FROM ANIMAL_INS
#   WHERE NAME IS NOT NULL
#   GROUP BY NAME
# ) AS unique_names;