

SELECT s.name, b.batch_name 
FROM students s 
INNER JOIN batches b 
ON s.batch_id = b.id;