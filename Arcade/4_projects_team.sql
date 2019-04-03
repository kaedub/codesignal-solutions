BEGIN
	SELECT name 
    FROM projectLog 
    GROUP BY name 
    ORDER BY name;
END
