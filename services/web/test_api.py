import pytest
from api import create_app, validate_json


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_validate_json():
    test_json_1 = {
        "url": "https://www.google.com",
        "url_reference": "google"
    }
    validated_test_json_1 = validate_json(test_json_1)
    assert "url_reference" in validated_test_json_1

    test_json_2 = {
        "url": "https://www.google.com"
    }
    validated_test_json_2 = validate_json(test_json_2)
    assert "url_reference" in validated_test_json_2
