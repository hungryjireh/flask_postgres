from flask.cli import FlaskGroup
from api import create_app
from db_models import db, UrlMapper


app = create_app()
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(UrlMapper(url="https://www.tech.gov.sg/", url_reference="govtech"))
    db.session.commit()


if __name__ == "__main__":
    cli()
