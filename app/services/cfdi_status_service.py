from app.repositories.cfdi_repository import CFDIRepository
from datetime import datetime

class CFDIStatusService:
    """
    Service class to handle CFDI status-related business logic.
    """

    def __init__(self, repo: CFDIRepository):
        """
        Initialize the service with a repository instance.

        Args:
            repo (CFDIRepository): An instance of the CFDIRepository.
        """
        self.repo = repo

    def get_cfd_status(self) -> dict:
        """
        Get the status of CFDIs and CRs by calling individual JSON-building methods.

        Returns:
            dict: A JSON-compatible dictionary with separated JSON structures.
        """
        fecha_actual = datetime.now()

        # Construir y retornar un JSON separado por cada estado
        return {
            "CFDI": self.build_cfdi_status_json(fecha_actual),
            "CFDI_RECHAZADOS": self.build_cfdi_rechazados_json(fecha_actual),
            "CFDI_EXTEMPORANEOS": self.build_cfdi_extemporaneos_json(fecha_actual),
            "CFDI_INCIDENCIAS": self.build_cfdi_incidencias_json(fecha_actual),
            "CR": self.build_cr_status_json(fecha_actual),
            "CR_CANCELACIONES_PENDIENTES": self.build_cr_pendientes_json(fecha_actual),
            "CR_CANCELACIONES_ERROR": self.build_cr_cancelacion_error_json(fecha_actual)
        }

    def build_cfdi_status_json(self, fecha: datetime) -> dict:
        """
        Build JSON for CFDI status.

        Args:
            fecha (datetime): The current date and time.

        Returns:
            dict: JSON structure for CFDI status.
        """
        pending_count = self.repo.fetch_pending_cfd_count()
        cfdi_status = "EXISTEN_PENDIENTES_CFDI" if pending_count > 0 else "ENVIOS_CFDI_OK"
        return {
            "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "CFDI_ESTATUS": cfdi_status,
            "CANTIDAD": str(pending_count)
        }

    def build_cfdi_rechazados_json(self, fecha: datetime) -> dict:
        """
        Build JSON for rejected CFDIs.

        Args:
            fecha (datetime): The current date and time.

        Returns:
            dict: JSON structure for rejected CFDIs.
        """
        rejected_count = self.repo.fetch_rejected_cfd_count()
        cfdi_rechazados_status = "EXISTEN_RECHAZOS" if rejected_count > 0 else "SIN_RECHAZOS"
        return {
            "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "ESTATUS_CFDI_RECHAZADOS": cfdi_rechazados_status,
            "CANTIDAD": str(rejected_count)
        }

    def build_cfdi_extemporaneos_json(self, fecha: datetime) -> dict:
        """
        Build JSON for extemporaneous CFDIs.

        Args:
            fecha (datetime): The current date and time.

        Returns:
            dict: JSON structure for extemporaneous CFDIs.
        """
        extemporaneous_count = self.repo.fetch_extemporaneous_cfd_count()
        cfdi_extemporaneos_status = "EXISTEN_EXTEMPORANEOS" if extemporaneous_count > 0 else "SIN_EXTEMPORANEOS"
        return {
            "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "ESTATUS_CFDI_EXTEMPORANEOS": cfdi_extemporaneos_status,
            "CANTIDAD": str(extemporaneous_count)
        }

    def build_cfdi_incidencias_json(self, fecha: datetime) -> dict:
        """
        Build JSON for CFDI incidents.

        Args:
            fecha (datetime): The current date and time.

        Returns:
            dict: JSON structure for CFDI incidents.
        """
        incidents_count = self.repo.fetch_incidents_cfd_count()
        cfdi_incidentes_status = "EXISTEN_INCIDENCIAS" if incidents_count > 0 else "SIN_INCIDENCIAS"
        return {
            "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "ESTATUS_CFDI_INCIDENCIAS": cfdi_incidentes_status,
            "CANTIDAD": str(incidents_count)
        }

    def build_cr_status_json(self, fecha: datetime) -> dict:
        """
        Build JSON for CR status.

        Args:
            fecha (datetime): The current date and time.

        Returns:
            dict: JSON structure for CR status.
        """
        cr_count = self.repo.fetch_status_cr_count()
        cr_status = "EXISTEN_PENDIENTES_CR" if cr_count > 0 else "ENVIOS_CR_OK"
        return {
            "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "ESTATUS_CR": cr_status,
            "CANTIDAD": str(cr_count)
        }

    def build_cr_pendientes_json(self, fecha: datetime) -> dict:
        """
        Build JSON for CR pending cancellations.

        Args:
            fecha (datetime): The current date and time.

        Returns:
            dict: JSON structure for CR pending cancellations.
        """
        cr_pending_cancellation_count = self.repo.fetch_peding_cancellation_cr_count()
        cr_pediente_cancelar_status = "EXISTEN_PENDIENTES_CANCELACIONES_CR" if cr_pending_cancellation_count > 0 else "CANCELACIONES_CR_OK"
        return {
            "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "ESTATUS_CR_CANCELACIONES_PENDIENTES": cr_pediente_cancelar_status,
            "CANTIDAD": str(cr_pending_cancellation_count)
        }

    def build_cr_cancelacion_error_json(self, fecha: datetime) -> dict:
        """
        Build JSON for CR cancellation errors.

        Args:
            fecha (datetime): The current date and time.

        Returns:
            dict: JSON structure for CR cancellation errors.
        """
        cr_cancellation_error_count = self.repo.fetch_cancellation_error_cr_count()
        cr_cancelacion_error_status = "EXISTEN_ERRORES_CANCELACION_CR" if cr_cancellation_error_count > 0 else "ESTATUS_CR_CANCELACIONES_OK"
        return {
            "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "ESTATUS_CR_CANCELACIONES_ERROR": cr_cancelacion_error_status,
            "CANTIDAD": str(cr_cancellation_error_count)
        }
