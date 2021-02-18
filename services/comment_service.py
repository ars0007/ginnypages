from dao.dao import GenericDao
from uuid import uuid4
import utils.utils as utils


def create_comment(payload, page_id):
    payload["comment_id"] = str(uuid4())
    payload["page_id"] = page_id
    response = GenericDao("comments").insert_record(payload)
    if response:
        return utils.prepare_response(201, message="comment successfully added")
    else:
        return utils.prepare_response(500, error="error while adding comment")


def update_comment(payload, page_id):
    payload["page_id"] = page_id
    response = GenericDao("pages").update_record(payload,
                                                 filter_query={"page_id": page_id, "user_id": payload["user_id"]})
    if response:
        return utils.prepare_response(200, message="page successfully updated ")
    else:
        return utils.prepare_response(500, error="error while updating page")


def delete_comment(page_id):
    response = GenericDao("pages").delete_record(filter_query={"page_id": page_id})
    if response:
        return utils.prepare_response(200, message="page deleted successfully")
    else:
        return utils.prepare_response(500, error="error while deleting page")


def get_comments():
    response = GenericDao("pages").find_records(projection={"_id": 0})
    if response:
        return utils.prepare_response(200, message="successfull", body=response)
    else:
        return utils.prepare_response(500, error="failure")
