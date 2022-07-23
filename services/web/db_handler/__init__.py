from db_models import UrlMapper, db


def find_url_reference(reference):
    reference_entry = UrlMapper.query.filter_by(url_reference=reference).first()
    if (reference_entry):
        queried_data_response_parsed = {"url": reference_entry.url, "url_reference": reference_entry.url_reference}
        return queried_data_response_parsed

    return {"url": reference, "message": "URL not found"}


def create_url_reference(json):
    try:
        reference_entry = UrlMapper(url_reference=json["url_reference"], url=json["url"])
        db.session.add(reference_entry)
        db.session.commit()
        posted_data_response_parsed = {"url": reference_entry.url, "url_reference": reference_entry.url_reference}
        return posted_data_response_parsed
    except Exception as error:
        exception_message = {"message": error.orig.args}
        if error.args and len(error.args) > 0:
            error_message_parsed = error.args[0].split("\n")
            if (len(error_message_parsed) > 1):
                exception_message = {"message": error_message_parsed[0], "detail": error_message_parsed[1].strip("DETAIL:  ")}

        return exception_message
