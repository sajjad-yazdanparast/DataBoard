CREATE USER 'sajjad_quera'@'localhost' IDENTIFIED BY 'P@ssword1401';
GRANT ALL PRIVILEGES ON *.* TO 'sajjad_quera'@'localhost' WITH GRANT OPTION;

CREATE USER 'sajjad_quera'@'%' IDENTIFIED BY 'P@ssword1401';
GRANT ALL PRIVILEGES ON *.* TO 'sajjad_quera'@'%' WITH GRANT OPTION;