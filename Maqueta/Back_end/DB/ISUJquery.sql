USE controlling;

## CONSULTAS INSERT 
INSERT INTO Usuario
SET idUsuario = "",
	alias = "mariaDb",
    contrasenia = "Maria2022",
    mail = "mariaDb@gmail.com",
	pais = "Uruguay";

INSERT INTO Cartera
SET idCartera = "",
	id_Usuario = 10;
    
INSERT INTO Operacion 
SET idOperacion = "",
	id_cartera = 10,
	id_activo = 3,
	cantidad = 5,
	precio_compra = 2320,
	fecha_compra = "2022-06-05";
    
## CONSULTAS SELECT    
SELECT * FROM Usuario;

SELECT alias, pais
FROM usuario
ORDER BY alias;

SELECT * FROM operacion
WHERE cantidad = 3;

SELECT simbolo
FROM activo
WHERE operador = 'IOL';

SELECT alias, 'registrado' AS condicion
FROM usuario;

SELECT COUNT(*)
FROM usuario
WHERE contrasenia LIKE '%22';


## CONSULTAS UPDATE
UPDATE usuario 
SET 
    pais = 'Bolivia'
WHERE
    idUsuario = 10;

UPDATE operacion 
SET 
    precio_venta = 3100,
    fecha_venta = '2022-11-08'
WHERE
    id_activo = 3 AND id_cartera = 1;
    
UPDATE operacion
SET 
    cantidad = 6
WHERE 
    idOperacion = 4;

UPDATE activo
SET 
   moneda = "Ethereum" 
WHERE 
   simbolo = "ETH" AND moneda = "pesos";
   
## CONSULTAS JOIN 
/* Calcular el valor de una operación */
SELECT 
    alias,  id_cartera, idOperacion, cantidad, precio_compra, cantidad * precio_compra AS "valor operacion"
FROM operacion
INNER JOIN
    cartera ON operacion.id_cartera = cartera.idCartera
INNER JOIN usuario 
     ON cartera.id_usuario = usuario.idUsuario;
       
/* Consultar usuarios sin registro de operaciones */    
SELECT alias, idCartera, id_Usuario, idOperacion AS "Sin registros"
FROM   cartera
INNER JOIN 
    usuario ON cartera.id_usuario = usuario.idUsuario
LEFT OUTER JOIN operacion
	ON operacion.id_cartera = cartera.idCartera
 WHERE operacion.idOperacion IS NULL;
 
/* Consultar qué activos y de qué operador tiene determinado usuario */
SELECT alias, idCartera, simbolo, operador
FROM cartera
INNER JOIN 
	usuario ON cartera.id_usuario = usuario.idUsuario
INNER JOIN 
     operacion ON cartera.idCartera = operacion.id_cartera
INNER JOIN 
      activo ON operacion.id_activo = activo.idActivo
WHERE idUsuario = 1;
 
 
 
 

   










    


