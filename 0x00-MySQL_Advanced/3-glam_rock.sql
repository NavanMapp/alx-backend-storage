-- List bands with "Glam rock" as their main style and rank them by longevity
SELECT band_name,
       CASE
           WHEN formed = 0 OR split = 0 THEN 0
           ELSE (2022 - formed) - (2022 - split)
       END AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
