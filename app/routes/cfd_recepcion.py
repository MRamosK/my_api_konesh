from . import main
from flask import Blueprint, jsonify # type: ignore
from app.services.cfdi_status_service import CFDIStatusService
from app.repositories.cfdi_repository import CFDIRepository
from datetime import datetime

main = Blueprint('cfd_recepcion', __name__)

# API Route for CFDI status
@main.route('/cfdi/status', methods=['GET'])
def get_cfdi_status():
    """
    API endpoint to get CFDI status.

    Returns:
        str: JSON response containing the CFDI status.
    """
    service = CFDIStatusService(CFDIRepository())
    response = service.build_cfdi_status_json(datetime.now())
    return jsonify(response)

# API Route for CFDI rejected
@main.route('/cfdi/rejected', methods=['GET'])
def get_cfdi_rejected():
    """
    API endpoint to get rejected CFDIs.

    Returns:
        str: JSON response containing rejected CFDIs status.
    """
    service = CFDIStatusService(CFDIRepository())
    response = service.build_cfdi_rechazados_json(datetime.now())
    return jsonify(response)

# API Route for CFDI extemporaneous
@main.route('/cfdi/extemporaneous', methods=['GET'])
def get_cfdi_extemporaneous():
    """
    API endpoint to get extemporaneous CFDIs.

    Returns:
        str: JSON response containing extemporaneous CFDIs status.
    """
    service = CFDIStatusService(CFDIRepository())
    response = service.build_cfdi_extemporaneos_json(datetime.now())
    return jsonify(response)

# API Route for CFDI incidents
@main.route('/cfdi/incidents', methods=['GET'])
def get_cfdi_incidents():
    """
    API endpoint to get CFDI incidents.

    Returns:
        str: JSON response containing CFDI incidents status.
    """
    service = CFDIStatusService(CFDIRepository())
    response = service.build_cfdi_incidencias_json(datetime.now())
    return jsonify(response)

# API Route for CR status
@main.route('/cr/status', methods=['GET'])
def get_cr_status():
    """
    API endpoint to get CR status.

    Returns:
        str: JSON response containing CR status.
    """
    service = CFDIStatusService(CFDIRepository())
    response = service.build_cr_status_json(datetime.now())
    return jsonify(response)

# API Route for CR pending cancellations
@main.route('/cr/cancellations/pending', methods=['GET'])
def get_cr_pending_cancellations():
    """
    API endpoint to get pending CR cancellations.

    Returns:
        str: JSON response containing CR pending cancellations status.
    """
    service = CFDIStatusService(CFDIRepository())
    response = service.build_cr_pendientes_json(datetime.now())
    return jsonify(response)

# API Route for CR cancellation errors
@main.route('/cr/cancellations/errors', methods=['GET'])
def get_cr_cancellation_errors():
    """
    API endpoint to get CR cancellation errors.

    Returns:
        str: JSON response containing CR cancellation errors status.
    """
    service = CFDIStatusService(CFDIRepository())
    response = service.build_cr_cancelacion_error_json(datetime.now())
    return jsonify(response)







# @main.route('/users/<int:id>', methods=['GET'])
# def get_user(id):
#     """
#     Get a user by ID.

#     Args:
#         id (int): User ID.

#     Returns:
#         str: JSON response containing user data.
#     """
#     user = User.query.get_or_404(id)
#     return jsonify(user_schema.dump(user))

# @main.route('/users', methods=['POST'])
# def create_user():
#     """Crear un nuevo usuario"""
#     data = request.get_json()
#     try:
#         # Cargar y validar los datos usando el esquema
#         user_data = user_schema.load(data)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

#     # Crear una instancia del modelo User con los datos validados
#     new_user = User(user_name=user_data['user_name'], email=user_data['email'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(user_schema.dump(new_user)), 201

# @main.route('/users/<int:id>', methods=['PUT'])
# def update_user(id: int) -> str:
#     """
#     Update an existing user.

#     Args:
#         id (int): User ID.

#     Returns:
#         str: JSON response containing the updated user.
#     """
#     user = User.query.get_or_404(id)
#     data = request.get_json()
#     try:
#         user_data = user_schema.load(data)  # Validar los datos con el esquema
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

#     # Actualizar el usuario con los datos validados
#     user.user_name = user_data.get('user_name', user.user_name)
#     user.email = user_data.get('email', user.email)
#     db.session.commit()
#     return jsonify(user_schema.dump(user))


# @main.route('/users/<int:id>', methods=['DELETE'])
# def delete_user(id: int) -> str:
#     """
#     Delete a user by ID.

#     Args:
#         id (int): User ID.

#     Returns:
#         str: JSON response indicating success.
#     """
#     user = User.query.get_or_404(id)
#     db.session.delete(user)
#     db.session.commit()
#     return jsonify({'message': 'User deleted successfully'})


# @main.route('/login')
# def login() -> str:
#     """
#     Route for the user login page.

#     Returns:
#         str: The rendered template for the user login page.
#     """
#     return render_template('users/login.html')

# @main.route('/signup')
# def signup() -> str:
#     """
#     Route for the user signup page.

#     Returns:
#         str: The rendered template for the user signup page.
#     """
#     return render_template('users/sign_up.html')
