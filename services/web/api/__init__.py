from flask import Flask, request, Response, json
from db_handler import find_url_reference, create_url_reference
from db_models import db
import uuid
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object("api.config.Config")
    db.init_app(app)
    CORS(app)

    @app.route("/api/v1/<shortened_url>", methods=["GET"])
    def get_shortened_url(shortened_url):
        return get_website(shortened_url)

    @app.route("/api/v1/create", methods=["POST"])
    def post_shortened_url():
        return create_link_shortener()

    return app


def get_website(shortened_url):
    data_entry = find_url_reference(shortened_url)
    if (data_entry and "message" in data_entry):
        return Response(json.dumps(data_entry), status=404, mimetype='application/json')

    return Response(json.dumps(data_entry), status=200, mimetype='application/json')


def create_link_shortener():
    data = validate_json(request.get_json())

    posted_data = create_url_reference(data)
    if (posted_data and "message" in posted_data):
        return Response(json.dumps(posted_data), status=400, mimetype='application/json')

    return Response(json.dumps(posted_data), status=200, mimetype='application/json')


def validate_json(data):
    if ("url_reference" not in data):
        data["url_reference"] = str(uuid.uuid4())
    return data
