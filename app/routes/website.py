from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.website import create_website, get_websites_by_user, get_website_by_id, update_website, delete_website
from app.services.openai import generate_website_content
from app.utils.responses import success_response,error_response
from bson.objectid import ObjectId
from flask import  Blueprint,request

website_bp = Blueprint("website", __name__)

@website_bp.route("/", methods=["POST"])
@jwt_required()
def create_new():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    content = generate_website_content(data["business_type"], data["industry"])
    layout = {"theme": "modern"}
    result = create_website(user_id, data["business_type"], data["industry"], content, layout)
    return success_response("Website created", {"id": str(result.inserted_id)}, status_code=201)


@website_bp.route("/", methods=["GET"])
@jwt_required()
def list_websites():
    user_id = get_jwt_identity()
    websites = get_websites_by_user(user_id)
    for w in websites:
        w["_id"] = str(w["_id"])
    return success_response("Websites fetched", websites)

@website_bp.route("/<website_id>", methods=["PUT"])
@jwt_required()
def edit_website(website_id):
    data = request.get_json()
    update_website(website_id, data)
    return success_response("Website updated")


@website_bp.route("/<website_id>", methods=["DELETE"])
@jwt_required()
def delete_site(website_id):
    delete_website(website_id)
    return success_response("Website deleted")


