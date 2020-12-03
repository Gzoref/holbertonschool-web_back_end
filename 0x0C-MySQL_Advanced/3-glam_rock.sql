-- Lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, (ifnull(split, 2020) - formed) lifespan
FROM
	metal_bands
WHERE
	style LIKE '%Glam rock%'
GROUP BY
	lifespan
ORDER BY
	lifespan DESC
