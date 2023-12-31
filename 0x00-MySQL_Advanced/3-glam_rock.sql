-- Lists all bands with Glam Rock
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan FROM 
