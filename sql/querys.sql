-- Inserts de parametros --

-- CFDI
INSERT INTO parametro (NOMBRE, VALOR, RFC_EMPRESA) values ("cfdi_status","30","SISTEMA");
select * from parametro p where p.NOMBRE = "cfdi_status";

-- CFDI_EXTEMPORANEOS
INSERT INTO parametro (NOMBRE, VALOR, RFC_EMPRESA) values ("cfdi_extemporaneo","30","SISTEMA");
select * from parametro p where p.NOMBRE = "cfdi_extemporaneo";

-- CFDI_INCIDENCIAS
INSERT INTO parametro (NOMBRE, VALOR, RFC_EMPRESA) values ("cfdi_incidentes","2024-08-23 12:00:00","SISTEMA");
select * from parametro p where p.NOMBRE = "cfdi_incidentes";

-- CR
INSERT INTO parametro (NOMBRE, VALOR, RFC_EMPRESA) values ("cr_status","30","SISTEMA");
select * from parametro p where p.NOMBRE = "cr_status";

-- CR_CANCELACIONES_ERROR
INSERT INTO parametro (NOMBRE, VALOR, RFC_EMPRESA) values ("cr_cancelacion_error","2024-01-01 00:00:00","SISTEMA");
select * from parametro p where p.NOMBRE = "cr_cancelacion_error";


-- Selects para datos --

-- CFDI tiempo
select count(*) from cfd_recepcion cfd force index(IDX_ESTADO_ENVIO_SAT) where cfd.ESTADO_ENVIO_SAT 
is null and cfd.FECHA_RECEPCION <= DATE_SUB(NOW(), INTERVAL 
(SELECT valor FROM parametro  WHERE nombre = "cfdi_status") MINUTE);

-- CFDI_RECHAZADOS
SELECT count(*) 
FROM CFD_RECEPCION force index(IDX_ESTADO_ENVIO_SAT) 
WHERE ESTADO_ENVIO_SAT = 'Comprobante rechazado';

-- CFDI_EXTEMPORANEOS *tiempo
select count(*) from cfd_recepcion cfd force index(IDX_FECHA_RECEP_ESTADO_ENVIO_SAT) 
WHERE cfd.ESTADO_ENVIO_SAT = 'Comprobante recibido extemporáneamente' AND 
cfd.FECHA_RECEPCION <= date_sub(now(), interval (select valor from parametro where nombre = "cfdi_extemporaneo") minute);

-- CFDI_INCIDENCIAS fecha
select count(*) from cfd_recepcion cfd force index(IDX_FECHA_RECEP_ESTADO_ENVIO_SAT)
where cfd.ESTADO_ENVIO_SAT = 'Comprobante recibido con incidencias' and cfd.FECHA_RECEPCION >=  
(select valor from parametro p where p.nombre = "cfdi_incidentes");

-- CR tiempo
select count(*) from cfd_recepcion_cr cr where cr.ESTADO_ENVIO_SAT 
is null and cr.FECHA_RECEPCION <= DATE_SUB(NOW(), INTERVAL 
(SELECT valor FROM parametro  WHERE nombre = "cr_status") MINUTE);

-- CR_CANCELACIONES_PENDIENTES
SELECT COUNT(*)
FROM CFD_RECEPCION_CR
WHERE CANCELADO IN (-1, -2);

-- CR_CANCELACIONES_ERROR *fecha
select count(*) from cfd_recepcion_cr cr  where cr.CANCELADO in (1308) and 
cr.FECHA_CANCELACION  >= (select valor from parametro p where p.nombre = "cr_cancelacion_error");

