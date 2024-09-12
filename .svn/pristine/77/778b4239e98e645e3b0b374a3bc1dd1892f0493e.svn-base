from flask import Flask
from flask.testing import FlaskClient
import pytest
from app import create_app, db
from app.modules.CFD_recepcion import User

@pytest.fixture(scope='module')
def app() -> Flask: # type: ignore
    """
    Fixture to create a Flask application instance for testing.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def client(app) -> FlaskClient:
    """
    Fixture to provide a test client for making requests.

    Args:
        app (Flask): The Flask application instance.
    
    Returns:
        FlaskClient: The test client.
    """
    return app.test_client()

@pytest.fixture(scope='module')
def init_db(app) -> None: # type: ignore
    """
    Fixture to set up and tear down the database for testing.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        None
    """
    db.create_all()
    user = User(username='testuser', email='testuser@example.com')
    db.session.add(user)
    db.session.commit()
    
    yield db
    
    db.drop_all()

def test_user_model(init_db) -> None:
    """
    Test the User model to ensure it works correctly.

    Args:
        init_db: The initialized database fixture.
    
    Returns:
        None
    """
    user = User.query.filter_by(username='testuser').first()
    assert user is not None
    assert user.email == 'testuser@example.com'
