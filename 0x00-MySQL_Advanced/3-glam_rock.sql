-- List bands with Glam rock as their main style, ranked by longevity
-- Lifespan is calculated as years until 2022

SELECT
    band_name,
    CASE
        WHEN formed IS NULL OR formed = 0 THEN 0
        ELSE IFNULL(2022 - formed, 0)
    END AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC, band_name;
