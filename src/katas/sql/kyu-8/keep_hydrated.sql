SELECT id
    , hours
    , FLOOR(hours * 0.5) AS Liters 
FROM cycling;
