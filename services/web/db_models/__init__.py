from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class UrlMapper(db.Model):
    __tablename__ = "url_mapper"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    url_reference = db.Column(db.String(128), unique=True, nullable=False)
    url = db.Column(db.String(128), nullable=False)
