SELECT 
    n, 
    CASE 
        WHEN n = 0 THEN 0
        ELSE CEIL((1 + SQRT(1 + 8 * n)) / 2)::integer
    END AS res
FROM 
    participants;
