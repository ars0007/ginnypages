from dao.dao import GenericDao
from uuid import uuid4
import utils.utils as utils


def create_page(payload):
    payload["page_id"] = str(uuid4())
    response = GenericDao("pages").insert_record(payload)
    if response:
        return utils.prepare_response(201, message="page successfully created")
    else:
        return utils.prepare_response(500, error="error while saving page")


def update_page(payload, page_id):
    response = GenericDao("pages").update_record(payload, filter_query={"page_id": page_id})
    if response:
        return utils.prepare_response(200, message="page successfully updated ")
    else:
        return utils.prepare_response(500, error="error while updating page")


def delete_page(page_id):
    response = GenericDao("pages").delete_record(filter_query={"page_id": page_id})
    if response:
        return utils.prepare_response(200, message="page deleted successfully")
    else:
        return utils.prepare_response(500, error="error while deleting page")


def get_page(page_id):
    response = GenericDao("pages").find_one_record(filter_query={"page_id": page_id}, projection={"_id": 0})
    if response:
        return utils.prepare_response(200, message="successfull", body=response)
    else:
        return utils.prepare_response(500, error="failure")
