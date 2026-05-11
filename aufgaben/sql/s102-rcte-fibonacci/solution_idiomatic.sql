WITH RECURSIVE fib(i, a, b) AS (  SELECT 0, 0, 1 UNION ALL   SELECT i+1, b, a+b FROM fib WHERE i < 10) SELECT i, a AS wert FROM fib ORDER BY i;
