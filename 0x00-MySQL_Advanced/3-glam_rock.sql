USE holberton;

SELECT 
    name AS band_name, 
    IFNULL(
        2022 - IFNULL(split, 2022), 
        0
    ) AS lifespan
FROM 
    bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    lifespan DESC;
