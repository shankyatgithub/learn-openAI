

SELECT s.student_id, s.name, b.batch_id, b.name 
FROM students s 
INNER JOIN student_batches sb ON sb.student_id = s.student_id 
INNER JOIN batches b ON b.batch_id = sb.batch_id;