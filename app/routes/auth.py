from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import create_user, find_user_by_email
from app.utils.responses import success_response, error_response

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if find_user_by_email(email):
            return error_response("Email already exists", 409)

        hashed_pw = generate_password_hash(password)
        create_user(email, hashed_pw)
        return success_response("User created successfully", status_code=201)
    except Exception as e:
        print('error',e)
        return error_response(str(e), 500)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = find_user_by_email(email)
    if not user or not check_password_hash(user["password"], password):
        return error_response("Invalid credentials", 401)

    access_token = create_access_token(identity=str(user["_id"]))
    return success_response("Login successful", {"token": access_token})

