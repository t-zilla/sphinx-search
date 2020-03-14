CREATE TABLE IF NOT EXISTS questions(
    id INT(8) UNSIGNED PRIMARY KEY,
    owner_user_id INT(8) UNSIGNED,
    creation_date DATETIME,
    parent_id INT(8) UNSIGNED,
    score INT(6),
    body TEXT
);

TRUNCATE TABLE questions;

LOAD DATA LOCAL INFILE '/datasets/Questions.csv' 
INTO TABLE questions
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

DELETE FROM questions
WHERE body IS NULL;

SELECT COUNT(*) FROM questions;

SELECT id, body FROM questions LIMIT 0,5;
