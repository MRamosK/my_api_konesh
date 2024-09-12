from app.repositories.cfdi_repository import CFDIRepository
from datetime import datetime
from collections import OrderedDict

# Business Logic Layer (BLL)
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
        Get the status of CFDIs and CRs based on various time-based conditions.

        Returns:
            dict: A JSON-compatible dictionary with the CFDI and CR statuses.
        """

        # Obtener los conteos usando el repositorio
        pending_count = self.repo.fetch_pending_cfd_count()
        rejected_count = self.repo.fetch_rejected_cfd_count()
        extemporaneous_count = self.repo.fetch_extemporaneous_cfd_count()
        incidents_count = self.repo.fetch_incidents_cfd_count()
        cr_count = self.repo.fetch_status_cr_count()
        cr_pending_cancellation_count = self.repo.fetch_peding_cancellation_cr_count()
        cr_cancellation_error_count = self.repo.fetch_cancellation_error_cr_count()

        # Construir y retornar la respuesta JSON
        return self.build_response_json(datetime.now(), pending_count, rejected_count,
                                        extemporaneous_count, incidents_count, cr_count,
                                        cr_pending_cancellation_count, cr_cancellation_error_count)

    def build_response_json(self, fecha: datetime, pending_count: int, rejected_count: int,
                            extemporaneous_count: int, incidents_count: int, cr_count: int,
                            cr_pending_cancellation_count: int, cr_cancellation_error_count: int) -> dict:
        """
        Build a JSON response with CFDI and CR statuses.

        Args:
            fecha (datetime): The current date and time.
            pending_count (int): The count of pending CFDIs.
            rejected_count (int): The count of rejected CFDIs.
            extemporaneous_count (int): The count of extemporaneous CFDIs.
            incidents_count (int): The count of CFDIs with incidents.
            cr_count (int): The count of CRs with pending status.
            cr_pending_cancellation_count (int): The count of CRs pending cancellation.
            cr_cancellation_error_count (int): The count of CRs with cancellation errors.

        Returns:
            dict: A JSON-compatible dictionary with the CFDI and CR statuses.
        """
        cfdi_status = "EXISTEN_PENDIENTES_CFDI" if pending_count > 0 else "ENVIOS_CFDI_OK"
        cfdi_rechazados_status = "EXISTEN_RECHAZOS" if rejected_count > 0 else "SIN_RECHAZOS"
        cfdi_extemporaneos_status = "EXISTEN_EXTEMPORANEOS" if extemporaneous_count > 0 else "SIN_EXTEMPORANEOS"
        cfdi_incidentes_status = "EXISTEN_INCIDENCIAS" if incidents_count > 0 else "SIN_INCIDENCIAS"
        cr_status = "EXISTEN_PENDIENTES_CR" if cr_count > 0 else "ENVIOS_CR_OK"
        cr_pediente_cancelar_satus = "EXISTEN_PENDIENTES_CANCELACIONES_CR" if cr_pending_cancellation_count > 0 else "CANCELACIONES_CR_OK"
        cr_cancelacion_error_status = "EXISTEN_ERRORES_CANCELACION_C" if cr_cancellation_error_count > 0 else "ESTATUS_CR_CANCELACIONES_OK"

        response = OrderedDict({
            "fecha": fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "CFDI": [
                {
                    "CFDI_ESTATUS": cfdi_status,
                    "CANTIDAD": str(pending_count)
                }
            ],
            "CFDI_RECHAZADOS": [
                {
                    "ESTATUS_CFDI_RECHAZADOS": cfdi_rechazados_status,
                    "CANTIDAD": str(rejected_count)
                }
            ],
            "CFDI_EXTEMPORANEOS": [
                {
                    "ESTATUS_CFDI_EXTEMPORANEOS": cfdi_extemporaneos_status,
                    "CANTIDAD": str(extemporaneous_count)
                }
            ],
            "CFDI_INCIDENCIAS": [
                {
                    "ESTATUS_CFDI_INCIDENCIAS": cfdi_incidentes_status,
                    "CANTIDAD": str(incidents_count)
                }
            ],
            "CR": [
                {
                    "ESTATUS_CR": cr_status,
                    "CANTIDAD": str(cr_count)
                }
            ],
            "CR_CANCELACIONES_PENDIENTES": [
                {
                    "ESTATUS_CR_CANCELACIONES_PENDIENTES": cr_pediente_cancelar_satus,
                    "CANTIDAD": str(cr_pending_cancellation_count)
                }
            ],
            "CR_CANCELACIONES_ERROR": [
                {
                    "ESTATUS_CR_CANCELACIONES_ERROR": cr_cancelacion_error_status,
                    "CANTIDAD": str(cr_cancellation_error_count)
                }
            ]
        })
        
        return response