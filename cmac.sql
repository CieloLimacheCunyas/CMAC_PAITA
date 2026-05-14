-- =========================
-- NUEVA BASE DE DATOS
-- =========================

CREATE DATABASE cmac_paita_system;

USE cmac_paita_system;

-- =========================
-- TABLA USUARIOS
-- =========================

CREATE TABLE usuarios(

    id INT AUTO_INCREMENT PRIMARY KEY,

    dni VARCHAR(8)
    UNIQUE NOT NULL,

    nombre VARCHAR(150)
    NOT NULL,

    tarjeta VARCHAR(16)
    UNIQUE NOT NULL,

    password VARCHAR(255)
    NOT NULL,

    pin VARCHAR(255)
    NOT NULL,

    created_at TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP

);

-- =========================
-- VER TABLA
-- =========================

SELECT * FROM usuarios;

-- =========================
-- VER COLUMNAS
-- =========================

DESCRIBE usuarios;