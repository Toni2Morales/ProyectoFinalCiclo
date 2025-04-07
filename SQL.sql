CREATE DATABASE BBDDProyecto;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contraseña VARCHAR(100) NOT NULL);

INSERT INTO usuarios (correo, contraseña)
VALUES ('ejemplo@email.com', 'contraseña_segura');

SELECT * FROM usuarios;
