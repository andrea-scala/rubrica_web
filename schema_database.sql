CREATE DATABASE IF NOT EXISTS rubrica CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'rubrica'@'localhost' IDENTIFIED BY 'rubrica';
GRANT ALL PRIVILEGES ON rubrica.* TO 'rubrica'@'localhost';
FLUSH PRIVILEGES;

USE rubrica;

CREATE TABLE IF NOT EXISTS lista_contatti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cognome VARCHAR(100) NOT NULL,
    indirizzo VARCHAR(255),
    telefono VARCHAR(20),
    eta INT
);
