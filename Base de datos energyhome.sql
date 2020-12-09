CREATE DATABASE SITIO_WEB;

USE SITIO_WEB;

CREATE TABLE CLIENT(
  ID INT(15) NOT NULL AUTO_INCREMENT,
  RUT VARCHAR(18) NOT NULL UNIQUE,
  NOMBRE VARCHAR(350) NOT NULL,
  DIRECCION VARCHAR(150) NOT NULL,
  EMAIL VARCHAR(80) NOT NULL,
  TELEFONO VARCHAR(15) NOT NULL,
  CONSTRAINT CLIENT_PK PRIMARY KEY (ID)
);

CREATE TABLE CONTACT_INFORMATION(
  ID INT(15) NOT NULL AUTO_INCREMENT,
  MENSAJE VARCHAR(150) NOT NULL,
  REGISTER DATETIME,
  CLIENT_ID INT(15) NOT NULL,
  UPLOAD_IMAGE VARCHAR(450) NOT NULL,
  CONSTRAINT CONTACT_INF_PK PRIMARY KEY (ID),
  CONSTRAINT CLIENT_FK FOREIGN KEY (CLIENT_ID) REFERENCES CLIENT(ID)
);

COMMIT;