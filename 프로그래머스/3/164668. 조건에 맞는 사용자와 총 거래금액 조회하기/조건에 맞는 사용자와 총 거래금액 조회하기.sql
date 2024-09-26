-- 코드를 입력하세요
SELECT
    A.writer_id,
    B.nickname,
    A.total_sales
FROM (
    SELECT
        WRITER_ID,
        SUM(price) AS total_sales
    FROM  used_goods_board
    WHERE status = 'DONE'
    GROUP BY 1
    HAVING total_sales >= 700000) A
JOIN
    used_goods_user AS B
ON A.writer_id = B.user_id
ORDER BY A.total_sales