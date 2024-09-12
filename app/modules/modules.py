from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

class CFDRecepcion(db.Model):
    __tablename__ = 'CFD_RECEPCION'
    idfactura = db.Column(db.Integer, primary_key=True)
    estado_envio_sat = db.Column(db.String)
    fecha_recepcion = db.Column(db.DateTime)

class CFDRecepcionCR(db.Model):
    __tablename__ = 'CFD_RECEPCION_CR'
    id = db.Column(db.Integer, primary_key=True)
    cancelado = db.Column(db.Integer)
    fecha_cancelacion = db.Column(db.DateTime)
    fecha_recepcion = db.Column(db.DateTime)
    estado_envio_sat = db.Column(db.String)

class Parametros(db.Model):
    __tablename__ = 'PARAMETRO'
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.String)
    nombre = db.Column(db.String)