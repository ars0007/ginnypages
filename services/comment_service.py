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
    response = GenericDao("comments").update_record(payload,
                                                    filter_query={"page_id": page_id, "user_id": payload["user_id"]},
                                                    projection={"_id": 0})
    if response:
        return utils.prepare_response(200, message="page successfully updated ", body=response)
    else:
        return utils.prepare_response(500, error="error while updating page")


def delete_comment(comment_id):
    response = GenericDao("comments").delete_record(filter_query={"comment_id": comment_id}, projection={"_id": 0})
    if response:
        return utils.prepare_response(200, message="page deleted successfully", body=response)
    else:
        return utils.prepare_response(500, error="error while deleting page")


def get_comments(page_id):
    comment_details = GenericDao("comments").find_records(filter_query={"page_id": page_id}, projection={"_id": 0})
    response = []
    for comment_detail in comment_details:
        res = utils.get_user_detials(comment_detail, comment=True)
        response.append(res)
    if response:
        return utils.prepare_response(200, message="successfull", body=response)
    else:
        return utils.prepare_response(500, error="failure")
