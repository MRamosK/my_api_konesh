from sqlalchemy import func # type: ignore
from sqlalchemy.sql import text # type: ignore
from app.modules.modules import CFDRecepcion, CFDRecepcionCR, Parametros,db

# Data Access Layer (DAL)
class CFDIRepository:
    """
    Repository for accessing CFDI-related data from the database.
    """

    @staticmethod
    def fetch_pending_cfd_count() -> int: # Tiempo
        """
        Fetch the count of pending CFDIs based on a deadline.
        

        Returns:
            int: The count of pending CFDIs.
        """
        
        # Subquery to get the interval value from the parametro table
        subquery = (
            db.session.query(func.coalesce(
                db.session.query(Parametros.valor)
                .filter(Parametros.nombre == "cfdi_status")
                .scalar_subquery(), 0)
            )
        ).scalar()

        # Main query to count the relevant records in the cfd_recepcion table
        count_query = db.session.query(func.count()).select_from(
            CFDRecepcion
        ).filter(
            CFDRecepcion.estado_envio_sat.is_(None),
            CFDRecepcion.fecha_recepcion <= func.date_sub(func.now(), text(f"INTERVAL {subquery} MINUTE"))
        ).with_hint(CFDRecepcion, 'FORCE INDEX (IDX_ESTADO_ENVIO_SAT)', 'mysql')

        # Execute the query and return the result
        result = db.session.execute(count_query).scalar()

        return result

    @staticmethod
    def fetch_extemporaneous_cfd_count() -> int: # Tiempo
        """
        Fetch the count of extemporaneous CFDIs based on a deadline.

        Returns:
            int: The count of extemporaneous CFDIs.
        """
        # Subquery to get the value from the parametro table
        subquery =  (
            db.session.query(func.coalesce(
                db.session.query(Parametros.valor)
                .filter(Parametros.nombre == "cfdi_extemporaneo")
                .scalar_subquery(), 0)
            )
        ).scalar()

        # Main query to count the relevant records in the cfd_recepcion table
        count_query = db.session.query(func.count()).select_from(
            CFDRecepcion
        ).filter(
            CFDRecepcion.estado_envio_sat == 'Comprobante recibido extemporáneamente',
            CFDRecepcion.fecha_recepcion <=  func.date_sub(func.now(), text(f"INTERVAL {subquery} MINUTE"))
        ).with_hint(CFDRecepcion, 'FORCE INDEX (IDX_FECHA_RECEP_ESTADO_ENVIO_SAT)', 'mysql')

        # Execute the query and return the result
        result = db.session.execute(count_query).scalar()

        return result

    @staticmethod
    def fetch_incidents_cfd_count() -> int: #Fecha
        """
        Fetch the count of CFDIs with incidents based on a deadline.

        Returns:
            int: The count of CFDIs with incidents.
        """
        # Subquery to get the value from the parametro table
        subquery = db.session.query(Parametros.valor).filter(Parametros.nombre == "cfdi_incidentes").scalar_subquery()


        # Main query to count the relevant records in the cfd_recepcion table
        count_query = db.session.query(func.count()).select_from(
            CFDRecepcion
        ).filter(
            CFDRecepcion.estado_envio_sat == 'Comprobante recibido con incidencias',
            CFDRecepcion.fecha_recepcion >= subquery
        ).with_hint(CFDRecepcion, 'FORCE INDEX (IDX_FECHA_RECEP_ESTADO_ENVIO_SAT)', 'mysql')

        # Execute the query and return the result
        result = db.session.execute(count_query).scalar()

        return result

    @staticmethod
    def fetch_rejected_cfd_count() -> int:
        """
        Fetch the count of rejected CFDIs.

        Returns:
            int: The count of rejected CFDIs.
        """
        return db.session.query(func.count(CFDRecepcion.idfactura)).filter(
            CFDRecepcion.estado_envio_sat == 'Comprobante rechazado'
        ).with_hint(CFDRecepcion, 'FORCE INDEX(IDX_ESTADO_ENVIO_SAT)').scalar()

    @staticmethod
    def fetch_peding_cancellation_cr_count() -> int:
        """
        Fetch the count of CRs pending cancellation.

        Returns:
            int: The count of CRs pending cancellation.
        """
        return db.session.query(func.count(CFDRecepcionCR.id)).filter(
            CFDRecepcionCR.cancelado.in_([-1, -2])
        ).scalar()

    @staticmethod
    def fetch_cancellation_error_cr_count() -> int: # Fecha
        """
        Fetch the count of CRs with cancellation errors.

        Returns:
            int: The count of CRs with cancellation errors.
        """
        subquery = db.session.query(Parametros.valor).filter(Parametros.nombre == "cr_cancelacion_error").scalar_subquery()
        
        
        # Main query to count the relevant records in the cfd_recepcion table
        count_query = db.session.query(func.count()).select_from(
            CFDRecepcionCR
        ).filter(
            CFDRecepcionCR.cancelado.in_([1308]),
            CFDRecepcionCR.fecha_cancelacion >= subquery
        )
        
        # Execute the query and return the result
        result = db.session.execute(count_query).scalar()
        
        return result

    @staticmethod
    def fetch_status_cr_count() -> int: # Tiempo
        """
        Fetch the count of CRs with pending status based on a deadline.

        Returns:
            int: The count of CRs with pending status.
        """
        # Subquery to get the interval value from the parametro table
        subquery = (
            db.session.query(func.coalesce(
                db.session.query(Parametros.valor)
                .filter(Parametros.nombre == "cr_status")
                .scalar_subquery(), 0)
            )
        ).scalar()
        
        # Main query to count the relevant records in the cfd_recepcion table
        count_query = db.session.query(func.count()).select_from(
            CFDRecepcionCR
        ).filter(
            CFDRecepcionCR.estado_envio_sat.is_(None),
            CFDRecepcionCR.fecha_recepcion < func.date_sub(func.now(), text(f"INTERVAL {subquery} MINUTE"))
        )
        
        # Execute the query and return the result
        result = db.session.execute(count_query).scalar()

        return result
