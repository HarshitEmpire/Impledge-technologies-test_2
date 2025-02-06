-- Update queries (run first)  
UPDATE Admissions SET attending_doctor_id = 29 WHERE attending_doctor_id = 3;  
UPDATE Admissions SET patient_id = 4 WHERE patient_id = 35;  

-- Doctors with Admissions  
SELECT DISTINCT d.*  
FROM Doctors d  
JOIN Admissions a ON d.doctor_id = a.attending_doctor_id;  

-- Doctors without Admissions  
SELECT d.*  
FROM Doctors d  
LEFT JOIN Admissions a ON d.doctor_id = a.attending_doctor_id  
WHERE a.attending_doctor_id IS NULL;  

-- Patients with incomplete admissions  
SELECT p.*  
FROM Patients p  
JOIN Admissions a ON p.patient_id = a.patient_id  
LEFT JOIN Doctors d ON a.attending_doctor_id = d.doctor_id  
WHERE d.doctor_id IS NULL;  