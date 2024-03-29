-- Get the number of fans per country of origin, ordered by the number of fans
SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin
ORDER BY total_fans DESC;
